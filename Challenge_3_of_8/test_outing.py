
import unittest
import pytest
import outing_respitory


class ChallengeThreeTests(unittest.TestCase):

    def test_listing_all_items(self):
        # Arrange
        # Act
        actual = len(outing_respitory.list_all_events())
        expected = 1

        # Assert
        self.assertEqual(expected, actual)

    def test_adding_events_to_the_list(self):
        # Arrange
        self.outing_type = "GOLF"
        self.outing_cost_ind = 50
        self.outing_date = "1/1/18"
        self.outing_attendance = 5

        # Act
        outing_respitory.add_event(self.outing_type, self.outing_cost_ind, self.outing_date, self.outing_attendance)
        actual = len(outing_respitory.outing_list)
        expected = 1

        # Assert
        self.assertEqual(expected, actual)

    def test_calc_of_all_items(self):
        # Arrange
        # Act
        outing_respitory.calc_overall()
        actual = outing_respitory.calc_overall()
        expected = 250.0

        # Assert
        self.assertEqual(expected, actual)

    def test_calc_of_each_item_type(self):
        # Arrange
        self.outing_type = "GOLF"

        # Act
        actual = outing_respitory.calc_by_type(self.outing_type) 
        expected = 250.0

        # Assert
        self.assertEqual(expected, actual)
