import csv

from store.models import Item, Order


def load_orders(path: str) -> list[Order]:
    orders: dict[str, Order] = {}
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            order = orders.setdefault(row["order_id"], Order(row["order_id"], row["customer"]))
            order.items.append(Item(row["item"], float(row["unit_price"]), int(row["quantity"])))
    return list(orders.values())
