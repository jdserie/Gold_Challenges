import unittest
from unittest.mock import patch

import outing
import outing_respitory


class OutingTests(unittest.TestCase):
    def setUp(self):
        outing_respitory.outing_list.clear()

    def test_totals(self):
        outing_respitory.add_event('GOLF', 50, '1/1/18', 5)
        outing_respitory.add_event('CONCERT', 20, '2/1/18', 2)
        self.assertEqual(len(outing_respitory.list_all_events()), 2)
        self.assertEqual(outing_respitory.calc_by_type('GOLF'), 250)
        self.assertEqual(outing_respitory.calc_overall(), 290)

    def test_bad_cost_does_not_add_an_outing(self):
        with patch('builtins.input', side_effect=['2', 'golf', 'ten', '4']), patch('builtins.print'):
            outing.main()
        self.assertEqual(outing_respitory.list_all_events(), [])
