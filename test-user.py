import synapsepy
from synapsepy.client import Client

# new_client = Client()
client = Client(
	client_id='client_id_1239ABCdefghijk1092312309',
	client_secret='client_secret_1239ABCdefghijk1092312309',
	fingerprint='1023918209480asdf8341098',
	ip_address='1.2.3.132',
	devmode=True
	)

print(client)