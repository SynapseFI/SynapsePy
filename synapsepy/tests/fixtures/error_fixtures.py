from unittest.mock import Mock
from requests.models import Response
from requests.exceptions import HTTPError

act_pend = Mock(spec=Response)
act_pend.raise_for_status.side_effect = HTTPError
act_pend.status_code = 202
act_pend.json.return_value = { 
	"error": {
		"en": "Action Pending"
		},
	"error_code": "10",
	"http_code": "202",
	"success": False
	}

inc_cli_cred = Mock(spec=Response)
inc_cli_cred.raise_for_status.side_effect = HTTPError
inc_cli_cred.status_code = 400
inc_cli_cred.json.return_value = { 
	"error": {
		"en": "Incorrect Client Credentials"
		},
	"error_code": "100",
	"http_code": "400",
	"success": False
	}

inc_user_cred = Mock(spec=Response)
inc_user_cred.raise_for_status.side_effect = HTTPError
inc_user_cred.status_code = 400
inc_user_cred.json.return_value = { 
	"error": {
		"en": "Incorrect User Credentials"
		},
	"error_code": "110",
	"http_code": "400",
	"success": False
	}

unauth_fing = Mock(spec=Response)
unauth_fing.raise_for_status.side_effect = HTTPError
unauth_fing.status_code = 400
unauth_fing.json.return_value = { 
	"error": {
		"en": "Unauthorized Fingerprint"
		},
	"error_code": "120",
	"http_code": "400",
	"success": False
	}

payload_err = Mock(spec=Response)
payload_err.raise_for_status.side_effect = HTTPError
payload_err.status_code = 400
payload_err.json.return_value = { 
	"error": {
		"en": "Payload Error"
		},
	"error_code": "200",
	"http_code": "400",
	"success": False
	}

unauth_act = Mock(spec=Response)
unauth_act.raise_for_status.side_effect = HTTPError
unauth_act.status_code = 400
unauth_act.json.return_value = { 
	"error": {
		"en": "Unauthorized Action"
		},
	"error_code": "300",
	"http_code": "400",
	"success": False
	}

inc_val = Mock(spec=Response)
inc_val.raise_for_status.side_effect = HTTPError
inc_val.status_code = 400
inc_val.json.return_value = { 
	"error": {
		"en": "Incorrect Values"
		},
	"error_code": "400",
	"http_code": "409",
	"success": False
	}

obj_not_found = Mock(spec=Response)
obj_not_found.raise_for_status.side_effect = HTTPError
obj_not_found.status_code = 404
obj_not_found.json.return_value = { 
	"error": {
		"en": "Object not found"
		},
	"error_code": "404",
	"http_code": "404",
	"success": False
	}

act_not_allow = Mock(spec=Response)
act_not_allow.raise_for_status.side_effect = HTTPError
act_not_allow.status_code = 400
act_not_allow.json.return_value = { 
	"error": {
		"en": "Action not allowed"
		},
	"error_code": "410",
	"http_code": "400",
	"success": False
	}

too_many_req = Mock(spec=Response)
too_many_req.raise_for_status.side_effect = HTTPError
too_many_req.status_code = 400
too_many_req.json.return_value = { 
	"error": {
		"en": "Too many requests"
		},
	"error_code": "429",
	"http_code": "400",
	"success": False
	}

idem_conf = Mock(spec=Response)
idem_conf.raise_for_status.side_effect = HTTPError
idem_conf.status_code = 400
idem_conf.json.return_value = { 
	"error": {
		"en": "Idempotency conflict"
		},
	"error_code": "450",
	"http_code": "400",
	"success": False
	}

req_fail = Mock(spec=Response)
req_fail.raise_for_status.side_effect = HTTPError
req_fail.status_code = 400
req_fail.json.return_value = { 
	"error": {
		"en": "Request failed"
		},
	"error_code": "460",
	"http_code": "400",
	"success": False
	}

serv_error = Mock(spec=Response)
serv_error.raise_for_status.side_effect = HTTPError
serv_error.status_code = 500
serv_error.json.return_value = { 
	"error": {
		"en": "Server Error"
		},
	"error_code": "500",
	"http_code": "500",
	"success": False
	}

serv_unav = Mock(spec=Response)
serv_unav.raise_for_status.side_effect = HTTPError
serv_unav.status_code = 503
serv_unav.json.return_value = { 
	"error": {
		"en": "Service Unavailable"
		},
	"error_code": "503",
	"http_code": "503",
	"success": False
	}
