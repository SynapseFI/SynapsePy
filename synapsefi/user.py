
from .endpoints import paths

from .node import Node, Nodes
from .subnet import Subnet, Subnets
from .transaction import Trans, Transactions

from functools import partial

import json
import logging
import requests
from . import errors as api_errors

class User():
	""" User Record
	"""

	def __init__(self, response, http, full_dehydrate=False, logging=False):
		"""Initializes the User by parsing response from API
		"""
		self.id = response['_id']
		self.body = response
		self.full_dehydrate = full_dehydrate
		self.http = http

		self.logger = self.get_log(logging)

	def refresh(self):
		'''gets a new refresh token by getting user
		Args:
			user (JSON): json response for user record with old_refresh_token
		Returns:
			dict: dict response of user record with new refresh_token
		'''
		path = paths['users'] + '/' + self.id

		self.body = self.http.get(path, full_dehydrate=self.full_dehydrate)
		return self.body['refresh_token']

	def oauth(self, payload=None):
		'''Gets new OAuth for user and updates the headers
		Args:
			payload (:obj:dict, optional): (opt)
		Returns:
			OAuth (str): newly created OAuth within scope
		'''
		path = paths['oauth'] + '/' + self.id

		body = {'refresh_token': self.body['refresh_token']}

		if payload:
			body.update(payload)

		try:
			response = self.http.post(path, body)

		except api_errors.IncorrectValues as e:
			self.refresh()
			body['refresh_token'] = user.body['refresh_token']
			response = self.http.post(path, body)

		self.http.update_headers(
			oauth_key=response['oauth_key']
		)
		return response

	def select_2fa_device(self, device):
		'''Sends MFA pin to specific device
		Args:
			device (str): device to send pin to
		Returns:
			dict: dictionary containing API response
		'''
		path = paths['oauth'] + '/' + self.id

		body = {
			'refresh_token': self.body['refresh_token'],
			'phone_number': device
			}

		response = self.http.post(path, body)
		return response


	def confirm_2fa_pin(self, pin):
		'''Confirms pin sent to device
		Args:
			pin (str): validation_pin sent to user's device
		Returns:
			dict: dictionary containing API response
		'''
		path = paths['oauth'] + '/' + self.id

		body = {
			'refresh_token': self.body['refresh_token'],
			'validation_pin': pin
			}

		response = self.http.post(path, body)
		self.http.update_headers(
			oauth_key=response['oauth_key']
		)
		return response

	def _do_request(self, req_func, path, body={}, **params):
		'''Single point of access for user methods in the event of an invalid OAuth
		'''
		self.logger.debug(
			"{} request on {}".format(req_func.__name__, path)
		)
		self.logger.debug(json.dumps(body, indent=2))

		req_dict = {
			"get": partial(req_func, path, **params),
			"post": partial(req_func, path, body, **params),
			"patch": partial(req_func, path, body, **params),
			"delete": partial(req_func, path)
		}

		try:
			response = req_dict[req_func.__name__]()

		except (requests.exceptions.HTTPError, api_errors.IncorrectUserCredentials) as e:
			self.logger.debug(
				"user's oauth expired. re-authenticatng"
			)
			self.oauth()

			self.logger.debug(
				"Retrying {} request on {}".format(
					req_func.__name__, path
				)
			)
			self.logger.debug(body)

			response = req_dict[req_func.__name__]()
		return response

	def update_info(self, body):
		'''Updates user information in database
		Args:
			body (dict): user information to update
		Returns:
			response (User): User object containing updated info
		'''
		path = paths['users'] + '/' + self.id

		response = self._do_request(self.http.patch, path, body)
		self.body = response
		return response


	def create_node(self, body, idempotency_key=None):
		'''Creates a new Node for User
		Args:
			body (dict): dictionary containing new Node information
			idempotency_key: (opt) Idempotency key for safely retrying requests
		'''
		path = paths['users'] + '/' + self.id + paths['nodes']

		response = self._do_request(
			self.http.post,
			path,
			body,
			idempotency_key=idempotency_key
		)

		if response.get('mfa'):
			return response
		return Nodes(response)

	def get_node(self, node_id, full_dehydrate=False, force_refresh=False):
		'''Gets Node from database
		Args:
			node_id (str): Node ID for the Node you are trying to get
			full_dehydrate (bool): (opt) Full Dehydrate True will will return back all the node info,
				including decrypted account/routing number, transaction history, etc.
			force_refresh (bool): (opt) If the node was created with bank logins,
				force refresh yes will attempt updating the account balance and transactions
		Returns:
			Node: Node object containing node info
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+'/'
			+ node_id
		)
		full_d = 'yes' if full_dehydrate else 'no'
		force_r = 'yes' if force_refresh else 'no'

		response = self._do_request(
			self.http.get,
			path,
			full_dehydrate=full_d,
			force_refresh=force_r
		)
		return Node(response, full_dehydrate=full_dehydrate)

	def update_node(self, node_id, body):
		'''Updates a node's info in the database
		Args:
			node_id (str): ID of the Node to update
			body (dict): dictionary containing updated info
		Returns:
			Node: Node object with updated info
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
		)
		response = self._do_request(self.http.patch, path, body)
		return Node(response)

	def ach_mfa(self, body):
		'''MFA to add user to database through bank logins
		Args:
			body (dict): dictionary containing access_token and mfa_answer
		Returns:
			Nodes: Nodes object containing aggregated accounts
			or
			dict: dictionary response if another MFA flow is needed
		'''
		path = paths['users'] + '/' + self.id + paths['nodes']

		response = self._do_request(self.http.post, path, body)

		if response.get('mfa'):
			return response
		return Nodes(response)

	def verify_micro(self, node_id, body):
		'''Verifies micro transactions for adding ACH-US Node with AC/RT
		Args:
			node_id (str): ID of the Node to verify
			body (dict): dictionary containing micro (list of micro-deposit amounts)
		Returns:
			Node: Node object containing node info
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
		)
		response = self._do_request(self.http.patch, path, body)
		return Node(response)

	def reinit_micro(self, node_id):
		'''Reinitiates micro-deposit for an ACH-US Node
		Args:
			node_id (str): ID of the Node object to reinitiate micro deposits for
		Returns:
			dict: dictionary of response from API	
		'''
		self.logger.debug(
			"reinitiating micro transaction for node_id: {}".format(
				node_id
			)
		)
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
		)
		response = self._do_request(
			self.http.patch, path, {}, resend_micro='YES'
		)
		return response

	def ship_debit(self, node_id, body):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
		)
		response = self._do_request(
			self.http.patch, path, body, ship='YES'
		)
		return response

	def reset_debit(self, node_id):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
		)
		response = self._do_request(
			self.http.patch, path, {}, reset='YES'
		)
		return response

	def generate_apple_pay(self, node_id, body):
		'''Generates an ApplePay token (currently not working in API)
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['apple']
		)
		response = self._do_request(self.http.patch, path, body)
		return response

	def create_ubo(self, body):
		'''
		'''
		path = paths['users'] +'/'+ self.id + paths['ubo']
		response = self._do_request(self.http.patch, path, body)
		return response

	def delete_node(self, node_id):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
		)
		response = self._do_request(self.http.delete, path)
		return response

	def create_trans(self, node_id, body, idempotency_key=None):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['trans']
		)
		response = self._do_request(
			self.http.post,
			path,
			body,
			idempotency_key=idempotency_key
		)
		return Trans(response)

	def get_trans(self, node_id, trans_id):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['trans']
			+ trans_id
		)
		response = self._do_request(self.http.get, path)
		return Trans(response)

	def comment_trans(self, node_id, trans_id, body):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['trans']
			+ '/'
			+ trans_id
		)

		response = self._do_request(self.http.patch, path, body)
		return response

	def dispute_trans(self, node_id, trans_id, dispute_reason):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+'/'
			+ node_id
			+ paths['trans']
			+ '/'
			+ trans_id
			+ paths['dispute']
		)

		body = { 'dispute_reason': dispute_reason }
		response = self._do_request(self.http.patch, path, body)
		return response

	def cancel_trans(self, node_id, trans_id):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['trans']
			+ '/'
			+ trans_id
		)
		response = self._do_request(self.http.delete, path)
		return response

	def dummy_tran(self, node_id, is_credit=False):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['dummy']
		)
		credit = 'YES' if is_credit else 'NO'
		response = self._do_request(
			self.http.get, path, is_credit=credit
		)
		return response

	def create_subnet(self, node_id, body, idempotency_key=None):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['subn']
		)

		response = self._do_request(self.http.post, path, body, idempotency_key=idempotency_key)
		return Subnet(response)

	def get_subnet(self, node_id, subnet_id):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['subn']
			+ '/'
			+ subnet_id
		)
		response = self._do_request(self.http.get, path)
		return Subnet(response)

	def get_all_nodes(self, page=None, per_page=None, type=None):
		'''
		'''
		path = paths['users'] + '/' + self.id + paths['nodes']

		response = self._do_request(
			self.http.get,
			path,
			page=page,
			per_page=per_page,
			type=type
		)
		return Nodes(response)

	def get_all_node_trans(self, node_id, page=None, per_page=None):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['trans']
		)
		response = self._do_request(
			self.http.get,path, page=page, per_page=per_page
		)
		return Transactions(response)

	def get_all_trans(self, page=None, per_page=None):
		'''
		'''
		path = paths['users'] + '/' + self.id + paths['trans']
		response = self._do_request(
			self.http.get, path, page=page, per_page=per_page
		)
		return Transactions(response)

	def get_all_subnets(self, node_id, page=None, per_page=None):
		'''
		'''
		path = (
			paths['users']
			+ '/'
			+ self.id
			+ paths['nodes']
			+ '/'
			+ node_id
			+ paths['subn']
		)
		response = self._do_request(
			self.http.get, path, page=page, per_page=per_page
		)
		return Subnets(response)

	def get_log(self, enable):
		'''
		'''
		logging.basicConfig()
		logger = logging.getLogger(__name__)
		logger.setLevel(logging.DEBUG)
		logger.disabled = not enable
		return logger


class Users():

	def __init__(self, response, http):
		'''
		'''
		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.users_count = response['users_count']

		self.list_of_users = [
			User(user_r, http)
			for user_r in response['users']
		]