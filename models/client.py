
from .http_client import HttpClient

from .user import User, Users
from .node import Node, Nodes
from .transaction import Trans, Transactions
from .subscription import Subscription, Subscriptions

from .endpoints import paths

import sys
import json
import logging
import requests
import models.errors as api_errors

class Client():
	""" Client Record """

	def __init__(self, client_id, client_secret, fingerprint, ip_address, devmode=False, logging=False):
		"""
		Args:
			client_id (str): API client id
			client_secret (str): API client secret
			fingerprint (str):
			ip_address (str):
			devmode (bool): (opt) switches between sandbox and production base_url
			logging (bool): (opt) enables logger
		"""
		self.client_id = client_id
		self.client_secret = client_secret
		
		self.http = HttpClient(
			client_id=client_id,
			client_secret=client_secret,
			fingerprint=fingerprint,
			ip_address=ip_address,
			base_url=
				'https://uat-api.synapsefi.com/v3.1' 
				if devmode else
				'https://api.synapsefi.com/v3.1',
			logging=logging
			)
		self.logging = logging
		self.logger = self.get_log(logging)

	def update_headers(self, client_secret=None, fingerprint=None, ip_address=None, oauth_key=None, idempotency_key=None):
		'''Updates session headers
		'''
		self.http.update_headers(
			client_secret=client_secret,
			fingerprint=fingerprint,
			ip_address=ip_address,
			oauth_key=oauth_key,
			idempotency_key=idempotency_key
			)

	def get_log(self, enable):
		'''Enables/Disables logs
		Args:
			enable (bool): enables if True, disables if False
		Returns:
			logger (Logger): logging.Logger object used to debug
		'''
		logging.basicConfig()
		logger = logging.getLogger(__name__)
		logger.setLevel(logging.DEBUG)
		logger.disabled = not enable

		return logger

	def create_user(self, body, idempotency_key=None):
		"""
		Args:
			body (json): user record
			json (json): JSON
		Returns:
			user (User): object containing User record
		"""
		self.logger.debug("Creating a new user")

		path = paths['users']
		response = self.http.post(
			path, body, idempotency_key=idempotency_key
		)
		
		return User(response, self.http, full_dehydrate=False, logging=self.logging)
	
	def create_subscription(self, webhook_url, scope, idempotency_key=None):
		'''
		Args:
			webhook_url (str): subscription url
			scope (list of str): API call types to subscribe to
		Returns:
			
		'''
		self.logger.debug("Creating a new subscription")

		path = paths['subs']

		body = {
			'scope': scope,
			'url': webhook_url
		}

		response = self.http.post(
			path, body, idempotency_key=idempotency_key
		)
		return Subscription(response)

	def get_user(self, user_id, full_dehydrate=False):
		"""Returns user object
		Args:
			user_id (Str): identification for user
		Returns:
			user (User): object containing User record
		"""
		self.logger.debug("getting a user")

		path = paths['users'] + '/' + user_id
		full_d = 'yes' if full_dehydrate else None
		response = self.http.get(path, full_dehydrate=full_d)
		return User(response, self.http, full_dehydrate=full_d, logging=self.logging)

	def get_subscription(self, sub_id):
		'''
		Args:
			sub_id (Str): subscription id
		Returns:
			(Subscription Object)
		'''
		self.logger.debug("getting a subscription")

		path = paths['subs'] + '/' + sub_id
		response = self.http.get(path)
		return Subscription(response)

	def update_subscription(self, sub_id, body, idempotency_key=None):
		'''
		Args:
			sub_id (str): subscription id
			body (JSON): update body
		Returns:
			(Subscription): object containing subscription record
		'''
		# self.logger.debug("updating subscription")

		url = paths['subs'] + '/' + sub_id
		response = self.http.patch(url, body)
		return Subscription(response)

	def crypto_quotes(self):
		'''
		'''
		path = paths['nodes'] + paths['cryptoq']
		response = self.http.get(path)
		return response

	def crypto_market_data(self, limit=None, currency=None):
		'''
		'''
		path = paths['nodes'] + paths['cryptom']
		response = self.http.get(
			path, limit=limit, currency=currency
		)
		return response

	def locate_atms(self, zip=None, lat=None, rad=None, page=None, per_page=None):
		'''
		'''
		path = paths['nodes'] + paths['atms']
		response = self.http.get(
			path,
			zip=zip,
			lat=lat,
			radius=rad,
			page=page,
			per_page=per_page
		)
		return response

	def issue_public_key(self, scope):
		'''
		Args:

		'''
		self.logger.debug("issuing a public key")
		
		path = paths['client']

		response = self.http.get(
			path, issue_public_key='YES', scope=scope
		)
		return response['public_key_obj']

	def get_all_users(self, query=None, page=None, per_page=None, show_refresh_tokens=None):
		"""Returns all user objects in a list
		Returns:
			(list of Json): json containing User records
		"""
		self.logger.debug("getting all users")

		path = paths['users']
		response = self.http.get(
			path,
			query=query,
			page=page,
			per_page=per_page,
			show_refresh_tokens=show_refresh_tokens
		)
		return Users(response, self.http)

	def get_all_trans(self, page=None, per_page=None):
		'''gets all client transactions
		Returns:
			(list of Transactions): list of all transaction records for client
		'''
		self.logger.debug("getting all transactions")
		
		path = paths['trans']
		response = self.http.get(
			path, page=page, per_page=per_page
		)
		return Transactions(response)

	def get_all_nodes(self, query=None, page=None, per_page=None, show_refresh_tokens=None):
		'''gets all client nodes
		Returns:
			(list of Nodes): list of all node records for client
		'''
		self.logger.debug("getting all nodes")
		
		path = paths['nodes']
		response = self.http.get(path)
		return Nodes(response)

	def get_all_subs(self, page=None, per_page=None):
		'''
		'''
		self.logger.debug("getting all subscriptions")
		
		path = paths['subs']
		response = self.http.get(
			path, page=page, per_page=per_page
		)
		return Subscriptions(response)

	def get_all_inst(self):
		'''
		'''
		self.logger.debug("getting all institutions")
		
		path = paths['inst']
		response = self.http.get(path)
		return response


