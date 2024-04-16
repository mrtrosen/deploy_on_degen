from dotenv import dotenv_values
import requests

# load the .env file into a python dictionary for easy access
config = dotenv_values(".env")

"""
This is the python equivalent of the broadcast mint curl script:
    curl -H 'Authorization: Bearer YOUR_API_KEY' \
 -H "Content-type: application/json" \
  -d '{
  "projectId": "YOUR_PROJECT_ID",
  "contractAddress": "DEMO_MINT_MODULE_CONTRACT_ADDRESS",
  "chainId": 666666666,
  "functionSignature": "mint(address account)",
  "args": {
    "account": <WALLET_ADDRESS_TO_SEND_MINTED_NFT_TO>
  }
 }' \
 'https://api.syndicate.io/transact/sendTransaction'

"""


if __name__ == "__main__":
    url = "https://api.syndicate.io/transact/sendTransaction"

    # loop from 1 through 101.
    # Why 101? Because the range function will go up to, but not include, the end range
    # thus creating 100 new mint transactions
    for i in range(1, 101):
        payload = {
            "projectId": config["SYNDICATE_PROJECT_ID"],
            "contractAddress": config["SYNDICATE_DEMO_MINT_MODULE_CONTRACT_ADDRESS"],
            "chainId": 666666666,
            "functionSignature": "mint(address account)",
            "args": {
                "account": config["WALLET_ADDRESS_TO_SEND_MINTED_NFT_TO"]
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

