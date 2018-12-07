from unittest import TestCase, mock
from .fixtures.user_fixtures import *

from models.user import User

@mock.patch('User.do_request')
class UserTests(TestCase):

	def setUp(self):
		pass

	def test_oauth(self, mock_request):
		pass

	def test_update_info(self, mock_request):
		pass

	def test_create_node(self, mock_request):
		pass

	def test_get_node(self, mock_request):
		pass

	def test_update_node(self, mock_request):
		pass

	def test_ach_mfa(self, mock_request):
		pass

	def test_verify_micro(self, mock_request):
		pass

	def test_reinit_micro(self, mock_request):
		pass

	def test_ship_debit(self, mock_request):
		pass

	def test_reset_debit(self, mock_request):
		pass

	def test_generate_apple_pay(self, mock_request):
		pass

	def test_dummy_tran(self, mock_request):
		pass

	def test_delete_node(self, mock_request):
		pass

	def test_create_trans(self, mock_request):
		pass

	def test_get_trans(self, mock_request):
		pass

	def test_comment_trans(self, mock_request):
		pass

	def test_cancel_trans(self, mock_request):
		pass

	def test_create_subnet(self, mock_request):
		pass

	def test_get_subnet(self, mock_request):
		pass

	def test_get_all_nodes(self, mock_request):
		pass

	def test_get_all_node_trans(self, mock_request):
		pass

	def test_get_all_trans(self, mock_request):
		pass

	def test_get_all_subnets(self, mock_request):
		pass

if __name__ == '__main__':
	unittest.main()