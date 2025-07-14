

def main_menu():
    print("Welcome to the Chicken Project")
    print("1. View All Chickens")
    print("2. Add New Chicken")
    print("3. Update Chicken")
    print("4. Remove Chicken")
    print("5. Exit")
    choice = input("Please enter your choice (1-5): ")
    return choice

def view_chicken(choice):
    if choice == "1":
        print("Viewing all chickens...")
    else:
        print("Invalid choice. Please select a valid option.")

def add_chicken(choice):
    if choice == "2":
        print("Adding a new chicken...")
        chicken_name = input("Enter the name of the chicken: ")
        chicken_breed = input("Enter the breed of the chicken: ")
        chicken_age = input("Enter the age of the chicken: ")
        chicken_birthday = input("Enter the birthday of the chicken (YYYY-MM-DD): ")
        
        print(f"Chicken '{chicken_name}' added successfully.")
    else:
        print("Invalid choice. Please select a valid option.")