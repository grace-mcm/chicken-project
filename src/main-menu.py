from db_utils import (chicken_list, add_new_chicken, update_chicken, remove_chicken)

#lists all available functions in the chicken project
def main_menu():
    print("Welcome to the Chicken Project")
    print("1. View All Chickens")
    print("2. Add New Chicken")
    print("3. Update Chicken")
    print("4. Remove Chicken")
    print("5. Exit")
    choice = input("Please enter your choice (1-5): ")
    return choice

# handles user input and lists all current chicken entries
def view_chicken(choice):
    if choice == "1":
        print("Viewing all chickens...")
        chicken_list()
    else:
        print("Invalid choice. Please select a valid option.")

# handles user input for adding chickens to the database
def add_chicken(choice):
    if choice == "2":
        print("Adding a new chicken...")
        chicken_name = input("Enter the name of the chicken: ")
        chicken_breed = input("Enter the breed of the chicken: ")
        chicken_age = input("Enter the age of the chicken: ")
        chicken_birthday = input("Enter the birthday of the chicken (YYYY-MM-DD): ")
        add_new_chicken(chicken_name, chicken_breed, chicken_age, chicken_birthday)
        print(f"Chicken '{chicken_name}' added successfully.")
    else:
        print("Invalid choice. Please select a valid option.")

# handles user input for updating existing chickens in the database
def update_chicken(choice):
    if choice == "3":
        print("Updating a chicken...")
        chicken_id = input("Enter the ID of the chicken to update: ")
        chicken_name = input("Enter the new name of the chicken: ")
        chicken_breed = input("Enter the new breed of the chicken: ")
        chicken_age = input("Enter the new age of the chicken: ")
        chicken_birthday = input("Enter the new birthday of the chicken (YYYY-MM-DD): ")
        update_chicken(chicken_id, chicken_name, chicken_breed, chicken_age, chicken_birthday)
        print(f"Chicken with ID '{chicken_id}' updated successfully.")
    else:
        print("Invalid choice. Please select a valid option.")

# handles user input for removing chickens from the database
def remove_chicken(choice):
    if choice == "4":
        print("Removing a chicken...")
        chicken_id = input("Enter the ID of the chicken to remove: ")
        remove_chicken(chicken_id)
        if chicken_id:
            remove_chicken(chicken_id)
            print(f"Chicken with ID '{chicken_id}' removed successfully.")
        else:
            print("No chicken ID provided.")
    else:
        print("Invalid choice. Please select a valid option.")  

# handles user input for exiting the program
def exit_program(choice):
    if choice == "5":
        print("Exiting the program. Goodbye!")
        return True
    else:
        print("Invalid choice. Please select a valid option.")
        return False