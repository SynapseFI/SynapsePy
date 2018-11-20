from .subscription import Subscription

class Subscriptions():

	def __init__(self, response):

		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']

		self.list_of_subs = [ Subscription(sub_r) for sub_r in response['subscriptions']]