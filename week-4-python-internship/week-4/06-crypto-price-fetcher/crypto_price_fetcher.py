"""
Mini Project Task: Write a program to fetch live cryptocurrency prices.

Uses the free CoinGecko public API (no API key required).
Docs: https://www.coingecko.com/en/api/documentation
"""

import requests

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_crypto_prices(coin_ids, vs_currency="usd"):
    """Fetch current prices for a list of coin IDs (e.g. ['bitcoin', 'ethereum'])."""
    params = {
        "ids": ",".join(coin_ids),
        "vs_currencies": vs_currency,
    }
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def display_prices(prices, vs_currency):
    if not prices:
        print("No price data returned. Check the coin names and try again.")
        return

    print(f"\n{'Coin':<15}{'Price (' + vs_currency.upper() + ')':<15}")
    print("-" * 30)
    for coin, data in prices.items():
        price = data.get(vs_currency, "N/A")
        print(f"{coin:<15}{price:<15}")


def main():
    print("=== Live Cryptocurrency Price Fetcher ===")
    print("Example coin IDs: bitcoin, ethereum, dogecoin, solana, cardano")

    coins_input = input("Enter coin names separated by commas: ").strip()
    coin_ids = [c.strip().lower() for c in coins_input.split(",") if c.strip()]

    if not coin_ids:
        print("No coins entered.")
        return

    vs_currency = input("Enter currency to compare against (default: usd): ").strip().lower() or "usd"

    try:
        prices = get_crypto_prices(coin_ids, vs_currency)
    except requests.exceptions.RequestException as e:
        print(f"Error: Network request failed ({e}).")
        return

    display_prices(prices, vs_currency)


if __name__ == "__main__":
    main()
