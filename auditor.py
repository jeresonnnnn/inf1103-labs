inventory = 0
failed_entries = 0

while True :
    user_input = input("Enter stock value (or type 'quit' to end system): ")

    if user_input == "quit":
        break

    if user_input.isdigit():
        stock_value = int(user_input)

        if stock_value < 0:
            print ("Error! Negative number is not a valid entry. Please try again!")
            failed_entries + 1
            continue

        inventory += stock_value
        print(f"Entry Accepted. Current value now is: {inventory}")

        if inventory > 500:
            print(f"ALERT! ALERT! Total stock value {inventory} has exceeded 500!")
            print("SHUTTING SYSTEM DOWN NOW!")
            break
        elif inventory == 500:
            print("Total stock value has reacheed 500 unit. Limit reached!")
            print("Stopping system now.")
            break
        else:
            pass

    else:
                print(f"Error! '{user_input}' is not a valid entry. Please try again!")
                failed_entries += 1
                continue

print("\n-----Inventory Report-----")
print(f"Total units processed: {inventory}")
print(f"Number of Failed/Rejected entries: {failed_entries}")    