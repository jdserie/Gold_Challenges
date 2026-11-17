import unittest
from unittest.mock import patch

import claim
import ClaimRepository


class ClaimsTests(unittest.TestCase):
    def setUp(self):
        ClaimRepository.claim_list.clear()
        for number in ('1', '2'):
            ClaimRepository.enter_claims_list(number, 'car', 'Repair', '150.75', '1/1/18', '1/2/18', True)

    def test_confirm_removes_only_oldest_claim(self):
        with patch('builtins.input', side_effect=['2', 'y', '4']), patch('builtins.print'):
            claim.main()
        self.assertEqual([entry.claimID for entry in ClaimRepository.claim_list], ['2'])

    def test_cancel_preserves_queue(self):
        with patch('builtins.input', side_effect=['2', 'n', '4']), patch('builtins.print'):
            claim.main()
        self.assertEqual([entry.claimID for entry in ClaimRepository.claim_list], ['1', '2'])
