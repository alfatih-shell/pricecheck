import argparse
import sys
import time
import requests
from dmacheck import opsgenie_utils
from alertg.app import check_gas_price


def get_token_price(token_address, chain_name, api_key):
    url = f"https://public-api.birdeye.so/defi/price?address={token_address}"
    headers = {
        "accept": "application/json",
        "x-chain": chain_name,
        "X-API-KEY": api_key,
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            price_data = data.get("data", {})
            token_price = price_data.get("value")
            if token_price is not None:
                return token_price
            else:
                print("Token price not found in response.")
                return None
        else:
            print("Failed to fetch token price:", data.get("message"))
            return None
    else:
        print("Failed to fetch token price. Status code:", response.status_code)
        return None


def alert_to_opsgenie(token_address, token_price):
    alert_payload = {
        "message": f"[Price-Checker] Your favourite token {token_address} currently at price {token_price}",
        "description": "Let's check on birdeye.so",
        "responders": [{"name": "me", "type": "team"}],
        "visible_to": [{"name": "me", "type": "team"}],
        "note": "This alert generated by me",
        "user": "zackzonexx",
        "priority": "P3",
        "source": "Price Checker Tools",
    }
    # Call the function from opsgenie_utils to create the alert
    opsgenie_utils.create_alert(alert_payload)
    print("Alert created in Opsgenie.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch token price and alert to Opsgenie."
    )
    parser.add_argument("--token_address", required=True, help="Token address")
    parser.add_argument("--chain_name", required=True, help="Chain name")
    parser.add_argument("--api_key", required=True, help="API key from birdeye.so")
    parser.add_argument(
        "--etherscan_api_key",
        required=True,
        help="Etherscan API key for gas price checking",
    )  # Add Etherscan API key for gas price check
    parser.add_argument(
        "--threshold", type=float, required=True, help="Price threshold"
    )
    args = parser.parse_args()

    missing_args = [arg for arg in vars(args) if getattr(args, arg) is None]
    if missing_args:
        sys.stderr.write(f"Missing required argument(s): {', '.join(missing_args)}\n")
        sys.exit(1)

    while True:
        token_price = get_token_price(args.token_address, args.chain_name, args.api_key)
        if token_price is not None and token_price >= args.threshold:
            alert_to_opsgenie(args.token_address, token_price)

            current_gas_price = check_gas_price(args.etherscan_api_key)
            if current_gas_price:
                print(
                    f"Gas price is below the threshold. Current safe gas price: {current_gas_price}"
                )
            else:
                print("Gas price is above the threshold or couldn't be fetched.")
        time.sleep(10)  # Sleep for 10 seconds before checking again
