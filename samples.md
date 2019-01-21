# Table of Contents
- [Client](#client)
	* [Initialize Client](#initialize-client)
	* [Update Headers](#update-headers)
	* [Create User](#create-user)
	* [Get User](#get-user)
	* [Get Subscription](#get-subscription)
	* [Update Subscription](#update-subscription)
	* [Get All Users](#get-all-users)
	* [Get All Client Transactions](#get-all-client-transactions)
	* [Get All Client Nodes](#get-all-client-nodes)
	* [Get All Client Institutions](#get-all-client-institutions)
	* [Issue Public Key](#issue-public-key)
- [User](#user)
	* [Get New Oauth](#get-new-oauth)
	* [Register New Fingerprint](#register-new-fingerprint)
	* [Update User or Update/Add Documents](#update-user-or-update-add-documents)
	* [Generate UBO](#generate-ubo)
	* [Get All User Nodes](#get-all-user-nodes)
	* [Get All User Transactions](#get-all-user-transactions)
	+ [Nodes](#nodes)
			* [Create Node](#create-node)
			* [Get Node](#get-node)
			* [Get All User Nodes](#get-all-user-nodes-1)
			* [Update Node](#update-node)
			* [Ship Debit](#ship-debit)
			* [Reset Debit](#reset-debit)
			* [Verify Micro Deposit](#verify-micro-deposit)
			* [Reinitiate Micro Deposit](#reinitiate-micro-deposit)
			* [Generate Apple Pay](#generate-apple-pay)
			* [Delete Node](#delete-node)
			* [Get All Node Subnets](#get-all-node-subnets)
			* [Get All Node Transactions](#get-all-node-transactions)
	+ [Subnets](#subnets)
			* [Create Subnet](#create-subnet)
			* [Get Subnet](#get-subnet)
	+ [Transactions](#transactions)
			* [Create Transaction](#create-transaction)
			* [Get Transaction](#get-transaction)
			* [Comment on Status](#comment-on-status)
			* [Dispute Transaction](#dispute-transaction)
			* [Cancel/Delete Transaction](#cancel-delete-transaction)
			* [Trigger Dummy Transactions](#trigger-dummy-transactions)

# Client
##### Initialize Client
```python
client = Client(
	client_id='client_id_1239ABCdefghijk1092312309',
	client_secret='client_secret_1239ABCdefghijk1092312309',
	fingerprint='1023918209480asdf8341098',
	ip_address='1.2.3.132',
	devmode=True
	)
```
##### Update Headers
```python
client.update_headers(
	client_secret='client_secret_1239ABCdefghijk1092312309',
	fingerprint='1023918209480asdf8341098',
	ip_address='1.2.3.132',
	oauth_key='oauth_bo4WXMIT5V0zKSRLYcqNwGtHZEDaA1k3pBv7r20s',
	idempotency_key='1234567'
	)
```
##### Create User
```python
body = {
	"logins": [
		{
			"email": "test@synapsefi.com"
		}
	],
	"phone_numbers": [
		"901.111.1111",
		"test@synapsefi.com"
	],
	"legal_names": [
		"Test User"
	],
	...
}

client.create_user(body)
```
##### Get User
```python
client.get_user('594e0fa2838454002ea317a0', full_dehydrate=True)
```
##### Create Subscription
```python
body = {
	"scope": [
		"USERS|POST",
		"USER|PATCH",
		"NODES|POST",
		"NODE|PATCH",
		"TRANS|POST",
		"TRAN|PATCH"
	],
	"url": "https://requestb.in/zp216zzp"
}
subs = client.create_subscription(body)
```
##### Get Subscription
```python
subs_id = '589b6adec83e17002122196c'
subs = client.get_subscription(subs_id)
```
##### Update Subscription
```python
body = {
		'subs_id': '589b6adec83e17002122196c'
		'url': 'https://requestb.in/zp216zzp'
		'scope': [
				"USERS|POST",
				"USER|PATCH",
				"NODES|POST",
				...
			]
		}
subs = client.update_subscription(body)
```
##### Get All Users
```python
allusers = client.get_all_users(show_refresh_tokens=True)
```
##### Get All Client Transactions
```python
alltrans = client.get_all_trans()
```
##### Get All Client Nodes
```python
allnodes = client.get_all_nodes()
```
##### Get All Client Institutions
```python
allinst = client.get_all_inst()
```
##### Issue Public Key
```python
scope = [
		"USERS|POST",
		"USER|PATCH",
		"NODES|POST",
		...
	]
pubkey = client.issue_public_key(scope)
```
# User
##### Get New Oauth
```python
body = {
		"refresh_token":"refresh_Y5beJdBLtgvply3KIzrh72UxWMEqiTNoVAfDs98G",
		"scope":[
				"USER|PATCH",
				"USER|GET",
				...
		]
}

user.oauth(body)
```
##### Register New Fingerprint
1. Supply the new fingerprint:
```python
client.update_headers(fingerprint='e83cf6ddcf778e37bfe3d48fc78a6502062fcxx')
user.oauth()
```
2. Supply 2FA device from the list
```python
user.select_2fa_device('test@synapsefi.com')
```
3. Verify the pin sent to the 2FA device
```python
user.confirm_2fa_pin('594230')
```

##### Update User or Update/Add Documents
```python
body = {
	"update":{
		"login":{
			"email":"test2@synapsefi.com"
		},
		"remove_login":{
			"email":"test@synapsefi.com"
		},
		"phone_number":"901-111-2222",
		"remove_phone_number":"901.111.1111"
		}
}

user.update_info(body)
```
##### Generate UBO
```python
body = {
	 "entity_info": {
			"cryptocurrency": True,
			"msb": {
				 "federal": True,
				 "states": ["AL"]
			},
			"public_company": False,
			"majority_owned_by_listed": False,
			"registered_SEC": False,
			"regulated_financial": False,
			"gambling": False,
			"document_id": "2a4a5957a3a62aaac1a0dd0edcae96ea2cdee688ec6337b20745eed8869e3ac8"
	 ...
}

user.create_ubo(body)
```
##### Get All User Nodes
```python
user.get_all_nodes(page=4, per_page=10, type='DEPOSIT-US')
```
##### Get All User Transactions
```python
user.get_all_trans(page=4, per_page=10)
```
### Nodes
##### Create Node
Refer to the following docs for how to setup the payload for a specific Node type:
- [Direct Deposit Accounts](https://docs.synapsefi.com/docs/opening-direct-deposit-accounts)
- [Issue Card](https://docs.synapsefi.com/docs/issue-a-card-number-1)
- [ACH-US with Logins](https://docs.synapsefi.com/docs/linking-an-ach-account-via-bank-logins)
- [ACH-US with AC/RT](https://docs.synapsefi.com/docs/linking-an-ach-account-with-accountrouting-number)
- [INTERCHANGE-US](https://docs.synapsefi.com/docs/link-a-card)
- [CHECK-US](https://docs.synapsefi.com/docs/create-the-check-account)
- [WIRE-US](https://docs.synapsefi.com/docs/sending-a-domestic-wire)
- [WIRE-INT](https://docs.synapsefi.com/docs/sending-an-international-wire)
- [IOU](https://docs.synapsefi.com/docs/opening-a-ledgering-account)

```python
body = {
	"type": "DEPOSIT-US",
	"info":{
			"nickname":"My Checking"
	}
}

user.create_node(body, idempotency_key='123456')
```
##### Get Node
```python
node_id = '594e606212e17a002f2e3251'
node = user.get_node(node_id, full_dehydrate=True, force_refresh=True)
```
##### Get All User Nodes
```python
nodes = user.get_nodes(page=1, per_page=5, type='ACH-US')
```
##### Update Node
```python
node_id = '5ba05ed620b3aa005882c52a'
body = {
	"supp_id":"new_supp_id_1234"
}
nodes = user.update_node(node_id, body)
```
##### Ship Debit
```python
node_id = '5ba05ed620b3aa005882c52a'

body = {
	"fee_node_id":"5ba05e7920b3aa006482c5ad",
	"expedite":True
}

nodes = user.ship_debit(node_id, body)
```
##### Reset Debit
```python
node_id = '5ba05ed620b3aa005882c52a'
nodes = user.reset_debit(node_id)
```
##### Verify Micro Deposit
```python
node_id = '5ba05ed620b3aa005882c52a'
body = {
	"micro":[0.1,0.1]
}
nodes = user.verify_micro(node_id, body)
```
##### Reinitiate Micro Deposit
```python
node_id = '5ba05ed620b3aa005882c52a'
nodes = user.reinit_micro(node_id)
```
##### Generate Apple Pay
```python
node_id = '5ba05ed620b3aa005882c52a'
body = {
	"certificate": "your applepay cert",
	"nonce": "9c02xxx2",
	"nonce_signature": "4082f883ae62d0700c283e225ee9d286713ef74"
}
nodes = user.generate_apple_pay(node_id)
```
##### Delete Node
```python
node_id = '594e606212e17a002f2e3251'
user.delete_node(node_id, trans_id, 'Pending verification...')
```
##### Get All Node Subnets
```python
node_id = '594e606212e17a002f2e3251'
user.get_all_subnets(node_id, page=4, per_page=10)
```
##### Get All Node Transactions
```python
node_id = '594e606212e17a002f2e3251'
user.get_all_node_trans(node_id, page=4, per_page=10)
```
### Subnets
##### Create Subnet
```python
node_id = '594e606212e17a002f2e3251'
body = {
	"nickname":"Test AC/RT"
}
user.create_subnet(node_id, body)
```
##### Get Subnet
```python
node_id = '594e606212e17a002f2e3251'
subn_id = '59c9f77cd412960028b99d2b'
user.get_subnet(node_id, subn_id)
```
### Transactions
##### Create Transaction
```python
node_id = '594e606212e17a002f2e3251'
body = {
	"to": {
		"type": "ACH-US",
		"id": "594e6e6c12e17a002f2e39e4"
	},
	"amount": {
		"amount": 20.1,
		"currency": "USD"
	},
	"extra": {
		"ip": "192.168.0.1"
	}
}

user.create_trans(node_id, body)
```
##### Get Transaction
```python
node_id = '594e606212e17a002f2e3251'
trans_id = '594e72124599e8002fe62e4f'
user.get_trans(node_id, trans_id)
```
##### Comment on Status
```python
node_id = '594e606212e17a002f2e3251'
trans_id = '594e72124599e8002fe62e4f'
user.comment_status(node_id, trans_id, 'Pending verification...')
```
##### Dispute Transaction
```python
node_id = '594e606212e17a002f2e3251'
trans_id = '594e72124599e8002fe62e4f'
dispute_reason = 'Chargeback...'
user.cancel_trans(node_id, trans_id, dispute_reason)
```
##### Cancel/Delete Transaction
```python
node_id = '594e606212e17a002f2e3251'
trans_id = '594e72124599e8002fe62e4f'
user.dummy_tran(node_id, trans_id)
```
##### Trigger Dummy Transactions
```python
node_id = '594e606212e17a002f2e3251'
user.cancel_trans(node_id, is_credit=True)
```