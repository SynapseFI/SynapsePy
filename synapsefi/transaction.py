
class Trans():

	def __init__(self, response):
		self.id = response['_id']
		self.body = response

class Transactions():

	def __init__(self, response):
		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.trans_count = response['trans_count']
		self.list_of_trans = [ Trans(trans_r) for trans_r in response['trans'] ]