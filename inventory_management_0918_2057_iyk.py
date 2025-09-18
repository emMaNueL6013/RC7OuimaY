# 代码生成时间: 2025-09-18 20:57:59
from bottle import route, run, request, response, template

# 库存管理系统
class InventoryManager:
    """Manages inventory of items."""
    def __init__(self):
        # Initialize the inventory with some items
        self.inventory = {"item1": 10, "item2": 20, "item3": 30}

    def add_item(self, item, quantity):
        """Adds a specified quantity of an item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        """Removes a specified quantity of an item from the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if item in self.inventory:
            if self.inventory[item] < quantity:
                raise ValueError("Not enough inventory.")
            self.inventory[item] -= quantity
            if self.inventory[item] == 0:
                del self.inventory[item]
        else:
            raise KeyError(f"Item {item} not found in inventory.")

    def get_inventory(self):
        """Returns the current state of the inventory."""
        return self.inventory

# Instantiate the InventoryManager
inventory_manager = InventoryManager()

# Define Bottle routes
@route('/add_item', method='POST')
def add_item():
    item = request.json.get('item')
    quantity = request.json.get('quantity')
    try:
        inventory_manager.add_item(item, quantity)
        response.status = 200
        return {"message": "Item added successfully."}
    except (ValueError, KeyError) as e:
        response.status = 400
        return {"message": str(e)}

@route('/remove_item', method='POST')
def remove_item():
    item = request.json.get('item')
    quantity = request.json.get('quantity')
    try:
        inventory_manager.remove_item(item, quantity)
        response.status = 200
        return {"message": "Item removed successfully."}
    except (ValueError, KeyError) as e:
        response.status = 400
        return {"message": str(e)}

@route('/get_inventory', method='GET')
def get_inventory():
    return inventory_manager.get_inventory()

# Run the Bottle application
run(host='localhost', port=8080)