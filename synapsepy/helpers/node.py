
class Node():

	def __init__(self, response, full_dehydrate=False):
		self.id = response['_id']
		self.type = response['type']
		self.full_dehydrate = full_dehydrate
		self.body = response

class Nodes():

	def __init__(self, response):
		self.page = response.get('page', 1)
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.node_count = response['node_count']
		self.list_of_nodes = [
			Node(node_r)
			for node_r in response['nodes']
		]