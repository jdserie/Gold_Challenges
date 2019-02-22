import unittest
import menu_repository
import pytest

'''
It is NOT testing cafe, despite the name
It is testing the menu_repository
'''


class TestsMenu(unittest.TestCase):

    def test_add_menu_item_function(self):
        # Arrange
        self.meal_num = 1
        self.item_name = "food"
        self.item_description = "yum"
        self.item_ingredients = "meat"
        self.price = 1
        # Act
        menu_repository.add_item_to_menu(self.meal_num, self.item_name, self.item_description, self.item_ingredients, self.price)
        actual = len(menu_repository.menu_items)
        expected = 1
        # Assert
        self.assertEqual(expected, actual)

    def test_ordering_items_from_the_menu(self):
        # Arrange
        self.meal_num = 1

        # Act
        menu_repository.order_item_from_menu(self.meal_num)
        actual = len(menu_repository.menu_items)
        expected = 1

        # Assert
        self.assertEqual(expected, actual)

    def test_listing_all_items(self):
        # Arrange
        self.item_name = "food"

        # Act
        menu_repository.list_menu_all_items(self.item_name)
        actual = len(menu_repository.menu_items)
        expected = 1

        # Assert
        self.assertEqual(expected, actual)

    def test_deleting_meal_from_the_menu(self):
        # Arrange
        self.meal_num = 1
        self.item_name = "food"
        self.item_description = "yum"
        self.item_ingredients = "meat"
        self.price = 1


        # Act
        menu_repository.add_item_to_menu(self.meal_num, self.item_name, self.item_description, self.item_ingredients, self.price)
        menu_repository.delete_item_from_menu
        self.assertTrue(menu_repository.delete_item_from_menu(self.meal_num))
