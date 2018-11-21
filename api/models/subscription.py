
class Subscription():

	def __init__(self, response, http):
		self.id = response['_id']
		self.url = response['url']
		self.body = response
		self.http = http