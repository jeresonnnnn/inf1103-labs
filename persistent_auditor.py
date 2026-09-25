def count_items(list):
    count = 0
    for item in list:
        count = count + 1
    return count

def load_inventory(filename="orders.txt"):
    orders = []
    with open(filename, "a") as f:
        pass

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue

            parts = line.split(",")

            if count_items(parts) == 3:
                order_id = int(parts[0].strip())
                product_name = parts[1].strip()
                quantity = int(parts[2].strip())

                orders.append([order_id, product_name, quantity])
    return orders

def save_inventory(orders, filename="orders.txt"):
     with open(filename, "w") as f:
          for order in orders:
               order_id = order[0]
               product_name = order[1]
               quantity = order[2]
               f.write(str(order_id) + "," + product_name + "," + str(quantity) + "\n")

def get_order_id(orders):
    if count_items(orders) == 0:
        return 1001

    highest_id = orders[0][0]

    for order in orders:
        if order[0] > highest_id:
            highest_id = order[0]
    return highest_id + 1

def display_order(orders):
     print("\nCurrent Orders:\n")

     for order in orders:
          order_id = order[0]
          product_name = order[1]
          quantity = order[2]
          print(str(order_id) + ", " + product_name + ", " + str(quantity))

def main():
    orders = load_inventory()

    display_order(orders)

    while True:
        user_input = input("\nEnter Product Name (or type 'quit' to end): ")
        user_input = user_input.strip()

        if user_input == "quit":
            break

        if user_input == "":
            print("Error! Product name cannot be empty. Please try again!")
            continue

        quantity_input = input("Enter Quantity: ")
        quantity_input = quantity_input.strip()

        if not quantity_input.isdigit():
            print("Error! '" + quantity_input + "' is not a valid quantity. Please try again!")
            continue

        quantity = int(quantity_input)
        new_id = get_order_id(orders)

        orders.append([new_id, user_input, quantity])

        print("\nNew order Added:")
        print(str(new_id) + ", " + user_input + ", " + str(quantity))

    save_inventory(orders)
    print("\nOrder successfully saved to orders.txt")


main()