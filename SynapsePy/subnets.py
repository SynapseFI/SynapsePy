from .subnet import Subnet

class Subnets():

	def __init__(self, response):
		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.subnets_count = response['subnets_count']