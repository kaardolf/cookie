"""unittesting HvertSkalMaeta.py solution
"""

__author__ = "Kirsten Ardolf"

import unittest
from HvertSkalMaeta import determine_contestant_location


class TestHvertSkalMaeta(unittest.TestCase):
    """ Test HvertSkalMaeta.py solution
    """
    def test1_determine_contestant_location(self) -> None:
        data = "Reykjavik"
        self.assertEqual(determine_contestant_location(data), "Reykjavik")

    def test2_determine_contestant_location(self) -> None:
        data = "Kopavogur"
        self.assertEqual(determine_contestant_location(data), "Reykjavik")

    def test3_determine_contestant_location(self) -> None:
        data = "Hafnarfjordur"
        self.assertEqual(determine_contestant_location(data), "Reykjavik")

    def test4_determine_contestant_location(self) -> None:
        data = "Reykjanesbaer"
        self.assertEqual(determine_contestant_location(data), "Reykjavik")

    def test5_determine_contestant_location(self) -> None:
        data = "Akureyri"
        self.assertEqual(determine_contestant_location(data), "Akureyri")

    def test6_determine_contestant_location(self) -> None:
        data = "Gardabaer"
        self.assertEqual(determine_contestant_location(data), "Reykjavik")
