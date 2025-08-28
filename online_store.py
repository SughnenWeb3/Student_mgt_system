store = {
    "Football": {"price": 50, "quantity": 10},
    "Jersey": {"price": 30, "quantity": 15},
    "Boots": {"price": 80, "quantity": 5}
}


def add_product(store_dict, name, price, quantity):
    if name in store_dict:
        print(f"Product '{name}' already exists.")
    else:
        store_dict[name] = {"price": price, "quantity": quantity}
        print(f" Product '{name}' added successfully.")


def update_stock(store_dict, name, quantity):
    if name not in store_dict:
        print(f" Product '{name}' does not exist.")
    else:
        store_dict[name]["quantity"] += quantity
        print(f" Stock updated for '{name}'. New quantity: {store_dict[name]['quantity']}")


def sell_product(store_dict, name, quantity):
    if name not in store_dict:
        print(f" Product '{name}' does not exist.")
    elif store_dict[name]["quantity"] < quantity:
        print(f" Not enough stock for '{name}'. Only {store_dict[name]['quantity']} left.")
    else:
        store_dict[name]["quantity"] -= quantity
        total_price = store_dict[name]["price"] * quantity
        print(f" Sold {quantity} '{name}' for ${total_price}.")


add_product(store, "Gloves", 20, 12)      
update_stock(store, "Boots", 3)           
sell_product(store, "Football", 2) 
