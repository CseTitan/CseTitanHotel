from room_data import room_menu
from customer_data import customer_menu
from organize_menu import print_center, input_center
from calc import rent_calc

if __name__ == '__main__':
    while True:
        print()
        print_center("==============================")
        print_center("=====The Titans Hotel=====")
        print_center("==============================")
        print_center("1. Manage Rooms")
        print_center("2. Manage Customers")
        print_center("3. Calculate Rent")
        print_center("0. Exit")
        print()

        choice = int(input_center("Enter your choice: "))
        if choice == 1:
            room_menu()
        elif choice == 2:
            customer_menu()
        elif choice == 3:
            rent_calc()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to exit)")
    print_center("GoodBye")
