import logging

def place_market_order(client, symbol, side, quantity):
    try:
        logging.info(f"MARKET | {side} {quantity} {symbol}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"MARKET SUCCESS | {order}")
        return order

    except Exception as e:
        logging.error(f"MARKET FAILED | {e}")
        raise
