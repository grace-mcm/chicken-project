from main_menu import main_menu, view_chicken, add_chicken, update_chicken, remove_chicken

def run_app():
    while True:
        choice = main_menu()
        
        if choice == "1":
            view_chicken(choice)
        elif choice == "2":
            add_chicken(choice)
        elif choice == "3":
            update_chicken(choice)
        elif choice == "4":
            remove_chicken(choice)
        elif choice == "5":
            print("Exiting the Chicken Project. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

run_app()