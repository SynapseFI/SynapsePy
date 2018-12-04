
from .transaction import Trans

class Transactions():

	def __init__(self, response, http):

		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.trans_count = response['trans_count']

		self.list_of_trans = [ Trans(trans_r, None, http) for trans_r in response['trans'] ]