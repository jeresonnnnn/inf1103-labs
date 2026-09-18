inventory = 0
failed_entries = 0

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
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

while True :
    user_input = get_valid_input()

    if user_input == "quit":
          break
    