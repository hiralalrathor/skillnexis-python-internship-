# Mini Project Task: Live Cryptocurrency Price Fetcher

**Assignment:** Write a program to fetch live cryptocurrency prices.

Fetches current prices for one or more cryptocurrencies using the
free, public CoinGecko API — no API key required.

## Setup
```bash
pip install requests
```

## Concepts Used
- REST API calls with the `requests` library
- JSON response parsing
- Exception handling for network errors
- User input handling (multiple comma-separated values)

## How to Run
```bash
python crypto_price_fetcher.py
```

## Example
```
=== Live Cryptocurrency Price Fetcher ===
Example coin IDs: bitcoin, ethereum, dogecoin, solana, cardano
Enter coin names separated by commas: bitcoin, ethereum
Enter currency to compare against (default: usd): usd

Coin           Price (USD)    
------------------------------
bitcoin        63250          
ethereum       3120           
```

## Note
This script makes a live network call to the CoinGecko API, so it
needs internet access to run — it cannot be tested in an offline
sandbox, but the code is complete and ready to run on your machine.
No API key or signup is required for this endpoint.
