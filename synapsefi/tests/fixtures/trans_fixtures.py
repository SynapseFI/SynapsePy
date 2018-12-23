
trans_payload = {
  "to": {
    "type": "DEPOSIT-US",
    "id": "5c0b0ff74f98b000bd81f4af"
  },
  "amount": {
    "amount": 300,
    "currency": "USD"
  },
  "extra": {
    "ip": "192.168.0.1",
    "note": "Test transaction"
  }
}

trans_get_response = {
    "_id": "5c0b1562905a4e00cb631470",
    "_links": {
        "self": {
            "href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0b0cfd1cfe2300a0fe490f/trans/5c0b1562905a4e00cb631470"
        }
    },
    "_v": 2,
    "amount": {
        "amount": 300,
        "currency": "USD"
    },
    "client": {
        "id": "5be38afd6a785e6bddfffe68",
        "name": "* Matthew Bernardo"
    },
    "extra": {
        "asset": None,
        "created_on": 1544230242087,
        "encrypted_note": "",
        "group_id": None,
        "ip": "192.168.0.1",
        "latlon": "0,0",
        "note": "Test transaction",
        "process_on": 1544230242087,
        "same_day": False,
        "supp_id": ""
    },
    "fees": [
        {
            "fee": 0,
            "note": "Facilitator Fee",
            "to": {
                "id": "None"
            }
        }
    ],
    "from": {
        "id": "5c0b0cfd1cfe2300a0fe490f",
        "nickname": "Fake Account",
        "type": "ACH-US",
        "user": {
            "_id": "5c0abeb9970f8426abc8df67",
            "legal_names": [
                "Test User"
            ]
        }
    },
    "recent_status": {
        "date": 1544230242087,
        "note": "Transaction Created.",
        "status": "CREATED",
        "status_id": "1"
    },
    "timeline": [
        {
            "date": 1544230242087,
            "note": "Transaction Created.",
            "status": "CREATED",
            "status_id": "1"
        }
    ],
    "to": {
        "id": "5c0b0ff74f98b000bd81f4af",
        "nickname": "My Deposit Account",
        "type": "DEPOSIT-US",
        "user": {
            "_id": "5c0abeb9970f8426abc8df67",
            "legal_names": [
                "Test User"
            ]
        }
    }
}

get_all_trans_resp = {
    "error_code": "0",
    "http_code": "200",
    "limit": 20,
    "page": 1,
    "page_count": 1,
    "success": True,
    "trans": [
        {
            "_id": "5c0b1562905a4e00cb631470",
            "_links": {
                "self": {
                    "href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67/nodes/5c0b0ff74f98b000bd81f4af/trans/5c0b1562905a4e00cb631470"
                }
            },
            "_v": 2,
            "amount": {
                "amount": 300,
                "currency": "USD"
            },
            "client": {
                "id": "5be38afd6a785e6bddfffe68",
                "name": "Matthew Bernardo"
            },
            "extra": {
                "asset": None,
                "created_on": 1544230242087,
                "encrypted_note": "",
                "group_id": None,
                "ip": "192.168.0.1",
                "latlon": "0,0",
                "note": "Test transaction",
                "process_on": 1544230242087,
                "same_day": False,
                "supp_id": ""
            },
            "fees": [
                {
                    "fee": 0.2,
                    "note": "Synapse Facilitator Fee",
                    "to": {
                        "id": "55b3f8c686c2732b4c4e9df6"
                    }
                }
            ],
            "from": {
                "id": "5c0b0cfd1cfe2300a0fe490f",
                "nickname": "Fake Account",
                "type": "ACH-US",
                "user": {
                    "_id": "5c0abeb9970f8426abc8df67",
                    "legal_names": [
                        "Test User"
                    ]
                }
            },
            "recent_status": {
                "date": 1544230251191,
                "note": "Unable to settle transaction from 5c0b0cfd1cfe2300a0fe490f, since the node 'allowed' is CREDIT.",
                "status": "CANCELED",
                "status_id": "5"
            },
            "timeline": [
                {
                    "date": 1544230242087,
                    "note": "Transaction Created.",
                    "status": "CREATED",
                    "status_id": "1"
                },
                {
                    "date": 1544230251191,
                    "note": "Unable to settle transaction from 5c0b0cfd1cfe2300a0fe490f, since the node 'allowed' is CREDIT.",
                    "status": "CANCELED",
                    "status_id": "5"
                }
            ],
            "to": {
                "id": "5c0b0ff74f98b000bd81f4af",
                "nickname": "My Deposit Account",
                "type": "DEPOSIT-US",
                "user": {
                    "_id": "5c0abeb9970f8426abc8df67",
                    "legal_names": [
                        "Test User"
                    ]
                }
            }
        }
    ],
    "trans_count": 1
}
