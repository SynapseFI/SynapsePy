

class Trans():

	def __init__(self, response):
		self.trans_id = response['_id']
		self.node_id = response['from']['id']
		self.user_id = response['from']['user']['_id']
		self.payload = response
		self.http = http