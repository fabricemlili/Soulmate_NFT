# How can you create your SoulMate NFT ?

## 1) Requirements

You can create your own environment if you want but here we just give keys to get all the requirements by installing.

**install skimage:**  

```jsx
python -m pip install -U scikit-image
```

**install pyxelate:**  

```sh
pip install git+https://github.com/sedthh/pyxelate.git --upgrade
```
**install hardhat:**  

```jsxs
yarn add --dev hardhat
```

Or  with npm 

```jsx
npm install hardhat 
```

## 2) Tranform a picture of you

Firstly, run the create_photo.py and enter the path of your picture file after the "Enter the path of the image: " message.
```jsxs
python3 create_photo.py
```

Once the pixalating is finished, you can find your picture pixalated at the same path that the basic picture.

## 3) Make the picture a NFT

Now, we need to use the image pixaleted to make it a NFT. To do it, you need to be registered on pinata. Create an account if 
doesn't make it yet. https://www.pinata.cloud

Upload the pixalated image into your pinata collection.

## 3) Metadata

Create your metadata in the ```metadata``` folder naming the new file as ```yourFirstName.json``` and copying the structure from another already existing json file. You can modify the description, the attributes, name as you wish. Copy the link of your image on pinata and paste it after ```"image":```. 

## 4) Deploy

On your terminal at the root directory run 

```sh
npx hardhat run scripts/deploy.js --network mumbai
```
Paste the result given by the command it is the address that we will need for the next step

## 5) Mint 

- First step ```"smart-contract-address"``` by the smart contract address of your Metamask account.
- Second step```"address"``` by the address you pasted before
- Third step ```"token-ueri"``` by the link of your image from Pinata

## 6) Look in OpenSea
Go into this link: 
https://testnets.opensea.io/assets/mumbai/smart-contract-address/YOUR-TOKEN-ID \
Replace with your smart contract address \
YOUR-TOKEN-ID refers to the number of time you ran your deploy if it is your first it is then 1
