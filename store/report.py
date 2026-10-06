from store.calculator import shipping, subtotal, total
from store.models import Order


def build_report(orders: list[Order]) -> str:
    lines = []
    for order in orders:
        lines.append(
            f"#{order.order_id} {order.customer:<10} "
            f"subtotal R$ {subtotal(order):>8.2f}  "
            f"shipping R$ {shipping(order):>6.2f}  "
            f"total R$ {total(order):>8.2f}"
        )
    return "\n".join(lines)


def summarize(orders: list[Order]) -> dict:
    return {
        "orderCount": len(orders),
        "grandTotal": round(sum(total(order) for order in orders), 2),
        "orders": [{"orderId": order.order_id, "customer": order.customer, "total": total(order)} for order in orders],
    }
