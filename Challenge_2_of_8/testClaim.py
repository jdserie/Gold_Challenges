
import unittest
import pytest
import ClaimRepository

class ChallengeTwoTests(unittest.TestCase):

    def test_adding_items_to_list(self):
        # Arrange
        self.claimID = "1"
        self.claimType = "car"
        self.description = "Engine failure."
        self.claimAmount = "150.75"
        self.dateOfIncident = "1/01/18"
        self.dateOfClaim = "1/02/18"
        self.isValid = True

        # Act 
        ClaimRepository.enter_claims_list(self.claimID, self.claimType, self.description, self.claimAmount, self.dateOfIncident, self.dateOfClaim, self.isValid)
        actual = len(ClaimRepository.claim_list)
        expected = 1

        # Assert
        self.assertEqual(expected, actual)

    def test_justifying_queue_cycle(self):
        # Arrange
        self.isValid = True

        # Act
        ClaimRepository.justify_claims(self.isValid)
        actual = len(ClaimRepository.claim_list)
        expected = 1

        # Assert
        self.assertEqual(expected, actual)

    def test_calling_all_list_items(self):
        # Arrange
        self.claimID = "1"
        self.claimType = "car"
        self.description = "Engine failure."
        self.claimAmount = "150.75"
        self.dateOfIncident = "1/01/18"
        self.dateOfClaim = "1/02/18"
        self.isValid = True

        # Act
        ClaimRepository.list_all_claims(self.claimID, self.claimType, self.description, self.claimAmount, self.dateOfIncident, self.dateOfClaim, self.isValid)
        actual = len(ClaimRepository.claim_list)
        expected = 1

        # Assert
        self.assertEqual(expected, actual)
