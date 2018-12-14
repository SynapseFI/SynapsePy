
class Subnet():

	def __init__(self, response):
		self.id = response['_id']
		self.user_id = response['user_id']
		self.node_id = response['node_id']
		self.body = response

class Subnets():

	def __init__(self, response):
		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.subnets_count = response['subnets_count']
		self.list_of_subnets = [Subnet(sub_r) for sub_r in response['subnets']]