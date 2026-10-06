import os
import platform
from datetime import datetime, timezone

import roberty_code as roberty

from store.loader import load_orders
from store.report import build_report, summarize

CSV_PATH = "data/orders.csv"


def print_roberty_context(robot) -> None:
    print("=== Roberty context ===")
    print(f"Running on Roberty: {robot.is_roberty}")
    print(f"Environment: {robot.environment}")
    print(f"Trigger: {robot.trigger}")
    for key, name in robot.ENV_VARS.items():
        print(f"  {key} ({name}): {os.environ.get(name)}")


def print_runtime_info() -> None:
    print("=== Runtime ===")
    print(f"Python: {platform.python_version()} on {platform.system()} {platform.release()}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Started at: {datetime.now(timezone.utc).isoformat()}")


def main(robot) -> dict:
    print_roberty_context(robot)
    print_runtime_info()

    print(f"=== Orders from {CSV_PATH} ===")
    orders = load_orders(CSV_PATH)
    print(build_report(orders))

    summary = summarize(orders)
    print(f"Grand total: R$ {summary['grandTotal']:.2f}")
    print("Writing summary as the execution result")
    return summary


if __name__ == "__main__":
    roberty.run(main)
