import unittest

from store.calculator import shipping, total
from store.models import Item, Order


def make_order(price: float) -> Order:
    return Order("1", "Test", "529.982.247-25", [Item("Thing", price, 1)])


class CalculatorTest(unittest.TestCase):
    def test_small_order_pays_shipping(self):
        self.assertEqual(shipping(make_order(50.0)), 15.0)

    def test_order_above_threshold_has_free_shipping(self):
        self.assertEqual(shipping(make_order(250.0)), 0.0)

    def test_total_includes_tax_and_shipping(self):
        self.assertEqual(total(make_order(100.0)), 125.0)


if __name__ == "__main__":
    unittest.main()
