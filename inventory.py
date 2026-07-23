"""Inventory data module for the inventory application.

Provides an Item dataclass and sample inventory data.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    """Represents an inventory item with name, quantity, and price.

    Attributes:
        item_name: The name of the item.
        quantity: The number of units in stock.
        price: The unit price of the item.
    """
    item_name: str
    quantity: int
    price: float


# Sample inventory dataset for testing and demonstration.
inventory: List[Item] = [
    Item(item_name="Laptop", quantity=10, price=750.00),
    Item(item_name="Mouse", quantity=50, price=15.50),
    Item(item_name="Keyboard", quantity=30, price=45.00),
    Item(item_name="Monitor", quantity=15, price=200.00),
    Item(item_name="Headset", quantity=25, price=60.00),
]
