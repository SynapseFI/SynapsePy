"""Custom errors for handling HTTP and API errors."""


class SynapseError(Exception):
	"""Custom class for handling HTTP and API errors."""
	def __init__(self, message, http_code, error_code, response):
		self.message = message
		self.http_code = http_code
		self.error_code = error_code
		self.response = response

		super(SynapseError, self).__init__(message)

	def __repr__(self):
		return '{0}(code={1},message={2})'.format(self.__class__, self.error_code, self.message)

class ActionPending(SynapseError):
	"""
	raised on ERROR_CODE 10
	Accepted, but action pending
	"""
	pass

class IncorrectClientCredentials(SynapseError):
	"""
	raised on ERROR_CODE 100
	Incorrect Client Credentials
	"""
	pass

class IncorrectUserCredentials(SynapseError):
	"""
	raised on ERROR_CODE 110
	Incorrect User Credentials
	"""
	pass

class UnauthorizedFingerprint(SynapseError):
	"""
	raised on ERROR_CODE 120
	Unauthorized Fingerprint
	"""
	pass

class PayloadError(SynapseError):
	"""
	raised on ERROR_CODE 200
	Error in Payload (Error in payload formatting)

	Supplied address is invalid / Unable to verify address
	"""
	pass

class UnauthorizedAction(SynapseError):
	"""
	raised on ERROR_CODE 300
	Unauthorized action (User/Client not allowed to perform this action)
	"""
	pass

class IncorrectValues(SynapseError):
	"""
	raised on ERROR_CODE 400
	Incorrect Values Supplied (eg. Insufficient balance, wrong MFA response, incorrect micro deposits)
	"""
	pass

class ObjectNotFound(SynapseError):
	"""
	raised on ERROR_CODE 404
	Object not found
	"""
	pass

class ActionNotAllowed(SynapseError):
	"""
	raised on ERROR_CODE 410
	Action Not Allowed on the object (either you do not have permissions or the action on this object is not supported)
	"""

class TooManyRequests(SynapseError):
	"""
	raised on ERROR_CODE 429
	Too many requests hit the API too quickly.
	"""
	pass

class IdempotencyConflict(SynapseError):
	"""
	raised on ERROR_CODE 450
	Idempotency key already in use
	"""
	pass

class RequestFailed(SynapseError):
	"""
	raised on ERROR_CODE 460
	Request Failed but not due to server error
	"""
	pass

class ServerError(SynapseError):
	"""
	raised on ERROR_CODE 500
	Server Error
	"""
	pass

class ServiceUnavailable(SynapseError):
	"""
	raised on ERROR_CODE 503
	Service Unavailable. The server is currently unable to handle the request due to a temporary overload or scheduled maintenance.
	"""
	pass

class GatewayTimeout(SynapseError):
	"""
	raised on ERROR_CODE 504
	Gateway Timeout. The request did not get a response in time from the server that it needed in order to complete the request.
	"""
	pass


class ErrorFactory():
	"""Determines which error to raise based on status code.
	"""

	ERRORS = {
		"10" : ActionPending,
		"100" : IncorrectClientCredentials,
		"110" : IncorrectUserCredentials,
		"120" : UnauthorizedFingerprint,
		"200" : PayloadError,
		"300" : UnauthorizedAction,
		"400" : IncorrectValues,
		"404" : ObjectNotFound,
		"410" : ActionNotAllowed,
		"429" : TooManyRequests,
		"450" : IdempotencyConflict,
		"460" : RequestFailed,
		"500" : ServerError,
		"503" : ServiceUnavailable,
		"504": GatewayTimeout
		}

	@classmethod
	def from_response(cls, response):
		"""Return the corresponding error from a response."""
		# import pdb; pdb.set_trace()

		# message = response.get('mfa', {}).get('message', response.get('message', response['error'])['en'])
		message = response.get('error', {}).get('en', "")
		http_code = response['http_code']
		error_code = response['error_code']

		klass = cls.ERRORS.get(error_code)
		return klass(message=message, http_code=http_code, error_code=error_code, response=response)

