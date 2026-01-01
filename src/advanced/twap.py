import logging
import time

def place_twap_order(client, symbol, side, total_quantity, slices, interval_seconds):
    try:
        slice_qty = total_quantity / slices
        orders = []

        logging.info(
            f"TWAP | {slices} slices | "
            f"{slice_qty} each | interval {interval_seconds}s"
        )

        for i in range(slices):
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=slice_qty
            )

            orders.append(order)
            logging.info(f"TWAP slice {i+1}/{slices} executed")

            if i < slices - 1:
                time.sleep(interval_seconds)

        return orders

    except Exception as e:
        logging.error(f"TWAP FAILED | {e}")
        raise
