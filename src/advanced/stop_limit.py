import logging

def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    try:
        logging.info(
            f"STOP-LIMIT | {side} {quantity} {symbol} "
            f"STOP={stop_price} LIMIT={limit_price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            timeInForce="GTC",
            quantity=quantity,
            stopPrice=stop_price,
            price=limit_price
        )

        logging.info(f"STOP-LIMIT SUCCESS | {order}")
        return order

    except Exception as e:
        logging.error(f"STOP-LIMIT FAILED | {e}")
        raise
