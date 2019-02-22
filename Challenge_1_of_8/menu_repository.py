
import menu

'''
This Module will handle the UI
and the CRUD Functionality of the Show object
'''

# Create Read Delete

menu_items = []


# CREATE
def add_item_to_menu(meal_num, item_name, item_description, item_ingredients, price):
    s = menu.Menu(meal_num, item_name, item_description, item_ingredients, price)
    menu_items.append(s)


# READ
def order_item_from_menu(meal_num):
    return menu_items


# LIST
def list_menu_all_items(item_name):
    return menu_items


# Delete
def delete_item_from_menu(meal_num):
    for menu in menu_items:
        if meal_num == menu.meal_num:
            index = menu_items.index(menu)
            menu_items.remove(menu)
            return True
