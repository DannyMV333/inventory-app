"""Helper functions for inventory analysis."""
from typing import List, Optional

from inventory import Item


def highest_stock_item(inventory: List[Item]) -> Optional[Item]:
    """Return the item with the highest quantity in stock.

    Returns None if the inventory is empty.
    """
    if not inventory:
        return None
    return max(inventory, key=lambda item: item.quantity)


def lowest_stock_item(inventory: List[Item]) -> Optional[Item]:
    """Return the item with the lowest quantity in stock.

    Returns None if the inventory is empty.
    """
    if not inventory:
        return None
    return min(inventory, key=lambda item: item.quantity)
