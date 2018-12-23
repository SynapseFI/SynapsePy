import unittest
import synapsefi.models.errors as api_errors

from unittest import TestCase, mock

from .fixtures.user_fixtures import simple_response, users_resp
from .fixtures.client_fixtures import test_client
from .fixtures.subscription_fixtures import subs_resp, subss_resp
from .fixtures.node_fixtures import get_nodes_response

from synapsefi.models.client import Client
from synapsefi.models.user import User, Users
from synapsefi.models.node import Node, Nodes
from synapsefi.models.subscription import Subscription, Subscriptions

class ClientTests(TestCase):
	'''
	TODO: need to add path/endpoint tests
	test all client methods
	'''

	def setUp(self):
		self.client = test_client

	def test_client_init(self):
		# check if obj is Client
		self.assertIsInstance(self.client, Client)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.post',
		return_value = simple_response,
		autospec = True
	)
	def test_create_user(self, mock_request):
		# check if obj is User
		simple = self.client.create_user({})
		self.assertIsInstance(simple, User)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.post',
		return_value = subs_resp,
		autospec = True
	)
	def test_create_subs(self, mock_request):
		# check if obj is Subscription
		sub = self.client.create_subscription('', '')
		self.assertIsInstance(sub, Subscription)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = subs_resp,
		autospec = True
	)
	def test_get_subs(self, mock_request):
		subs = self.client.get_subscription('')
		self.assertIsInstance(subs, Subscription)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_crypto_quotes(self, mock_request):
		response = self.client.crypto_quotes()
		self.assertIsInstance(response, dict)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_crypto_market_data(self, mock_request):
		response = self.client.crypto_market_data()
		self.assertIsInstance(response, dict)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_locate_atms(self, mock_request):
		response = self.client.locate_atms()
		self.assertIsInstance(response, dict)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = {'public_key_obj':{}},
		autospec = True
	)
	def test_issue_pub_key(self, mock_request):
		# check if obj is dict
		key = self.client.issue_public_key([])
		self.assertIsInstance(key, dict)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = users_resp,
		autospec = True
	)
	def test_get_users(self, mock_request):
		# check if obj is Users
		users = self.client.get_all_users()
		self.assertIsInstance(users, Users)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = subss_resp,
		autospec = True
	)
	def test_get_subss(self, mock_request):
		# check if obj is Subscriptions
		subss = self.client.get_all_subs()
		self.assertIsInstance(subss, Subscriptions)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = get_nodes_response,
		autospec = True
	)
	def test_get_nodes(self, mock_request):
		# check if obj is Nodes
		nodes = self.client.get_all_nodes()
		self.assertIsInstance(nodes, Nodes)

	@mock.patch(
		'synapsefi.models.http_client.HttpClient.get',
		return_value = {},
		autospec = True
	)
	def test_get_inst(self, mock_request):
		# check if obj is JSON
		inst = self.client.get_all_inst()
		self.assertIsInstance(inst, dict)

if __name__ == '__main__':
	unittest.main()