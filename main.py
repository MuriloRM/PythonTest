import roberty_code as roberty

from store.loader import load_orders, parse_rows
from store.models import Order
from store.report import build_report, summarize

DEFAULT_CSV_PATH = "data/orders.csv"


def read_orders(robot) -> list[Order]:
    rows = robot.input("orders")
    if rows:
        print(f"Loaded {len(rows)} rows from the 'orders' input")
        return parse_rows(rows)
    csv_path = robot.input("csvPath", DEFAULT_CSV_PATH)
    print(f"No 'orders' input, reading {csv_path}")
    return load_orders(csv_path)


def main(robot) -> dict:
    print(f"Running on Roberty: {robot.is_roberty}")
    print(f"Environment: {robot.environment} | Trigger: {robot.trigger}")
    print(f"Inputs received: {robot.inputs()}")

    orders = read_orders(robot)
    print(build_report(orders))

    summary = summarize(orders)
    if summary["invalidCpfOrders"] and robot.input("failOnInvalidCpf", False):
        raise ValueError(f"Orders with invalid CPF: {summary['invalidCpfOrders']}")

    print("Writing summary as the execution result")
    return summary


if __name__ == "__main__":
    roberty.run(main)
