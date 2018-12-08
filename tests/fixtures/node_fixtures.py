
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
		"name": "Matthew Bernardo"
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

card_us_up = {
  "allowed":"CREDIT-AND-DEBIT"
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
		"name": "Matthew Bernardo"
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