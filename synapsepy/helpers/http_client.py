import json
import logging
import requests
import http.client as http_client
from . import errors as api_errors

class HttpClient():
	"""Handles HTTP requests (including headers) and API errors.
	"""
	def __init__(self, client_id, client_secret, fingerprint, ip_address, base_url, logging):
		self.client_id = client_id
		self.client_secret = client_secret
		self.fingerprint = fingerprint
		self.ip_address = ip_address
		self.base_url = base_url
		self.oauth_key = ''
		self.idempotency_key = None
		self.session = requests.Session()
		self.logger = self.get_log(logging)

		self.update_headers()

	def update_headers(self, **kwargs):
		"""Update the supplied properties on self and in the header dictionary.
		"""
		self.logger.debug("updating headers")

		for header in kwargs.keys():
			if kwargs.get(header) is not None:
				setattr(self, header, kwargs.get(header))

		self.session.headers.update(
			{
				'Content-Type': 'application/json',
				'X-SP-LANG': 'en',
				'X-SP-GATEWAY': self.client_id + '|' + self.client_secret,
				'X-SP-USER': self.oauth_key + '|' + self.fingerprint,
				'X-SP-USER-IP': self.ip_address
			}
		)

		self.logger.debug(json.dumps(self.session.headers.__dict__, indent=2))

		if self.idempotency_key:
			self.session.headers['X-SP-IDEMPOTENCY-KEY'] = self.idempotency_key

		return self.session.headers

	def get_headers(self):
		self.logger.debug("getting headers")
		return self.session.headers

	def get(self, path, **params):
		"""Send a GET request to the API."""

		url = self.base_url + path
		self.logger.debug("GET {}".format(url))

		valid_params = [
			'query',
			'page',
			'per_page',
			'type',
			'is_credit',
			'issue_public_key',
			'show_refresh_tokens',
			'subnet_id',
			'subnetid',
			'foreign_transaction',
			'full_dehydrate',
			'force_refresh',
			'limit',
			'ticker',
			'currency',
			'radius',
			'scope',
			'lat',
			'lon',
			'zip',
			'filter',
			'user_id'
		]

		parameters = {}

		for param in valid_params:
			if params.get(param) is not None:
				parameters[param] = params[param]

		response = self.session.get(url, params=parameters)

		return self.parse_response(response)

	def post(self, path, payload, **kwargs):
		"""Send a POST request to the API."""

		url = self.base_url + path

		self.logger.debug("POST {}".format(url))

		data = json.dumps(payload)

		if kwargs.get('idempotency_key') is not None:
			self.update_headers(idempotency_key=kwargs['idempotency_key'])

		response = self.session.post(url, data=data)
		return self.parse_response(response)

	def patch(self, path, payload, **params):
		"""Send a PATCH request to the API."""

		url = self.base_url + path
		self.logger.debug("PATCH {}".format(url))

		parameters = {}

		valid_params = [
			'resend_micro',
			'ship',
			'reset'
		]

		for param in valid_params:
			if params.get(param) is not None:
				parameters[param] = params[param]

		self.logger.debug("Params {}".format(parameters))
		data = json.dumps(payload)
		response = self.session.patch(url, data=data, params=parameters)

		return self.parse_response(response)

	def delete(self, path):
		"""Send a DELETE request to the API."""

		url = self.base_url + path
		self.logger.debug("PATCH {}".format(url))

		response = self.session.delete(url)
		return self.parse_response(response)

	def parse_response(self, response):
		"""Convert successful response to dict or raise error."""
		try:
			payload = response.json()
		except Exception as e:
			raise api_errors.GatewayTimeout(message="Request returned a non-JSON response due to a network timeout.", http_code=504, error_code="504", response=False)

		try:
			response.raise_for_status()

		except requests.exceptions.RequestException as e:
			raise api_errors.ErrorFactory.from_response(payload) from e

		if payload.get('error') and int(payload.get('error_code', 0)) == 10: # checks for unregistered fingerprint
			raise api_errors.ErrorFactory.from_response(payload)

		return response.json()

	def get_log(self, enable, debuglevel=1):
		"""Log requests to stdout."""
		# http_client.HTTPConnection.debuglevel = 1 if enable else 0

		logging.basicConfig()

		logger = logging.getLogger(__name__)
		logger.setLevel(logging.DEBUG)
		logger.disabled = not enable

		return logger
