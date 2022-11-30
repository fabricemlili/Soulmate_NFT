name = input(" Comment vous appelez-vous ? ")
age = input("Quel age avez-vous ? ")
eye = input("De quel couleurs sont vos yeux ? ")

import requests

url = "https://gateway.pinata.cloud/ipfs/QmayDn2KjygywMT1GFpB4map9Pbs8A4XVyNv3atM9DmijA"

payload={'pinataOptions': '{"cidVersion": 1}',
'pinataMetadata': '{"name": "MyFile", "keyvalues": {"company": "Pinata"}'}
files=[
  ('file',('JH.png',open('/Users/chloe/Soulmate_NFT/nft-test/photos/JH.png','rb'),'application/octet-stream'))
]
headers = {
  'Authorization': 'Bearer JWT FROM PINATA API KEYS'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

