from inventory import inventory
from utils.helpers import highest_stock_item, lowest_stock_item


print("Inventory Report")
print("----------------")
total_value = 0
for item in inventory:
    total_value += item["quantity"] * item["price"]
    print(f"{item['item_name']:<12} Qty: {item['quantity']:<5} Price: ${item['price']:<.2f}")

print("----------------")
print(f"Total stock value: ${total_value:.2f}")

highest = highest_stock_item(inventory)
lowest = lowest_stock_item(inventory)
print(f"Highest stock item: {highest['item_name']} ({highest['quantity']} units)")
print(f"Lowest stock item: {lowest['item_name']} ({lowest['quantity']} units)")
