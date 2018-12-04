
from .endpoints import paths

from .node import Node
from .nodes import Nodes
from .subnet import Subnet
from .subnets import Subnets
from .transaction import Trans
from .transactions import Transactions

from functools import partial

import requests
import json
import api.models.errors as api_errors

class User():
	""" User Record
	"""

	def __init__(self, response, http, full_dehydrate=False):
		"""
		Args:
			response: response from api of user record
		"""
		self.id = response['_id']
		self.body = response
		self.full_dehydrate = full_dehydrate
		self.http = http

	def do_request(self, req_func, path, body={}, **params):
		'''
		'''
		req_dict = {
			"get": partial(req_func, path, **params),
			"post": partial(req_func, path, body, **params),
			"patch": partial(req_func, path, body),
			"delete": partial(req_func, path)
		}

		try:
			response = req_dict[req_func.__name__]()

		except (requests.exceptions.HTTPError, api_errors.IncorrectUserCredentials) as e:
			self.oauth()
			response = req_dict[req_func.__name__]()

		return response

	def refresh(self):
		'''gets a new refresh token by getting user
		Args:
			user (JSON): json response for user record with old_refresh_token
		Returns:
			user (JSON): json response for user record with new refresh_token
		'''
		path = paths['users'] + '/' + self.id
		self.body = self.http.get(path, full_dehydrate=self.full_dehydrate)
		return self.body['refresh_token']

	def oauth(self, payload):
		'''creates a new OAuth for the user
		Args:
			scope (list): permissions allowed for OAuth key
			phone_number (str)
			validation_pin (str)
		Returns:
			OAuth (Str): newly created OAuth within scope
		'''
		path = paths['oauth'] + '/' + self.id
		body = { 'refresh_token': self.body['refresh_token'] }
		body.update(payload)

		try:
			response = self.http.post(path, body)

		except api_errors.IncorrectValues as e:
			self.refresh()
			body['refresh_token'] = user.body['refresh_token']
			response = self.http.post(path, body)

		self.oauth_key = response['oauth_key']
		response = self.http.update_headers(oauth_key=self.oauth_key)
		return response

	def update_info(self, body):
		'''removes user from indexing (soft-deletion)
		Args:
			user (json): user record
		Returns:
			response (json): API response to patch
		'''
		path = paths['users'] + '/' + self.id
		response = self.do_request(self.http.patch, path, body)
		self.body = response
		return response


	def create_node(self, body):
		'''
		'''
		path = paths['users'] + '/' + self.id + paths['nodes']

		try:
			response = self.do_request(self.http.post, path, body)
		
		except api_errors.ActionPending as e:
			return e.response['mfa']

		return Nodes(response)

	def get_node(self, node_id, full_d=False, force_r=False):
		'''
		'''
		path = paths['users'] + '/' + self.id + paths['nodes'] +'/'+ node_id

		full_d = 'yes' if params.get('full_dehdyrate') else 'no'
		force_r = 'yes' if params.get('force_refresh') else 'no'

		response = self.do_request(self.http.get, path, full_dehydrate=full_d, force_refresh=force_r)
		return Node(response, full_dehdyrate=full_dehdyrate)

	def update_node(self, node_id, body):
		'''
		'''
		path = paths['users'] + '/' + self.id + paths['nodes'] +'/'+ node_id
		response = self.do_request(self.http.patch, path, body)
		return response

	def ach_mfa(self, body):
		'''
		'''
		path = paths['users'] + '/' + self.id + paths['nodes']
		response = self.do_request(self.http.post, path, body)
		return Node(response)

	def verify_micro(self, node_id, body):
		path = paths['users'] + '/' + self.id + paths['nodes'] + '/' + node_id
		response = self.do_request(self.http.patch, body)
		return response

	def reinit_micro(self, node_id, body):
		path = paths['users'] + '/' + self.id + paths['nodes'] + '/' + node_id
		response = self.do_request(self.http.patch, bdoy)
		return response

	def issue_card(self, body):
		path = paths['users'] + '/' + self.id + paths['nodes']
		response = self.do_request(self.http.post, path, body)
		return response

	def ship_debit(self, node_id, body):
		'''
		'''
		path = paths['users'] +'/'+ self.id + paths['nodes'] +'/'+ node_id
		response = self.do_request(self.http.patch, path, body, ship='YES')
		return response

	def reset_debit(self, node_id):
		'''
		'''
		path = paths['/users'] +'/'+ self.id + paths['/nodes'] +'/'+ node_id
		response = self.do_request(self.http.patch, path, {}, reset='YES')
		return response

	def generate_apple_pay(self, node_id, body):
		'''
		'''
		path = paths['/users'] +'/'+ self.id + paths['/nodes'] +'/'+ node_id + paths['apple']
		response = self.do_request(self.http.patch, path, body)
		return response

	def dummy_tran(self, node_id, is_credit=False):
		'''
		'''
		credit = 'YES' if is_credit else 'NO'
		path = paths['users'] +'/'+ self.id + paths['nodes'] +'/'+ node_id + paths['dummy']
		response = self.do_request(self.http.get, path, is_credit=credit)
		return response

	def delete_node(self, node_id):
		'''
		'''
		path = paths['users'] +'/'+ self.id + paths['nodes'] +'/'+ node_id
		response = self.do_request(self.http.delete, path)
		return response

	def create_trans(self, node_id, body):
		'''
		'''
		path = paths['users'] +'/'+ self.id + paths['nodes'] +'/'+ node_id + paths['trans']
		response = self.do_request(self.http.post, path, body)
		return Trans(response)

	def get_trans(self, node_id, trans_id):
		'''
		'''
		path = paths['users'] +'/'+ self.id + paths['nodes'] +'/'+ node_id + paths['trans'] + trans_id
		response = self.do_request(self.http.get, path)
		return Trans(response)

	def comment_trans(self, node_id, trans_id, body):
		'''
		'''
		path = (paths['users'] +'/'+ self.id + 
			paths['nodes'] +'/'+ node_id + 
			paths['trans'] + '/' + trans_id)

		response = self.do_request(self.http.patch, path, body)
		return response

	def cancel_trans(self, node_id, trans_id):
		'''
		'''
		path = (paths['users'] +'/'+ self.id + 
			paths['nodes'] +'/'+ node_id + 
			paths['trans'] + '/' + trans_id)

		response = self.do_request(self.http.delete, path)
		return response

	def create_subnet(self, node_id, body):
		'''
		'''
		path = (paths['users'] +'/'+ self.id + 
			paths['nodes'] +'/'+ node_id + 
			paths['subn'])

		response = self.do_request(self.http.post, path, body)
		return Subnet(response)

	def get_subnet(self, subnet_id):
		'''
		'''
		path = (paths['users'] +'/'+ self.id + 
			paths['nodes'] +'/'+ node_id + 
			paths['subn'] + '/' + subnet_id)

		response = self.do_request(self.http.get, path)
		return Subnet(response)

	def get_all_nodes(self, **params):
		'''
		'''
		path = paths['users'] + '/' + self.id + paths['nodes']
		response = self.do_request(self.http.get, path, **params)
		return Nodes(response)

	def get_all_node_trans(self):
		path = paths['users'] +'/'+ self.id + paths['nodes'] +'/'+ node_id + paths['trans']
		response = self.do_request(self.http.get, path, **params)
		return Transactions(response)

	def get_all_trans(self, **params):
		'''
		'''
		path = paths['users'] + '/' + self.id + paths['trans']
		response = self.do_request(self.http.get, path, **params)
		return Transactions(response)

	def get_all_subnets(self, node_id, page, per_page):
		'''
		'''
		path = paths['users'] +'/'+ self.id + paths['nodes'] +'/'+ node_id + paths['subn']
		response = self.do_request(self.http.get, path, page=page, per_page=per_page)
		return Subnets(response)
