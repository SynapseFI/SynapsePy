
from .node import Node
from .nodes import Nodes

from functools import partial

import api.models.errors as api_errors
import requests
import json

class User():
	""" User Record
	"""

	paths = {
		'oauth': '/oauth/',
		'client': '/client',
		'users': '/users',
		'trans': '/trans',
		'nodes': '/nodes',
		'subs': '/subscriptions',
		'inst': '/institutions'
		}

	def __init__(self, response, http, full_dehydrate=False):
		"""
		Args:
			response: response from api of user record
		"""
		self.id = response['_id']
		self.body = response
		self.full_dehydrate = full_dehydrate
		self.http = http
		self.oauth_key = ''

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
		path = self.paths['users'] + '/' + self.id
		self.body = self.http.get(path, full_dehydrate=self.full_dehydrate)
		return self.body['refresh_token']

	def oauth(self, scope=[]):
		'''creates a new OAuth for the user
		Args:
			user (json): User to create new OAuth for
			scope (list): permissions allowed for OAuth key
		Returns:
			OAuth (Str): newly created OAuth within scope
		'''
		path = self.paths['oauth'] + self.id
		body = { 'refresh_token': self.body['refresh_token'] }

		if scope:
			body['scope'] = scope

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
		path = self.paths['users'] + '/' + self.id
		response = self.do_request(self.http.patch, path, body=body)
		self.body = response
		return response

	def create_node(self, type, payload):
		path = self.paths['users'] + '/' + self.id + self.paths['nodes']
		
		body = { 'type': type }
		body.update(payload)

		response = self.do_request(self.http.post, path, body=body)
		return Node(response, self.http)

	def create_deposit_us(self, payload):
		return self.create_node('DEPOSIT-US', payload)

	def create_ach(self, payload):
		return self.create_node('ACH-US', payload)

	def create_interchange(self, payload):
		return self.create_node('INTERCHANGE-US', payload)

	def create_check(self, payload):
		return self.create_node('CHECK-US', payload)

	def create_crypto(self, payload):
		return self.create_node('CRYPTO-US', payload)

	def create_wire_us(self, payload):
		return self.create_node('WIRE-US', payload)

	def create_wire_int(self, payload):
		return self.create_node('WIRE-INT', payload)

	def create_iou(self, payload):
		return self.create_node('IOU', payload)

	def get_node(self, node_id, **params):
		'''
		'''
		path = self.paths['users'] + '/' + self.id + self.paths['nodes'] +'/'+ node_id

		full_dehdyrate = 'yes' if params.get('full_dehdyrate') else 'no'
		force_ref = 'yes' if params.get('force_refresh') else 'no'

		response = self.do_request(self.http.get, path, full_dehydrate=full_dehydrate, force_refresh=force_refresh)
		return Node(response, self.http, full_dehdyrate=full_dehdyrate)

	def get_all_nodes(self, **params):
		'''
		'''
		path = self.paths['users'] + '/' + self.id + self.paths['nodes']
		response = self.do_request(self.http.get, path, **params)
		return Nodes(response, self.http)