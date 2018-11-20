from .user import User

class Users():

	def __init__(self, http, response):

		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.list_of_users = [ User(user_r, http, full_dehydrate='no') for user_r in response['users'] ]
		
		self.http = http