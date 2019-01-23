
import unittest
import synapsepy.errors as api_errors

from .fixtures.error_fixtures import *
from .fixtures.client_fixtures import *

class ErrorTests(unittest.TestCase):
	
	def setUp(self):
		self.http = test_client.http

	def test_act_pend(self):
		self.assertRaises(api_errors.ActionPending, self.http.parse_response, act_pend)

	def test_inc_cli_cred(self):
		self.assertRaises(api_errors.IncorrectClientCredentials, self.http.parse_response, inc_cli_cred)

	def test_inc_user_cred(self):
		self.assertRaises(api_errors.IncorrectUserCredentials, self.http.parse_response, inc_user_cred)

	def test_unauth_fing(self):
		self.assertRaises(api_errors.UnauthorizedFingerprint, self.http.parse_response, unauth_fing)

	def test_payload_err(self):
		self.assertRaises(api_errors.PayloadError, self.http.parse_response, payload_err)

	def test_unauth_act(self):
		self.assertRaises(api_errors.UnauthorizedAction, self.http.parse_response, unauth_act)
	
	def test_inc_val(self):
		self.assertRaises(api_errors.IncorrectValues, self.http.parse_response, inc_val)
	
	def test_obj_not_found(self):
		self.assertRaises(api_errors.ObjectNotFound, self.http.parse_response, obj_not_found)
	
	def test_act_not_allow(self):
		self.assertRaises(api_errors.ActionNotAllowed, self.http.parse_response, act_not_allow)
	
	def test_too_many_req(self):
		self.assertRaises(api_errors.TooManyRequests, self.http.parse_response, too_many_req)
	
	def test_idem_conf(self):
		self.assertRaises(api_errors.IdempotencyConflict, self.http.parse_response, idem_conf)
	
	def test_req_fail(self):
		self.assertRaises(api_errors.RequestFailed, self.http.parse_response, req_fail)

	def test_serv_error(self):
		self.assertRaises(api_errors.ServerError, self.http.parse_response, serv_error)
	
	def test_serv_unav(self):
		self.assertRaises(api_errors.ServiceUnavailable, self.http.parse_response, serv_unav)
	


if __name__ == '__main__':
	unittest.main()