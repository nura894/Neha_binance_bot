import logging

def place_oco_order(
    client,
    symbol,
    side,
    quantity,
    take_profit_price,
    stop_price,
    stop_limit_price
):
    try:
        logging.info("OCO | placing take-profit and stop-loss")

        tp = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=take_profit_price
        )

        sl = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            timeInForce="GTC",
            quantity=quantity,
            stopPrice=stop_price,
            price=stop_limit_price
        )

        logging.info("OCO SUCCESS")
        return {"take_profit": tp, "stop_loss": sl}

    except Exception as e:
        logging.error(f"OCO FAILED | {e}")
        raise
