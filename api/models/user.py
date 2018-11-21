
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
		self.payload = response
		self.full_dehydrate = full_dehydrate
		self.http = http
		self.oauth_key = ''

	def refresh(self):
		'''gets a new refresh token by getting user
		Args:
			user (JSON): json response for user record with old_refresh_token
		Returns:
			user (JSON): json response for user record with new refresh_token
		'''
		path = self.paths['users'] + '/' + self.id
		self.payload = self.http.get(path, full_dehydrate=self.full_dehydrate)
		return self.payload

	def oauth(self, scope=[]):
		'''creates a new OAuth for the user
		Args:
			user (json): User to create new OAuth for
			scope (list): permissions allowed for OAuth key
		Returns:
			OAuth (Str): newly created OAuth within scope
		'''
		path = self.paths['oauth'] + self.id

		payload = { 'refresh_token': self.payload['refresh_token'] }

		if scope:
			payload['scope'] = scope

		try:
			response = self.http.post(path, payload)

		except api_errors.IncorrectValues as e:
			self.refresh()
			payload['refresh_token'] = user.payload['refresh_token']
			response = self.http.post(path, payload)

		self.oauth_key = response['oauth_key']
		
		response = self.http.update_headers(oauth_key=self.oauth_key)

		return response

	def unindex(self):
		'''removes user from indexing (soft-deletion)
		Args:
			user (json): user record
		Returns:
			response (json): API response to patch
		'''
		
		path = self.paths['users'] + '/' + self.id
		payload = { "permission": "MAKE-IT-GO-AWAY" }
		self.http.update_headers(oauth_key=self.oauth_key)

		try:
			response = self.http.patch(path, payload)

		except (requests.exceptions.HTTPError, api_errors.IncorrectUserCredentials) as e:
			self.oauth()
			response = self.http.patch(path, payload)

		except Exception:
			raise
		
		return response

	def update_user(self):
		pass
	def add_document(self):
		pass
	def update_document(self):
		pass
	def delete_document(self):
		pass
	
	def get_all_nodes(self):
		pass

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