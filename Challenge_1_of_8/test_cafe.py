import unittest
from unittest.mock import patch

import cafe
import menu_repository


class CafeTests(unittest.TestCase):
    def setUp(self):
        menu_repository.menu_items.clear()

    def test_add_read_delete(self):
        menu_repository.add_item_to_menu('1', 'Soup', 'Lunch', 'Beans', '4.50')
        self.assertEqual(menu_repository.order_item_from_menu('1')[0].item_name, 'Soup')
        self.assertTrue(menu_repository.delete_item_from_menu('1'))
        self.assertEqual(menu_repository.menu_items, [])

    def test_lookup_uses_selected_order(self):
        menu_repository.add_item_to_menu('1', 'Soup', 'Lunch', 'Beans', '4.50')
        with patch('builtins.input', side_effect=['2', '1', '5']), patch('builtins.print') as output:
            cafe.main()
        self.assertIn('#1 is a Soup: $4.50', str(output.call_args_list))
