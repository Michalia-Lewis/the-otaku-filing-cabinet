import unittest
import subprocess
import re
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import otaku_filing_cabinet

# lambda function to make feedback messages easier to read
common_msg = lambda msg, expected, actual: f"{msg}\nExpected: {expected}\nActual: {actual}"

clean_spaces = lambda string: re.sub(r"\s+", "", string)

def lines_to_set(string: str) -> set:
    """Converts a string with newlines to a set of lines"""
    return set([clean_spaces(line) for line in string.splitlines()])


class TestOtakuFilingCabinet(unittest.TestCase):
    def test_load_shows(self) -> None:
        """Test load shows with a smaller anime show file"""
        show_catalog = otaku_filing_cabinet.load_shows("test_data/test_anime_ratings_short.dat")
        self.assertEqual(
            show_catalog,
            {
                "Mob Psycho 100": (487, "psychic"),
                "Erased": (366, "mystery"),
                "Yuri!!! on Ice": (255, "sports"),
                "Parasyte": (612, "horror"),
                "Toradora!": (301, "romance"),
                "Samurai Champloo": (720, "action"),
                "The Devil is a Part-Timer!": (188, "comedy"),
                "Noragami": (542, "supernatural"),
                "Violet Evergarden": (931, "drama"),
                "Komi Can't Communicate": (404, "slice-of-life"),
            }
        )


    def test_get_new_show_from_user(self) -> None:
        
        user_catalog_tuple = otaku_filing_cabinet.get_new_show_from_user()
        self.assertEqal()