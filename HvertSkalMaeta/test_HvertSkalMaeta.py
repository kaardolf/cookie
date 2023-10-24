"""
separate test file for pytest
pytest recursively discovers all the files with test* and runs the
assert statements/function in them
"""

__author__ = "Kirsten Ardolf"


import sys
from HvertSkalMaeta import determine_contestant_location


def test_determine_contestant_location() -> None:
    """Test HvertSkalMaeta.py answer function.
    """
    assert determine_contestant_location("Reykjavik") == "Reykjavik"
    assert determine_contestant_location("Kopavogur") == "Reykjavik"
    assert determine_contestant_location("Hafnarfjordur") == "Reykjavik"
    assert determine_contestant_location("Reykjanesbaer") == "Reykjavik"
    assert determine_contestant_location("Akureyri") == "Akureyri"
    assert determine_contestant_location("Gardabaer") == "Reykjavik"
    print('all test casses passed...', file=sys.stderr)


if __name__ == "__main__":
    # Don't need to call test_answer() if we use pytest
    test_determine_contestant_location()
