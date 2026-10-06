from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    unit_price: float
    quantity: int


@dataclass
class Order:
    order_id: str
    customer: str
    cpf: str
    items: list[Item] = field(default_factory=list)
