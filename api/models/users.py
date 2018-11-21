from .user import User

class Users():

	def __init__(self, http, response):

		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.http = http
		self.list_of_users = [ User(user_r, http) for user_r in response['users'] ]