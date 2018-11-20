from .node import Node

class Nodes():

	def __init__(self, response):

		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.node_count = response['node_count']

		self.list_of_nodes = [Node(node_r) for node_r in response['nodes']]