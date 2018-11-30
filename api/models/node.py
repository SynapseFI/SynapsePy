from .transaction import Trans

from .endpoints import paths

class Node():

	def __init__(self, response, user, http, full_dehydrate=False):
		self.id = response['_id']
		self.user_id = response['user_id']
		self.type = response['type']
		self.user = user
		self.full_dehydrate = full_dehydrate
		self.response = response
		self.http = http

	def do_request(self, req_func, path, body={}, **params):
		'''
		'''
		if not self.user:
			self.user = self.http.get(paths['users'] + '/' + self.user_id)
		return self.user.do_request(req_func, path, body=body, **params)
		

	def create_trans(self, body):
		'''
		'''
		path = paths['users'] +'/'+ self.user_id + paths['nodes'] +'/'+ self.id + paths['trans']
		response = self.do_request(self.http.post, path, body)
		return Trans(response, self.http)

	def get_trans(self, trans_id):
		'''
		'''
		path = paths['users'] +'/'+ self.user_id + paths['nodes'] +'/'+ self.id + paths['trans'] + trans_id
		response = self.do_request(self.http.get, path)
		return Trans(response, self.user, self.http)

	def dummy_tran(self, is_credit=False):
		'''
		'''
		credit = 'YES' if is_credit else 'NO'
		path = paths['users'] +'/'+ self.user_id + paths['nodes'] +'/'+ self.id + paths['dummy']
		return self.do_request(self.http.get, path, is_credit=credit)

	def ship_debit(self, body):
		'''
		'''
		path = paths['users'] +'/'+ self.user_id + paths['nodes'] +'/'+ self.id
		return self.do_request(self.http.patch, path, body, ship='YES')

	def reset_debit(self):
		'''
		'''
		path = paths['/users'] +'/'+ self.user_id + paths['/nodes'] +'/'+ self.id
		return self.do_request(self.http.patch, path, {}, reset='YES')