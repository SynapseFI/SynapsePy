from .user import User

class Users():

	def __init__(self, response, http):
		'''
		'''
		self.page = response['page']
		self.page_count = response['page_count']
		self.limit = response['limit']
		self.users_count = response['users_count']
		self.list_of_users = [ User(user_r, http) for user_r in response['users'] ]