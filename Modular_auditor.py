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
        
while True :
    user_input = get_valid_input()

    if user_input == "quit":
          break
    