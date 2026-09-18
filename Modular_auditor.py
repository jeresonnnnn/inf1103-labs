def get_valid_input():
    user_input = input("Enter stock value (or type 'quit' to end system): ")

    if user_input == "quit":
        return "quit"

    if user_input.isdigit():
        value = int(user_input)
        if value < 0:
            print ("Error! Negative number is not a valid entry. Please try again!")
            return None
        return value
    else:
        print(f"Error! '{user_input}' is not a valid entry. Please try again!")
        return None

def process_delivery(current_total, new_total):
    new_delivery = current_total + new_total
    return new_delivery

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("\n--- Delivery Report ---")
    print(f"Total deliveries processed: {total_units}")
    print(f"Number of Failed/Rejected entries: {failed_attempts}")

def main():
    inventory = 0
    failed_entries = 0
    delivery_count = 0

    while True :
        input = get_valid_input()

        if input == "quit":
          break

        if input is None:
            failed_entries += 1
            continue

        inventory = process_delivery(inventory, input)
        delivery_tax = calculate_tax(input)
        delivery_count += 1

        print(f"Accepted. Delivery: {input} units | Tax on this delivery: {delivery_tax}")
        print(f"Running total inventory: {inventory}")

    generate_report(delivery_count, failed_entries)
    
main()