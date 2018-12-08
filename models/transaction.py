
class Trans():

	def __init__(self, response):
		self.id = response['_id']
		self.body = response