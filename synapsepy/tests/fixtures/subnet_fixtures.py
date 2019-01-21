
subnet_payload = {
	"nickname":"Test AC/RT"
}

subnet_get_resp = {
	"_id": "5c1151d32a3d440028193353",
	"_links": {
		"self": {
			"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0b0ff74f98b000bd81f4af/subnets/5c1151d32a3d440028193353"
		}
	},
	"account_class": "CHECKING",
	"account_num": "9826249105",
	"client": {
		"id": "5be38afd6a785e6bddfffe68",
		"name": "Matthew Bernardo"
	},
	"nickname": "Test AC/RT",
	"node_id": "5c0b0ff74f98b000bd81f4af",
	"routing_num": {
		"ach": "084106768",
		"wire": "084106768"
	},
	"user_id": "5c0abeb9970f8426abc8df67"
}

subnet_get_all_resp = {
	"error_code": "0",
	"http_code": "200",
	"limit": 20,
	"page": 1,
	"page_count": 1,
	"subnets": [
		{
			"_id": "5c1151d32a3d440028193353",
			"_links": {
				"self": {
					"href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0b0ff74f98b000bd81f4af/subnets/5c1151d32a3d440028193353"
				}
			},
			"account_class": "CHECKING",
			"account_num": "9826249105",
			"client": {
				"id": "5be38afd6a785e6bddfffe68",
				"name": "Matthew Bernardo"
			},
			"nickname": "Test AC/RT",
			"node_id": "5c0b0ff74f98b000bd81f4af",
			"routing_num": {
				"ach": "084106768",
				"wire": "084106768"
			},
			"user_id": "5c0abeb9970f8426abc8df67"
		}
	],
	"subnets_count": 1,
	"success": True
}