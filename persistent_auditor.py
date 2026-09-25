def count_items(list):
    count = 0
    for item in list:
        count = count + 1
        return count

def load_inventory(filename="orders.txt"):
    orders = []
    with open (filename, "a") as f:
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
                quantity = int(parts[3].strip())

                orders.append([order_id, product_name, quantity])

                return orders

def save_inventory(orders, filename="orders.txt"):
     with open(filename, "w") as f:
          for order in orders:
               order_id = order[0]
               product_name = order[1]
               quantity = order[2]
               f.write(str(order_id) + "," + product_name + "," + str(quantity) + "\n")
               

def main():
    orders = load_inventory()

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

main()