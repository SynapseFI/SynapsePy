
class Subscription():

	def __init__(self, response):
		self.id = response['_id']
		self.url = response['url']
		self.body = response

class Subscriptions():

	def __init__(self, response):
		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.subscriptions_count = response['subscriptions_count']
		self.list_of_subs = [ Subscription(sub_r) for sub_r in response['subscriptions']]