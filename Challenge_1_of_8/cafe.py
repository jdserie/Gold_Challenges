# UI File

import menu_repository

while True:
    print('\nWelcome to Komodo Cafe!\n')
    user_input = input('1) Add Menu Item:\n' +
                       '2) Menu Details:\n' +
                       '3) List All Menu Items\n' +
                       '4) Delete Menu Itmes:\n' +
                       '5) Exit\n' +
                       '>')

    if user_input == '1':
        item_name = input('Enter menu item name: ')
        meal_num = input('Enter the menu item number: ')
        item_description = input('Enter a brief item description: ')
        item_ingredients = input("Enter ingredients in the menu item: ")
        price = input("Enter menu item price: ")
        menu_repository.add_item_to_menu(meal_num, item_name, item_description, item_ingredients, price)
        print("Menu item added!")
    elif user_input == '2':
        meal_num = input("Select order number: ")
        menu_items = menu_repository.order_item_from_menu(meal_num)
        for meal in menu_items:
            if meal.meal_num == meal_num:              
                print(
                f"I'll have the #{meal_num}\n" +
                f"#{meal_num} is a {item_name}: {price}\n" +
                f"Ingredients include: {item_ingredients}\n" +
                f"Meal is {item_description}\n")
                break
        else:            
            print("This is not a menu item!\n")
    elif user_input == '3':
        list_of_items = menu_repository.menu_items
        meal_length = len(list_of_items)
        if meal_length > 0:
            print(list_of_items)
        else:
            print("No Menu Items Listed!")
    elif user_input == '4':
        meal_num = input("Enter Item Number to Delete: ")
        if menu_repository.delete_item_from_menu(meal_num):
            print(f"Meal Number #{meal_num} Deleted!")
        else:
            print("Menu Item Does Not Exist!")
    elif user_input == '5':
        exit(0)
