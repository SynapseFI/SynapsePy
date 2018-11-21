import requests
import logging
import json
import http.client as http_client
from .errors import ErrorFactory

class HttpClient():
	"""Handles HTTP requests (including headers) and API errors.
	"""
	def __init__(self, **kwargs):
		self.logger = self.get_log(kwargs['logging'])

		self.update_headers(
			client_id=kwargs['client_id'],
			client_secret=kwargs['client_secret'],
			fingerprint=kwargs['fingerprint'],
			ip_address=kwargs['ip_address'],
			oauth_key=''
		)

		self.base_url= kwargs['base_url']

	def update_headers(self, **kwargs):
		"""Update the supplied properties on self and in the header dictionary.
		"""
		self.logger.debug("updating headers")

		header_options = ['client_id', 'client_secret', 'fingerprint',
						  'ip_address', 'oauth_key']

		for prop in header_options:
			if kwargs.get(prop) is not None:
				setattr(self, prop, kwargs.get(prop))

		self.headers = {
			'Content-Type': 'application/json',
			'X-SP-LANG': 'en',
			'X-SP-GATEWAY': self.client_id + '|' + self.client_secret,
			'X-SP-USER': self.oauth_key + '|' + self.fingerprint,
			'X-SP-USER-IP': self.ip_address
		}

		self.session = requests.Session()
		self.session.headers.update(self.headers)
		return self.session.headers

	def get_headers(self):
		self.logger.debug("getting headers")
		return self.session.headers

	def get(self, path, **params):
		"""Send a GET request to the API."""

		url = self.base_url + path
		self.logger.debug("GET {}".format(url))

		valid_params = [
			'query', 'page', 'per_page', 'type', 'issue_public_key',
			'show_refresh_tokens','full_dehydrate',
			'radius', 'scope', 'lat', 'lon', 'zip'
			]
		parameters = {}

		for param in valid_params:
			if params.get(param) is not None:
				parameters[param] = params[param]
				if param == 'full_dehydrate':
					parameters[param] = 'yes' if params[param] else 'no'

		response = self.session.get(url, params=parameters)

		return self.parse_response(response)

	def post(self, path, payload, **kwargs):
		"""Send a POST request to the API."""

		url = self.base_url + path

		self.logger.debug("POST {}".format(url))

		headers = self.get_headers()
		if kwargs.get('idempotency_key'):
			headers['X-SP-IDEMPOTENCY-KEY'] = kwargs['idempotency_key']
		data = json.dumps(payload)

		response = self.session.post(url, data=data)

		return self.parse_response(response)

	def patch(self, path, payload):
		"""Send a PATCH request to the API."""

		url = self.base_url + path
		self.logger.debug("PATCH {}".format(url))

		data = json.dumps(payload)
		response = self.session.patch(url, data=data)

		return self.parse_response(response)

	def delete(self, path):
		"""Send a DELETE request to the API."""

		url = self.base_url + path
		self.logger.debug("PATCH {}".format(url))

		response = self.session.delete(url)
		return self.parse_response(response)

	def parse_response(self, response):
		"""Convert successful response to dict or raise error."""
		
		payload = response.json()

		if int(payload.get('error_code', 0)) > 0:
			raise ErrorFactory.from_response(payload)
		else:
			response.raise_for_status
			return response.json()

	def get_log(self, enable, debuglevel=1):
		"""Log requests to stdout."""
		# http_client.HTTPConnection.debuglevel = 1 if enable else 0

		logging.basicConfig()

		logger = logging.getLogger("__name__")
		logger.setLevel(logging.DEBUG)
		logger.disabled = not enable

		return logger
