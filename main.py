import logging
from binance import Client

from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco import place_oco_order
from src.advanced.twap import place_twap_order
from src.advanced.grid_orders import place_grid_orders


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="bot.log"
)


def validate_inputs(symbol, side, quantity):
    if not symbol.isalpha():
        raise ValueError("Invalid symbol")
    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")


def create_client(api_key, api_secret):
    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com"
    return client


def main():
    API_KEY = "YOUR_TESTNET_API_KEY"
    API_SECRET = "YOUR_TESTNET_API_SECRET"

    client = create_client(API_KEY, API_SECRET)

    order_type = input("Order type(MARKET/LIMIT/STOP-LIMIT/OCO/TWAP/GRID): ").upper()
    symbol = input("Symbol(BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()

    try:
        if order_type == "MARKET":
            qty = float(input("Quantity: "))
            validate_inputs(symbol, side, qty)
            result = place_market_order(client, symbol, side, qty)

        elif order_type == "LIMIT":
            qty = float(input("Quantity: "))
            price = float(input("Limit price: "))
            validate_inputs(symbol, side, qty)
            result = place_limit_order(client, symbol, side, qty, price)

        elif order_type == "STOP-LIMIT":
            qty = float(input("Quantity: "))
            stop_p = float(input("Stop price: "))
            limit_p = float(input("Limit price: "))
            validate_inputs(symbol, side, qty)
            result = place_stop_limit_order(client, symbol, side, qty, stop_p, limit_p)

        elif order_type == "OCO":
            qty = float(input("Quantity: "))
            tp = float(input("Take profit price: "))
            stop = float(input("Stop price: "))
            stop_limit = float(input("Stop-limit price: "))
            validate_inputs(symbol, side, qty)
            result = place_oco_order(client, symbol, side, qty, tp, stop, stop_limit)

        elif order_type == "TWAP":
            total_qty = float(input("Total quantity: "))
            slices = int(input("Slices: "))
            interval = int(input("Interval seconds: "))
            validate_inputs(symbol, side, total_qty)
            result = place_twap_order(client, symbol, side, total_qty, slices, interval)

        elif order_type == "GRID":
            qty = float(input("Quantity per order: "))
            lower = float(input("Lower price: "))
            upper = float(input("Upper price: "))
            grids = int(input("Grid count: "))
            validate_inputs(symbol, side, qty)
            result = place_grid_orders(client, symbol, side, qty, lower, upper, grids)

        else:
            raise ValueError("Invalid order type")

        print("SUCCESS")
        print(result)

    except Exception as e:
        print("FAILED")
        print(e)


if __name__ == "__main__":
    main()
