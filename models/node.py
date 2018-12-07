
class Node():

	def __init__(self, response, full_dehydrate=False):
		self.id = response['_id']
		self.type = response['type']
		self.full_dehydrate = full_dehydrate
		self.response = response