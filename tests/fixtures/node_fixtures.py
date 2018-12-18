
card_us_payload = {
  "type": "CARD-US",
  "info": {
	"nickname":"My Debit Card",
	"document_id":"2a4a5957a3a62aaac1a0dd0edcae96ea2cdee688ec6337b20745eed8869e3ac8"
  }
}

card_us_get_response = {
	"_id": "5c0af4e64f98b000bc81c6fd",
	"_links": {
		"self": {
			"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0af4e64f98b000bc81c6fd"
		}
	},
	"allowed": "INACTIVE",
	"client": {
		"id": "5be38afd6a785e6bddfffe68",
		"name": "test user"
	},
	"extra": {
		"note": None,
		"other": {
			"access_token": "5c0af4eac3c43d7a63b1bc77"
		},
		"supp_id": ""
	},
	"info": {
		"balance": {
			"amount": 0,
			"currency": "USD"
		},
		"card_hash": "0ce83962ea95688a3801c302b31c18cbd71d992ab050b6f32468fc280b31ce31",
		"card_number": "6340",
		"card_style_id": None,
		"document_id": "2a4a5957a3a62aaac1a0dd0edcae96ea2cdee688ec6337b20745eed8869e3ac8",
		"name_on_account": " ",
		"nickname": "My Debit Card",
		"preferences": {
			"allow_foreign_transactions": False,
			"atm_withdrawal_limit": 100,
			"pos_withdrawal_limit": 1000
		}
	},
	"is_active": True,
	"timeline": [
		{
			"date": 1544221925385,
			"note": "Node created."
		},
		{
			"date": 1544221937791,
			"note": "Card Created."
		}
	],
	"type": "CARD-US",
	"user_id": "5c0abeb9970f8426abc8df67"
}

card_us_up_response = {
	"_id": "5c0af4e64f98b000bc81c6fd",
	"_links": {
		"self": {
			"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0af4e64f98b000bc81c6fd"
		}
	},
	"allowed": "CREDIT-AND-DEBIT",
	"client": {
		"id": "5be38afd6a785e6bddfffe68",
		"name": "test user"
	},
	"extra": {
		"note": None,
		"other": {
			"access_token": "5c0af4eac3c43d7a63b1bc77"
		},
		"supp_id": ""
	},
	"info": {
		"balance": {
			"amount": 0,
			"currency": "USD"
		},
		"card_hash": "0ce83962ea95688a3801c302b31c18cbd71d992ab050b6f32468fc280b31ce31",
		"card_number": "6340",
		"card_style_id": None,
		"document_id": "2a4a5957a3a62aaac1a0dd0edcae96ea2cdee688ec6337b20745eed8869e3ac8",
		"name_on_account": " ",
		"nickname": "My Debit Card",
		"preferences": {
			"allow_foreign_transactions": False,
			"atm_withdrawal_limit": 100,
			"pos_withdrawal_limit": 1000
		}
	},
	"is_active": True,
	"timeline": [
		{
			"date": 1544221925385,
			"note": "Node created."
		},
		{
			"date": 1544221937791,
			"note": "Card Created."
		}
	],
	"type": "CARD-US",
	"user_id": "5c0abeb9970f8426abc8df67"
}

get_nodes_response = {
	"error_code": "0",
	"http_code": "200",
	"limit": 20,
	"node_count": 3,
	"nodes": [
		{
			"_id": "5c0b0ff74f98b000bd81f4af",
			"_links": {
				"self": {
					"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0b0ff74f98b000bd81f4af"
				}
			},
			"allowed": "CREDIT-AND-DEBIT",
			"client": {
				"id": "5be38afd6a785e6bddfffe68",
				"name": "test user"
			},
			"extra": {
				"note": None,
				"other": {},
				"supp_id": ""
			},
			"info": {
				"balance": {
					"amount": 0,
					"currency": "USD"
				},
				"document_id": None,
				"name_on_account": " ",
				"nickname": "My Deposit Account"
			},
			"is_active": True,
			"timeline": [
				{
					"date": 1544228854825,
					"note": "Node created."
				}
			],
			"type": "DEPOSIT-US",
			"user_id": "5c0abeb9970f8426abc8df67"
		},
		{
			"_id": "5c0b0cfd1cfe2300a0fe490f",
			"_links": {
				"self": {
					"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0b0cfd1cfe2300a0fe490f"
				}
			},
			"allowed": "CREDIT",
			"client": {
				"id": "5be38afd6a785e6bddfffe68",
				"name": "test user"
			},
			"extra": {
				"note": None,
				"other": {
					"access_token": None,
					"updated_on": None
				},
				"supp_id": ""
			},
			"info": {
				"account_num": "2134",
				"address": "8001 VILLA PARK DRIVE, HENRICO, VA, US",
				"balance": {
					"amount": "0.00",
					"currency": "USD"
				},
				"bank_logo": "https://cdn.synapsepay.com/bank_logos/new/bofa.png",
				"bank_long_name": "BANK OF AMERICA",
				"bank_name": "BANK OF AMERICA",
				"class": "CHECKING",
				"match_info": {
					"email_match": "not_found",
					"name_match": "not_found",
					"phonenumber_match": "not_found"
				},
				"name_on_account": " ",
				"nickname": "Fake Account",
				"routing_num": "0017",
				"type": "PERSONAL"
			},
			"is_active": True,
			"timeline": [
				{
					"date": 1544228093046,
					"note": "Node created."
				},
				{
					"date": 1544228096991,
					"note": "Micro deposits initiated."
				}
			],
			"type": "ACH-US",
			"user_id": "5c0abeb9970f8426abc8df67"
		},
		{
			"_id": "5c0af4e64f98b000bc81c6fd",
			"_links": {
				"self": {
					"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0af4e64f98b000bc81c6fd"
				}
			},
			"allowed": "CREDIT-AND-DEBIT",
			"client": {
				"id": "5be38afd6a785e6bddfffe68",
				"name": "test user"
			},
			"extra": {
				"note": None,
				"other": {
					"access_token": "5c0af4eac3c43d7a63b1bc77"
				},
				"supp_id": ""
			},
			"info": {
				"balance": {
					"amount": 0,
					"currency": "USD"
				},
				"card_hash": "0ce83962ea95688a3801c302b31c18cbd71d992ab050b6f32468fc280b31ce31",
				"card_style_id": None,
				"document_id": "2a4a5957a3a62aaac1a0dd0edcae96ea2cdee688ec6337b20745eed8869e3ac8",
				"name_on_account": " ",
				"nickname": "My Debit Card",
				"preferences": {
					"allow_foreign_transactions": False,
					"atm_withdrawal_limit": 100,
					"pos_withdrawal_limit": 1000
				}
			},
			"is_active": True,
			"timeline": [
				{
					"date": 1544221925385,
					"note": "Node created."
				},
				{
					"date": 1544221937791,
					"note": "Card Created."
				}
			],
			"type": "CARD-US",
			"user_id": "5c0abeb9970f8426abc8df67"
		}
	],
	"page": 1,
	"page_count": 1,
	"success": True
}

""" Everything below is technically unused or can be mocked """

ach_us_logins = {
  "type": "ACH-US",
  "info":{
	"bank_id":"synapse_good",
	"bank_pw":"test1234",
	"bank_name":"fake"
  }
}

ach_us_acrt = {
  "type": "ACH-US",
  "info": {
	"nickname": "Fake Account",
	"account_num": "1232225674134",
	"routing_num": "051000017",
	"type": "PERSONAL",
	"class": "CHECKING"
  }
}

ach_us_payload = {
  "type": "ACH-US",
  "info": {
	"nickname": "Fake Account",
	"account_num": "12322134",
	"routing_num": "051000017",
	"type": "PERSONAL",
	"class": "CHECKING"
  }
}

ach_us_get_response = {
	"_id": "5c0b0cfd1cfe2300a0fe490f",
	"_links": {
		"self": {
			"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0b0cfd1cfe2300a0fe490f"
		}
	},
	"allowed": "CREDIT",
	"client": {
		"id": "5be38afd6a785e6bddfffe68",
		"name": "test user"
	},
	"extra": {
		"note": None,
		"other": {
			"access_token": None,
			"updated_on": None
		},
		"supp_id": ""
	},
	"info": {
		"account_num": "2134",
		"address": "8001 VILLA PARK DRIVE, HENRICO, VA, US",
		"balance": {
			"amount": "0.00",
			"currency": "USD"
		},
		"bank_logo": "https://cdn.synapsepay.com/bank_logos/new/bofa.png",
		"bank_long_name": "BANK OF AMERICA",
		"bank_name": "BANK OF AMERICA",
		"class": "CHECKING",
		"match_info": {
			"email_match": "not_found",
			"name_match": "not_found",
			"phonenumber_match": "not_found"
		},
		"name_on_account": " ",
		"nickname": "Fake Account",
		"routing_num": "0017",
		"type": "PERSONAL"
	},
	"is_active": True,
	"timeline": [
		{
			"date": 1544228093046,
			"note": "Node created."
		},
		{
			"date": 1544228096991,
			"note": "Micro deposits initiated."
		}
	],
	"type": "ACH-US",
	"user_id": "5c0abeb9970f8426abc8df67"
}

debit_us_payload = {
  "type": "DEPOSIT-US",
  "info": {
	"nickname":"My Deposit Account"
  }
}

debit_us_get_response = {
	"_id": "5c0b0ff74f98b000bd81f4af",
	"_links": {
		"self": {
			"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0b0ff74f98b000bd81f4af"
		}
	},
	"allowed": "CREDIT-AND-DEBIT",
	"client": {
		"id": "5be38afd6a785e6bddfffe68",
		"name": "test user"
	},
	"extra": {
		"note": None,
		"other": {},
		"supp_id": ""
	},
	"info": {
		"balance": {
			"amount": 0,
			"currency": "USD"
		},
		"document_id": None,
		"name_on_account": " ",
		"nickname": "My Deposit Account"
	},
	"is_active": True,
	"timeline": [
		{
			"date": 1544228854825,
			"note": "Node created."
		}
	],
	"type": "DEPOSIT-US",
	"user_id": "5c0abeb9970f8426abc8df67"
}


