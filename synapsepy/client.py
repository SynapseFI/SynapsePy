
from .http_client import HttpClient

from .user import User, Users
from .node import Node, Nodes
from .transaction import Trans, Transactions
from .subscription import Subscription, Subscriptions
from . import errors as api_errors

from .endpoints import paths

import sys
import json
import logging
import requests

class Client():
	""" Client Record """
	def __init__(self, client_id, client_secret, fingerprint, ip_address, devmode=False, logging=False):
		"""
		Args:
			client_id (str): API client id
			client_secret (str): API client secret
			fingerprint (str): device fingerprint
			ip_address (str): user IP address
			devmode (bool): (opt) switches between sandbox and production base url
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
		Args:
			client_secret (str): (opt) API client secret
			fingerprint (str): (opt) device fingerprint
			ip_address (str): (opt) user IP address
			idempotency_key (str): (opt) idempotency key for safely retrying requests
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
			Logger: logging.Logger object used to debug
		'''
		logging.basicConfig()
		logger = logging.getLogger(__name__)
		logger.setLevel(logging.DEBUG)
		logger.disabled = not enable

		return logger

	def create_user(self, body, ip, fingerprint=None, idempotency_key=None):
		"""Creates a User object containing a user's record
		Args:
			body (dict): user record
			ip (str): IP address of the user to create
			fingerprint (str) (opt): device fingerprint of the user 
			idempotency_key (str): (opt) idempotency key for safely retrying requests
		Returns:
			user (User): object containing User record
		"""
		self.logger.debug("Creating a new user")

		path = paths['users']

		if fingerprint:
			self.update_headers(fingerprint=fingerprint)
		self.update_headers(ip_address=ip)

		response = self.http.post(
			path, body, idempotency_key=idempotency_key
		)
		return User(response, self.http, full_dehydrate=False, logging=self.logging)

	def get_user(self, user_id, ip=None, fingerprint=None, full_dehydrate=False):
		"""Returns User object grabbed from API
		Args:
			user_id (str): identification for user
			ip (str) (opt): IP address of the user to create
			fingerprint (str) (opt): device fingerprint of the user 
			full_dehydrate (bool) (opt): Full Dehydrate True will return back user's KYC info.
		Returns:
			user (User): object containing User record
		"""
		self.logger.debug("getting a user")

		if ip:
			self.update_headers(ip_address=ip)
		if fingerprint:
			self.update_headers(fingerprint=fingerprint)

		path = paths['users'] + '/' + user_id
		full_d = 'yes' if full_dehydrate else None
		response = self.http.get(path, full_dehydrate=full_d)
		return User(response, self.http, full_dehydrate=full_d, logging=self.logging)
	
	def create_subscription(self, webhook_url, scope, idempotency_key=None):
		'''Creates a webhook
		Args:
			webhook_url (str): subscription url
			scope (list of str): API call types to subscribe to
		Returns:
			dict: dictionary object containing json response
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

	def get_subscription(self, sub_id):
		'''Returns Subscription object of webhook
		Args:
			sub_id (Str): subscription id
		Returns:
			Subscription Object
		'''
		self.logger.debug("getting a subscription")

		path = paths['subs'] + '/' + sub_id
		response = self.http.get(path)
		return Subscription(response)

	def update_subscription(self, sub_id, body, idempotency_key=None):
		'''Updates a webhook
		Args:
			sub_id (str): subscription id
			body (JSON): update body
		Returns:
			(Subscription): object containing subscription record
		'''
		self.logger.debug("updating subscription")

		path = paths['subs'] + '/' + sub_id
		response = self.http.patch(path, body)
		return Subscription(response)

	def webhook_logs(self):
		'''Returns all of the webhooks sent by SynapseFi
		'''
		headers = self.http.get_headers()
		content_type = headers.pop('Content-Type')
		path = paths['subs'] + paths['logs']
		response = self.http.get(path)
		headers['Content-Type'] = content_type
		return response

	def crypto_quotes(self):
		'''Gets quotes for crypto currencies
		Returns:
			dict: dictionary containing crypto quotes
		'''
		path = paths['nodes'] + paths['cryptoq']
		response = self.http.get(path)
		return response

	def crypto_market_data(self, limit=None, currency=None):
		'''Returns current market data for a particular crytpo-currency
		Args:
			limit (int): (opt) Number of days from today
			currency (str): (opt) crypto-currency to grab market data for
		Returns:
			dict: dictionary containing market data for crypto-currency
		'''
		path = paths['nodes'] + paths['cryptom']
		response = self.http.get(
			path, limit=limit, currency=currency
		)
		return response

	def trade_market_data(self, ticker):
		'''Returns current market data for a particular crytpo-currency
		Args:
			limit (int): (opt) Number of days from today
			currency (str): (opt) crypto-currency to grab market data for
		Returns:
			dict: dictionary containing market data for crypto-currency
		'''
		path = paths['nodes'] + paths['trade']
		response = self.http.get(
			path, ticker=ticker
		)
		return response

	def locate_atms(self, zip=None, lat=None, lon=None, rad=None, page=None, per_page=None):
		'''Returns atms closest to a particular coordinate
		Args:
			zip (str): (opt) Zip code for ATM locator
			lat (str): (opt) Latitude of the pin
			lon (str): (opt) Longitude of the pin
			radius (str): (opt) radius in miles
			page (int): (opt) Page number
			per_page (str): (opt) Number of Nodes per page
		Returns:
			dict: dictionary containing closest atms
		'''
		path = paths['nodes'] + paths['atms']
		response = self.http.get(
			path,
			zip=zip,
			lat=lat,
			lon=lon,
			radius=rad,
			page=page,
			per_page=per_page
		)
		return response

	def issue_public_key(self, scope):
		'''Issues a public key for use with a UIaaS product
		Args:
			scope (list of str): Scopes that you wish to issue the public keys for
		Returns:
			dict: dictionary containing public key info 
		'''
		self.logger.debug("issuing a public key")
		
		path = paths['client']

		response = self.http.get(
			path, issue_public_key='YES', scope=scope
		)
		return response['public_key_obj']

	def get_all_users(self, query=None, page=None, per_page=None, show_refresh_tokens=None):
		"""Returns all user objects in a list
		Args:
			query (string): (opt) Name/Email of the user that you wish to search
			page (int): (opt) Page number
			per_page (int): (opt) How many users do you want us to return per page.
			show_refresh_tokens (bool): (opt) [yes/no] When dehydrating if the user object should have refresh tokens or not.
		Returns:
			(Users): object containing pagination info and list of User objects
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
		'''Gets all client transactions
		Args:
			page (int): (opt) Page number
			per_page (int): (opt) How many trans do you want us to return per page.
		Returns:
			(Transactions): object containing pagination info and list of Transaction objects
		'''
		self.logger.debug("getting all transactions")
		
		path = paths['trans']
		response = self.http.get(
			path, page=page, per_page=per_page
		)
		return Transactions(response)

	def get_all_nodes(self, page=None, per_page=None, type=None):
		'''Gets all client nodes
		Args:
			page (int): (opt) Page number
			per_page (int): (opt) How many nodes do you want us to return per page.
			type (bool): (opt) Type of nodes you wish to see. (NOTE: deprecated in v3.2)
		Returns:
			(Nodes): object containing pagination info and list of Node objects
		'''
		self.logger.debug("getting all nodes")
		
		path = paths['nodes']
		response = self.http.get(
			path, page=page, per_page=per_page, type=type
		)
		return Nodes(response)

	def get_all_subs(self, page=None, per_page=None):
		'''Gets all client webhooks
		Args:
			page (int): (opt) Page number
			per_page (int): (opt) How many subs do you want us to return per page.
		Returns:
			(Subscriptions): object containing pagination info and list of Subscription objects
		'''
		self.logger.debug("getting all subscriptions")
		
		path = paths['subs']
		response = self.http.get(
			path, page=page, per_page=per_page
		)
		return Subscriptions(response)

	def get_all_inst(self):
		'''Gets all institutions
		Returns:
			dict: dictionary containing institutions
		'''
		self.logger.debug("getting all institutions")
		
		path = paths['inst']
		response = self.http.get(path)
		return response

