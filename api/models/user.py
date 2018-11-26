
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
		# get(path, params)
		# post(path, payload, params)
		# patch(path, payload)
		# delete(path)

		req_dict = {
			"get": partial(req_func,path, **params),
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

		# try:
		# 	response = self.http.patch(path, body)

		# except (requests.exceptions.HTTPError, api_errors.IncorrectUserCredentials) as e:
		# 	self.oauth()
		# 	response = self.http.patch(path, body)

		# except Exception:
		# 	raise

		response = self.do_request(self.http.patch, path, body=body)
		self.body = response
		return response

	def create_node(self, body, **params):
		'''
		'''
		path = self.paths['users'] + '/' + self.id + self.paths['nodes']

		try:
			response = self.http.post(path, body, **params)
		
		except (requests.exceptions.HTTPError, api_errors.IncorrectUserCredentials) as e:
			self.oauth()
			response = self.http.post(path, body, **params)

		except Exception:
			raise

		return Node(response, self.http)

	def get_node(self, node_id, **params):
		'''
		'''
		path = self.paths['users'] + '/' + self.id + self.paths['nodes'] +'/'+ node_id

		full_dehdyrate = 'yes' if params.get('full_dehdyrate') else 'no'
		force_ref = 'yes' if params.get('force_refresh') else 'no'

		try:
			response = self.http.get(path, full_dehdyrate=full_dehdyrate, force_refresh=force_ref)
		
		except (requests.exceptions.HTTPError, api_errors.IncorrectUserCredentials) as e:
			self.oauth()
			response = self.http.get(path, full_dehdyrate=full_dehdyrate, force_refresh=force_ref)

		except Exception:
			raise

		return Node(response, self.http, full_dehdyrate=full_dehdyrate)

	def get_all_nodes(self, **params):
		'''
		'''
		path = self.paths['users'] + '/' + self.id + self.paths['nodes']

		try:
			response = self.http.get(path, **params)
		
		except (requests.exceptions.HTTPError, api_errors.IncorrectUserCredentials) as e:
			self.oauth()
			response = self.http.get(path, **params)

		except Exception:
			raise

		return Nodes(response, self.http)

	# def get_trans(self, node_id, trans_id):
	# 	'''gets a specific transaction record
	# 	Args:
	# 		user_id (str): user id
	# 	'''
	# 	url = self.get_base()
	# 		+ self.paths['getuser'] + user_id
	# 		+ self.paths['getnode'] + node_id
	# 		+ self.paths['gettrans'] + trans_id

	# 	response = self.http.get(url)
	# 	return Trans(response)

	# def all_user_trans(self, **params):
	# 	url = self.get_base()
	# 		+ self.paths['getuser'] + self.id
	# 		+ self.paths['trans']

	# 	if not self.oauth:
	# 		self.oauth(self)

	# 	self.http.update_headers(oauth_key=self.oauth)

	# 	response = self.http.get(url)
	# 	return [Trans(trans_r) for trans_r in response]