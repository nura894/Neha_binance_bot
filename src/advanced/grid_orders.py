import logging

def place_grid_orders(
    client,
    symbol,
    side,
    quantity,
    lower_price,
    upper_price,
    grid_count
):
    try:
        logging.info(
            f"GRID | {symbol} | {grid_count} levels "
            f"range {lower_price} - {upper_price}"
        )

        step = (upper_price - lower_price) / grid_count
        orders = []

        for i in range(grid_count):
            price = lower_price + step * i

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=round(price, 2)
            )

            orders.append(order)
            logging.info(f"GRID order placed @ {price}")

        return orders

    except Exception as e:
        logging.error(f"GRID FAILED | {e}")
        raise
