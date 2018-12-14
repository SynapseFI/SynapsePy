# SynapsePy

Python wrapper for SynapseFi API

## USAGE
##### Import
```python
import SynapsePy
```
## Client

##### Create Client
```python
client = Client(
	client_id='client_id_1239ABCdefghijk1092312309',
	client_secret='client_secret_1239ABCdefghijk1092312309',
	fingerprint='1023918209480asdf8341098',
	ip_address='1.2.3.132',
	devmode=True
	)
```
##### Create User
```python
basicuser = {
  "logins": [
	{
	  "email": "test1@synapsefi.com"
	}
  ],
  "phone_numbers": [
	"901.111.1111",
	"test1@synapsefi.com"
  ],
  "legal_names": [
	"Basic User"
  ]
  ...
}

client.create_user(basicuser)
```
##### Get User
```python
userid = '5bf456bab68b62008e5a9ce3'
user = client.get_user(userid)
```
##### Create Subscription
```python
url = 'https://requestb.in/zp216zzp'
scope = [
    "USERS|POST",
    "USER|PATCH",
    "NODES|POST",
    "NODE|PATCH",
    "TRANS|POST",
    "TRAN|PATCH"
  ]
response = client.create_subscription(url, scope)
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
##### Get All Transactions
```python
alltrans = client.get_all_trans()
```
##### Get All Nodes
```python
allnodes = client.get_all_nodes()
```
##### Get All Institutions
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

## User
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
##### Update Info/Documents
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
##### Get Node
```python
node = user.get_node('594e606212e17a002f2e3251', full_dehydrate=True, force_refresh=True)
```
##### Get All Nodes
```python
nodes = user.get_nodes(page=1, per_page=5, type='ACH-US')
```
##### Comment on Status
```python
user.comment_status(trans_id, 'Pending verification...')
```
##### Cancel/Delete Transaction
```python
user.cancel_trans(trans_id)
```
