import json
import os

from Product import Product
from Inventory import inventory

def load_inventory(filename="inventory.json"):
    inventory = inventory()
    if not os.path.exists(filename):
        return inventory
    try:
        with open(filename, "r") as f:
            for item in json.load(f):
                inventory.add_product(Product.from_dict(item))
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Warning: could not fully load {filename} ({e}).")
    return inventory

def save_inventory(inventory, filename="inventory.json"):
    with open(filename, "w") as f:
        json.dump([p.to_dict() for p in inventory.get_products()], f, indent=4)
    print(f"Inventory saved to {filename}.")