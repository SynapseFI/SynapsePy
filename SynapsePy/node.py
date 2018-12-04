from .endpoints import paths

class Node():

	def __init__(self, response, full_dehydrate=False):
		self.id = response['_id']
		self.user_id = response['user_id']
		self.type = response['type']
		self.full_dehydrate = full_dehydrate
		self.response = response