
class Subnet():

	def __init__(self, response):
		self.id = response['_id']
		self.user_id = response['user_id']
		self.node_id = response['node_id']
		self.body = response