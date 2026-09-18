inventory = 0
failed_entries = 0

def get_valid_input():
        user_input = input("Enter stock value (or type 'quit' to end system): ")
        return user_input

while True :
    user_input = get_valid_input()

    if user_input == "quit":
          break
    