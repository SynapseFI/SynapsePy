

class Node():

	def __init__(self, response):
		self.node_id = response['_id']
		self.user_id = response['user_id']
		self.response = response
		self.http = http