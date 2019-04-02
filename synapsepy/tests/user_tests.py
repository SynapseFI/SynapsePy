import unittest
import warnings
from unittest import TestCase, mock

from .fixtures.user_fixtures import *
from .fixtures.node_fixtures import *
from .fixtures.trans_fixtures import *
from .fixtures.subnet_fixtures import *

from ..client import Client
from ..user import User
from ..node import Node, Nodes
from ..transaction import Trans, Transactions
from ..subnet import Subnet, Subnets

from ..http_client import HttpClient

@mock.patch(
	'synapsepy.user.User._do_request',
	return_value={},
	autospec=True
)
class UserTests(TestCase):
	'''
	TODO: need to add path/endpoint tests
	test all user methods
	'''

	def setUp(self):
		self.client = Client(
			client_id='',
			client_secret='',
			fingerprint='',
			ip_address='',
			devmode=True,
			logging=False )

		self.user = User(simple_response, self.client.http)

		self.card_us_id = card_us_get_response['_id']
		self.card_us_type = card_us_get_response['type']

		self.trans_id = trans_get_response['_id']

		self.ach_us_id = ach_us_get_response['_id']
		self.debit_us_id = debit_us_get_response['_id']

		self.subnet_id = subnet_get_resp['_id']

		self.nodes_page = get_nodes_response['page']
		self.nodes_page_count = get_nodes_response['page_count']
		self.nodes_limit = get_nodes_response['limit']
		self.nodes_node_count = get_nodes_response['node_count']

		self.node_trans_page = get_all_trans_resp['page']
		self.node_trans_page_count = get_all_trans_resp['page_count']
		self.node_trans_limit = get_all_trans_resp['limit']
		self.node_trans_count = get_all_trans_resp['trans_count']

	@mock.patch(
		'synapsepy.http_client.HttpClient.get',
		return_value={'refresh_token':'1234'},
		autospec=True
	)
	def test_refresh(self, mock_get, mock_request):
		self.assertEqual(
			self.user.refresh(),
			mock_get.return_value['refresh_token']
		)

	@mock.patch(
		'synapsepy.http_client.HttpClient.post',
		return_value={'oauth_key':'1234'},
		autospec=True
	)
	def test_oauth(self, mock_post, mock_request):
		self.assertEqual(
			self.user.oauth(), mock_post.return_value
		)

	def test_update_info(self, mock_request):
		self.assertIsInstance(
			self.user.update_info({}), dict
		)

	def test_create_node(self, mock_request):
		mock_request.return_value = get_nodes_response
		self.assertIsInstance(
			self.user.create_node(card_us_payload), Nodes
		)

		mock_request.return_value = ach_mfa_resp
		self.assertIsInstance(
			self.user.create_node(ach_us_logins),
			dict
		)

	def test_get_node(self, mock_request):
		mock_request.return_value = card_us_get_response

		test_node = self.user.get_node(self.card_us_id)
		self.assertIsInstance(test_node, Node)
		self.assertEqual(test_node.id, self.card_us_id)
		self.assertEqual(test_node.type, self.card_us_type)
		self.assertEqual(
			test_node.body, card_us_get_response
		)

	def test_get_node_statements(self, mock_request):
		statem = self.user.get_node_statements('')
		self.assertIsInstance(statem, dict)

	def test_update_node(self, mock_request):
		mock_request.return_value = card_us_up_response

		test_node = self.user.update_node(
			self.card_us_id, {}
		)
		self.assertIsInstance(test_node, Node)
		self.assertEqual(test_node.id, self.card_us_id)
		self.assertEqual(test_node.type, self.card_us_type)
		self.assertNotEqual(
			test_node.body, card_us_get_response
		)
		self.assertEqual(
			test_node.body, card_us_up_response
		)

	def test_ach_mfa(self, mock_request):
		mock_request.return_value = get_nodes_response
		self.assertIsInstance(self.user.ach_mfa({}), Nodes)

		mock_request.return_value = ach_mfa_resp
		self.assertIsInstance(
			self.user.ach_mfa({}),
			dict
		)

	def test_verify_micro(self, mock_request):
		mock_request.return_value = ach_us_get_response
		self.assertIsInstance(
			self.user.verify_micro(self.ach_us_id,{}),
			Node
		)

	def test_reinit_micro(self, mock_request):
		self.assertEqual(
			self.user.reinit_micro(self.ach_us_id),
			mock_request.return_value
		)

	def test_ship_card_node(self, mock_request):
		warnings.simplefilter("ignore")
		self.assertEqual(
			self.user.ship_card_node(self.card_us_id, {}),
			mock_request.return_value
		)

	def test_reset_card_node(self, mock_request):
		warnings.simplefilter("ignore")
		self.assertEqual(
			self.user.reset_card_node(self.debit_us_id),
			mock_request.return_value
		)

	def test_generate_apple_pay(self, mock_request):
		self.assertEqual(
			self.user.generate_apple_pay(
				self.card_us_id, {}
			),
			mock_request.return_value
		)

	def test_dummy_tran(self, mock_request):
		self.assertEqual(
			self.user.dummy_tran(self.card_us_id),
			mock_request.return_value
		)

	def test_delete_node(self, mock_request):
		self.assertEqual(
			self.user.delete_node(self.card_us_id),
			mock_request.return_value
		)

	def test_create_trans(self, mock_request):
		mock_request.return_value = trans_get_response

		test_trans = self.user.create_trans(
			self.card_us_id, {}
		)
		self.assertIsInstance(test_trans, Trans)
		self.assertEqual(test_trans.id, self.trans_id)
		self.assertEqual(
			test_trans.body, trans_get_response
		)

	def test_get_trans(self, mock_request):
		mock_request.return_value = trans_get_response

		test_trans = self.user.get_trans(
			self.card_us_id, self.trans_id
		)
		self.assertIsInstance(test_trans, Trans)
		self.assertEqual(test_trans.id, self.trans_id)
		self.assertEqual(
			test_trans.body, trans_get_response
		)

	def test_comment_trans(self, mock_request):
		self.assertEqual(
			self.user.comment_trans(
				self.card_us_id, self.trans_id, ''
			),
			mock_request.return_value
		)

	def test_cancel_trans(self, mock_request):
		self.assertEqual(
			self.user.cancel_trans(
				self.card_us_id, self.trans_id
			),
			mock_request.return_value
		)

	def test_create_subnet(self, mock_request):
		mock_request.return_value = subnet_get_resp

		test_subnet = self.user.create_subnet(
			'', {}
		)
		self.assertIsInstance(test_subnet, Subnet)

	def test_get_subnet(self, mock_request):
		mock_request.return_value = subnet_get_resp

		test_subnet = self.user.get_subnet('', '')
		self.assertIsInstance(test_subnet, Subnet)

	def test_update_subnet(self, mock_request):
		mock_request.return_value = subnet_get_resp

		test_subnet = self.user.update_subnet('','',{})
		self.assertIsInstance(test_subnet, Subnet)

	def test_ship_card(self, mock_request):
		test_response = self.user.ship_card('','',{})
		self.assertEqual(test_response, {})

	def test_get_all_nodes(self, mock_request):
		mock_request.return_value = get_nodes_response

		test_nodes = self.user.get_all_nodes()
		self.assertIsInstance(test_nodes, Nodes)
		self.assertEqual(test_nodes.page, self.nodes_page)
		self.assertEqual(
			test_nodes.page_count, self.nodes_page_count
		)
		self.assertEqual(test_nodes.limit, self.nodes_limit)
		self.assertEqual(
			test_nodes.node_count, self.nodes_node_count
		)

		for node in test_nodes.list_of_nodes:
			self.assertIsInstance(node, Node)

	def test_get_all_node_trans(self, mock_request):
		mock_request.return_value = get_all_trans_resp

		test_node_trans = self.user.get_all_node_trans('')
		self.assertIsInstance(test_node_trans, Transactions)
		self.assertEqual(
			test_node_trans.page,
			self.node_trans_page
		)
		self.assertEqual(
			test_node_trans.page_count,
			self.node_trans_page_count
		)
		self.assertEqual(
			test_node_trans.limit, self.node_trans_limit
		)
		self.assertEqual(
			test_node_trans.trans_count,
			self.node_trans_count
		)

		for trans in test_node_trans.list_of_trans:
			self.assertIsInstance(trans, Trans)

	def test_get_all_trans(self, mock_request):
		mock_request.return_value = get_all_trans_resp

		test_node_trans = self.user.get_all_trans()
		self.assertIsInstance(test_node_trans, Transactions)

	def test_get_all_subnets(self, mock_request):
		mock_request.return_value = subnet_get_all_resp

		test_get_all_subn = self.user.get_all_subnets('')
		self.assertIsInstance(test_get_all_subn, Subnets)

	def test_get_statements(self, mock_request):
		statem = self.user.get_statements()
		self.assertIsInstance(statem, dict)

if __name__ == '__main__':
	unittest.main()
