import csv

from store.models import Item, Order


def parse_rows(rows: list[dict]) -> list[Order]:
    orders: dict[str, Order] = {}
    for row in rows:
        order_id = str(row["order_id"])
        order = orders.setdefault(order_id, Order(order_id, row["customer"], row["cpf"]))
        order.items.append(Item(row["item"], float(row["unit_price"]), int(row["quantity"])))
    return list(orders.values())


def load_orders(path: str) -> list[Order]:
    with open(path, newline="", encoding="utf-8") as file:
        return parse_rows(list(csv.DictReader(file)))
