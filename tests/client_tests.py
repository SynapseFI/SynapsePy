
import unittest
import models.errors as api_errors

from .fixtures.client_fixtures import *
from .fixtures.user_fixtures import *
from .fixtures.subscription_fixtures import *

from models.client import Client
from models.user import User, Users
from models.subscription import Subscription, Subscriptions
from models.node import Node, Nodes


class ClientTests(unittest.TestCase):

	def setUp(self):
		self.client = test_client

	def test_client_init(self):
		# check if obj is Client
		self.assertIsInstance(self.client, Client)

	def test_create_user(self):
		# check if obj is User
		simple = self.client.create_user(simple_user)
		basedocs = self.client.create_user(basedocs_user)
		self.assertIsInstance(simple, User)
		self.assertIsInstance(basedocs, User)

	def test_create_subs(self):
		# check if obj is Subscription
		sub = self.client.create_subscription(webhook_url, sub_scope)
		self.assertIsInstance(sub, Subscription)

	def test_get_subs(self):
		sub_id = self.client.create_subscription(webhook_url, sub_scope).id
		subs = self.client.get_subscription(sub_id)
		self.assertIsInstance(subs, Subscription)

	def test_crypto_quotes(self):
		pass

	def test_crypto_market_data(self):
		pass

	def test_locate_atms(self):
		pass

	def test_issue_pub_key(self):
		# check if obj is JSON
		pub_key_scope = ["OAUTH|POST"]
		key = self.client.issue_public_key(pub_key_scope)
		self.assertIsInstance(key, dict)

	def test_get_users(self):
		# check if obj is Users
		users = self.client.get_all_users()
		self.assertIsInstance(users, Users)

	def test_get_subss(self):
		# check if obj is Subscriptions
		subss = self.client.get_all_subs()
		self.assertIsInstance(subss, Subscriptions)

	def test_get_nodes(self):
		# check if obj is Nodes
		nodes = self.client.get_all_nodes()
		self.assertIsInstance(nodes, Nodes)

	def test_get_inst(self):
		# check if obj is JSON
		inst = self.client.get_all_inst()
		self.assertIsInstance(inst, dict)

if __name__ == '__main__':
	unittest.main()