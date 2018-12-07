
class Subscription():

	def __init__(self, response):
		self.id = response['_id']
		self.url = response['url']
		self.body = response