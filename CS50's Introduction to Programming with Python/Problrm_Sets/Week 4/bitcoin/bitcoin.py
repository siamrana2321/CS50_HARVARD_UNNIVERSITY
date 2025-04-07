import sys
import requests

def get_bitcoin_price():
    url = "https://api.coincap.io/v2/assets/bitcoin"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price_per_bitcoin = get_bitcoin_price()

    total_cost = num_bitcoins * price_per_bitcoin

    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
