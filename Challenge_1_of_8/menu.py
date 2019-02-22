# POPO File


class Menu:

    def __init__(self, meal_num, item_name, item_description, item_ingredients, price):
        self.meal_num = meal_num
        self.item_name = item_name
        self.item_description = item_description
        self.item_ingredients = item_ingredients
        self.price = price

    def __repr__(self):
        return self.item_name
