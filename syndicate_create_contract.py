from dotenv import dotenv_values
import requests

# load the .env file into a python dictionary for easy access
config = dotenv_values(".env")

"""
This is the python equivalent of the contract creation curl script:
    curl -H 'Authorization: Bearer YOUR_API_KEY' \
     -H "Content-type: application/json" \
      -d '{
      "projectId": "YOUR_PROJECT_ID",
      "contractAddress": "0xfBFeE6E588cbD17357F2651B67ef3c30DA5bcAEA",
      "chainId": 666666666,
      "functionSignature": "createWithOpenMint(address owner,string calldata name,string calldata symbol)",
      "args": {
        "owner": "0x_CONTRACT_OWNER",
        "name": "Deploy on Degen Workshop",
        "symbol": "DEPLOY"
      }
     }' \
     'https://api.syndicate.io/transact/sendTransaction'

"""


if __name__ == "__main__":
    url = "https://api.syndicate.io/transact/sendTransaction"

    payload = {
        "projectId": config["SYNDICATE_PROJECT_ID"],
        "contractAddress": "0xfBFeE6E588cbD17357F2651B67ef3c30DA5bcAEA",
        "chainId": 666666666,
        "functionSignature": "createWithOpenMint(address owner,string calldata name,string calldata symbol)",
        "args": {
            'owner': config["SYNDICATE_DEMO_CONTRACT_OWNER_ADDRESS"],
            'name': config["NFT_TOKEN_NAME"],
            'symbol': config["NFT_TOKEN_SYMBOL"],
        }
    }

    # We need to send in a User-Agent to the API endpoint otherwise it will
    # return with a 403 Forbidden error.
    headers = {
        "Authorization": f"Bearer {config['SYNDICATE_API_KEY']}",
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    response_json = response.json()
    if "transactionId" in response_json:
        print(f"Transaction ID is: {response_json['transactionId']}")
    else:
        print("There was an issue with sending the transaction.")
        print(response)
        print(response.text)

