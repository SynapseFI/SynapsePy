

class Node():

	def __init__(self, response, http, full_dehydrate=False):
		self.node_id = response['_id']
		self.user_id = response['user_id']
		self.full_dehydrate = full_dehydrate
		self.response = response
		self.http = http