# Deploy on Degen
The included python scripts in this project are a python representation of the Deploy on Degen workshop 
hosted by Syndicate for the Deploy on Degen week:  https://lu.ma/ofb9n1la

All code is provided as-is with ZERO warranty or support, and may be freely distributed as you wish.


## Setup
Follow the steps below to clone and setup a python environment to run the python code.
```bash
# 1. clone the repo to your local computer
git clone git@github.com:mrtrosen/deploy_on_degen.git

# 2. enter the project directory
cd deploy_on_degen

# 3. create a python virtual environment
python -m venv .venv

# 4. activate the virtual environment
source .venv/bin/activate

# 5. copy the env_example file to .env
cp env_example .env

# 6. use your favorite editor to update the .env file with the appropriate settings.

```

### Update .env file with correct information for your Syndicate environment
 - SYNDICATE_API_KEY
   - Your API key from your Syndicate project
   - Settings - API Keys - CLICK TO REVEAL
 - SYNDICATE_PROJECT_ID
   - Settings - General - Project ID
 - SYNDICATE_DEMO_CONTRACT_OWNER_ADDRESS
   - What wallet will be the owner of the created contract
   - This should be a wallet that you control!
 - SYNDICATE_DEMO_MINT_MODULE_CONTRACT_ADDRESS
   - Obtained from the syndicate_create_contract.py transaction details
   - Transactions - Click on Tx Hash to go to blockscout
   - Click on 'Internal txns'
   - Find the 'Create' internal tnx type, should be the 2nd from the top of the internal txns
   - Click The copy icon on the 'To' address field.  Use this address as the mint module contract address
 - WALLET_ADDRESS_TO_SEND_MINTED_NFT_TO
   - The wallet address to send the minted NFT to. 
 - NFT_TOKEN_NAME
 - The name of the NFT Token you wish to create.
   - example: Python Deploy on Degen Workshop
 - NFT_TOKEN_NAME
   - The symbole of the NFT Token you wish to create
   - example:  PYDEPLOY

## Ready to Start!
You should now be able to run the following python scripts to complete the Deploy on Degen syndicate examples!
```bash
# first, create the contract
python syndicate_create_contract.py

# now, try to mint the first NFT token!
python syndicate_broadcast_first_mint.py

# and if that works, try to create 100 more!
python syndicate_broadcast_100_mints.py

```
While you run the steps above, you can watch the transactions process in your syndicate admin through the 'Transactions' 
tab.



