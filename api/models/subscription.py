
class Subscription():

	def __init__(self, response, http):
		self.id = response['_id']
		self.url = response['url']
		self.body = response
		self.http = http

	def update_subscription(self, sub_id, body):
		'''
		Args:
			sub_id (str): subscription id
			body (JSON): update body
		Returns:
			(Subscription): object containing subscription record
		'''
		# self.logger.debug("updating subscription")

		url = self.paths['subs'] + '/' + sub_id
		response = self.http.patch(url, body)
		return Subscription(response, self.http)