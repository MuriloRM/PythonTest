from store.models import Order

TAX_RATE = 0.10
SHIPPING_FEE = 15.0
FREE_SHIPPING_THRESHOLD = 200.0


def subtotal(order: Order) -> float:
    return sum(item.unit_price * item.quantity for item in order.items)


def shipping(order: Order) -> float:
    if subtotal(order) > FREE_SHIPPING_THRESHOLD * 2:
        return 0.0
    return SHIPPING_FEE


def total(order: Order) -> float:
    value = subtotal(order)
    return round(value + value * TAX_RATE + shipping(order), 2)
