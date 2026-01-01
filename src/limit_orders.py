import logging

def place_limit_order(client, symbol, side, quantity, price):
    try:
        logging.info(f"LIMIT | {side} {quantity} {symbol} @ {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )

        logging.info(f"LIMIT SUCCESS | {order}")
        return order

    except Exception as e:
        logging.error(f"LIMIT FAILED | {e}")
        raise
