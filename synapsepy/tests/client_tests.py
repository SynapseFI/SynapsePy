import unittest
from unittest import TestCase, mock

from .. import errors as api_errors

from .fixtures.user_fixtures import simple_response, users_resp
from .fixtures.subscription_fixtures import subs_resp, subss_resp
from .fixtures.node_fixtures import get_nodes_response
from .fixtures.client_fixtures import verified_routing_number, verified_address

from ..client import Client
from ..user import User, Users
from ..node import Node, Nodes
from ..transaction import Trans, Transactions
from ..subscription import Subscription, Subscriptions

class ClientTests(TestCase):
	'''
	TODO: need to add path/endpoint tests
	test all client methods
	'''

	def setUp(self):
		self.client = Client(
			client_id='',
			client_secret='',
			fingerprint='',
			ip_address='',
			devmode=True,
			logging=False )

	def test_client_init(self):
		# check if obj is Client
		self.assertIsInstance(self.client, Client)

	@mock.patch(
		'synapsepy.http_client.HttpClient.post',
		return_value = simple_response,
		autospec = True
	)
	def test_create_user(self, mock_request):
		# check if obj is User
		simple = self.client.create_user({},'CREATE_USER_IP',fingerprint='CREATE_USER_FP')
		self.assertIsInstance(simple, User)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = simple_response,
		autospec = True
	)
	def test_get_user(self, mock_request):
		# check if obj is User
		simple = self.client.get_user('', ip='GET_USER_IP', fingerprint='GET_USER_FP')
		self.assertIsInstance(simple, User)

	@mock.patch(
		'synapsepy.http_client.HttpClient.post',
		return_value = subs_resp,
		autospec = True
	)
	def test_create_subs(self, mock_request):
		# check if obj is Subscription
		sub = self.client.create_subscription('', '')
		self.assertIsInstance(sub, Subscription)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = subs_resp,
		autospec = True
	)
	def test_get_subs(self, mock_request):
		subs = self.client.get_subscription('')
		self.assertIsInstance(subs, Subscription)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_webhook_logs(self, mock_request):
		logs = self.client.webhook_logs()
		self.assertIsInstance(logs, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_crypto_quotes(self, mock_request):
		response = self.client.crypto_quotes()
		self.assertIsInstance(response, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_crypto_market_data(self, mock_request):
		response = self.client.crypto_market_data()
		self.assertIsInstance(response, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_trade_market_data(self, mock_request):
		response = self.client.trade_market_data('')
		self.assertIsInstance(response, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_locate_atms(self, mock_request):
		response = self.client.locate_atms()
		self.assertIsInstance(response, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {'public_key_obj':{}},
		autospec = True
	)
	def test_issue_pub_key(self, mock_request):
		# check if obj is dict
		key = self.client.issue_public_key([])
		self.assertIsInstance(key, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = users_resp,
		autospec = True
	)
	def test_get_users(self, mock_request):
		# check if obj is Users
		users = self.client.get_all_users()
		self.assertIsInstance(users, Users)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = subss_resp,
		autospec = True
	)
	def test_get_subss(self, mock_request):
		# check if obj is Subscriptions
		subss = self.client.get_all_subs()
		self.assertIsInstance(subss, Subscriptions)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = get_nodes_response,
		autospec = True
	)
	def test_get_nodes(self, mock_request):
		# check if obj is Nodes
		nodes = self.client.get_all_nodes()
		self.assertIsInstance(nodes, Nodes)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_get_inst(self, mock_request):
		# check if obj is JSON
		inst = self.client.get_all_inst()
		self.assertIsInstance(inst, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_get_node_types(self, mock_request):
		# check if obj is JSON
		node_types = self.client.get_node_types()
		self.assertIsInstance(node_types, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_get_user_document_types(self, mock_request):
		# check if obj is JSON
		user_document_types = self.client.get_user_document_types()
		self.assertIsInstance(user_document_types, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_get_user_entity_types(self, mock_request):
		# check if obj is JSON
		user_entity_types = self.client.get_user_entity_types()
		self.assertIsInstance(user_entity_types, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_get_user_entity_scopes(self, mock_request):
		# check if obj is JSON
		user_entity_scopes = self.client.get_user_entity_scopes()
		self.assertIsInstance(user_entity_scopes, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.post',
		return_value = verified_routing_number,
		autospec = True
	)
	def test_verify_routing_number(self, mock_request):
		# check if obj is dictionary
		routing_num = self.client.verify_routing_number({ 
			"type": 'ACH-US', 
			"routing_num": "084008426"
		})
		self.assertIsInstance(routing_num, dict)

	@mock.patch(
		'synapsepy.http_client.HttpClient.post',
		return_value = verified_address,
		autospec = True
	)
	def test_verify_address(self, mock_request):
		# check if obj is dictionary
		address = self.client.verify_address({
			"address_street": "1 Market St. STE 500",
			"address_city": "San Francisco",
			"address_subdivision": "CA",
			"address_postal_code": "94105",
			"address_country_code": "US"
		})
		self.assertIsInstance(address, dict)


	@mock.patch(
		'synapsepy.http_client.HttpClient.patch',
		return_value = {},
		autospec = True
	)
	def test_dispute_chargeback(self, mock_request):
		chargeback = self.client.dispute_chargeback('', {})
		self.assertIsInstance(chargeback, dict)

if __name__ == '__main__':
	unittest.main()