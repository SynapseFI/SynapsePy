

class Trans():

	def __init__(self, response, user, http):
		self.id = response['_id']
		self.node_id = response['from']['id']
		self.user_id = response['from']['user']['_id']
		self.payload = response
		self.user = user
		self.http = http

	def do_request(self, req_func, path, body={}, **params):
		'''
		'''
		if not self.user:
			self.user = self.http.get(paths['users'] + '/' + self.user_id)
		return self.user.do_request(req_func, path, body=body, **params)

	def comment_status(self, body):
		'''
		'''
		path = (paths['users'] +'/'+ self.user_id + 
			paths['nodes'] +'/'+ self.node_id + 
			paths['trans'] + '/' + self.id)

		return self.do_request(self.http.patch, path, body)

	def cancel(self):
		'''
		'''
		path = (paths['users'] +'/'+ self.user_id + 
			paths['nodes'] +'/'+ self.node_id + 
			paths['trans'] + '/' + self.id)

		return self.do_request(self.http.delete, path)