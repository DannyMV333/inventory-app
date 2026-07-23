"""Main application script for the inventory management system.

Reads inventory data and displays a report of stock values,
including total stock value, total item count, and average price.
"""
from statistics import mean
from typing import List

from inventory import Item, inventory
from utils.helpers import highest_stock_item, lowest_stock_item

BOX_W = 42


def print_separator(char: str = "=") -> None:
    """Print a horizontal separator line."""
    print(char * BOX_W)


def print_column_headers() -> None:
    """Print the column headers for the inventory table."""
    print(f"{'Item':<12} {'Qty':<6} {'Price':>8} {'Value':>10}")
    print("-" * BOX_W)


def print_item_row(item: Item) -> float:
    """Print a single inventory item row and return its line value."""
    value = item.quantity * item.price
    print(f"{item.item_name:<12} {item.quantity:<6} ${item.price:>6.2f} ${value:>7.2f}")
    return value


def print_summary(total_value: float, prices: List[float]) -> None:
    """Print the summary section of the inventory report."""
    print_separator()
    print(f"{'Total stock value:':<25} ${total_value:>9.2f}")
    print(f"{'Total items:':<25} {len(prices):>10}")
    print(f"{'Average price:':<25} ${mean(prices):>9.2f}")
    print_separator()


def print_extremes(inv: List[Item]) -> None:
    """Print the highest and lowest stock items."""
    highest = highest_stock_item(inv)
    lowest = lowest_stock_item(inv)
    print(f"Highest stock: {highest.item_name} ({highest.quantity} units)")
    print(f"Lowest stock:  {lowest.item_name} ({lowest.quantity} units)")
    print_separator()


def run_report() -> None:
    """Generate and display the full inventory report."""
    print_separator()
    print(f"{'INVENTORY REPORT':^{BOX_W}}")
    print_separator()
    print_column_headers()

    total_value = 0.0
    prices: List[float] = []

    for item in inventory:
        value = print_item_row(item)
        total_value += value
        prices.append(item.price)

    print_summary(total_value, prices)
    print_extremes(inventory)


if __name__ == "__main__":
    run_report()
