# Binance Futures Order Bot (USDT-M Testnet)

## Overview
This project is a command-line trading bot built for **Binance USDT-M Futures Testnet**.
It allows placing **Market** and **Limit** and some **advanced** orders using the official demo Binance API.
The project includes proper logging and error handling and is intended for learning
and assignment evaluation purposes.

---

## Features
- Market Order placement
- Limit Order placement
- Binance Futures **Testnet** support
- Logging of all actions to `bot.log`
- Error handling using exceptions
- Modular project structure

---

## Project Structure

CRYPTO-TRADING-BOT/
├── src/
│   ├── __init__.py
│   ├── market_orders.py        # Market order execution
│   ├── limit_orders.py         # Limit order execution
│   └── advanced/
│       ├── __init__.py
│       ├── stop_limit.py       # Stop-Limit orders
│       ├── oco.py              # OCO orders
│       ├── twap.py             # TWAP strategy
│       └── grid_orders.py      # Grid trading strategy
├── main.py                     # Entry point
├── README.md                   # Documentation
└── report.pdf                  # Project report




---

## Prerequisites
- Python 3.8 or higher
- Binance Futures Testnet account
- Testnet API Key and Secret

---

## API Setup (Binance Futures Testnet)
1. Visit https://testnet.binancefuture.com
2. Log in using GitHub or Binance account
3. Create a new API key
4. Enable **Futures trading permission**
5. Copy the API Key and Secret

⚠️ Do **not** use real Binance API keys.

---

## Installation
Install the required dependency:


pip install python-binance


## How to Run

1. Open main.py

2. Paste your testnet API key and secret:

API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_SECRET_KEY"


3. Run the program:

python main.py


## Logging

All order requests and responses are logged to:

bot.log


Each log entry includes timestamp, order type, and stat

