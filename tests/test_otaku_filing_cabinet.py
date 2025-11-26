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
        """Test the load_shows function with a smaller anime show file"""
        show_catalog = otaku_filing_cabinet.load_shows("test_data/test_anime_ratings_short.dat")
        self.assertEqual(
            show_catalog,
            {
                "Mob Psycho 100": (3, "psychic"),
                "Erased": (9999, "mystery"),
                "Yuri!!! On Ice": (8, "sports"),
                "Parasyte": (666, "horror"),
                "Toradora!": (1, "romance"),
                "Samurai Champloo": (720, "action"),
                "The Devil Is A Part-Timer!": (42, "comedy"),
                "Noragami": (5, "supernatural"),
                "Violet Evergarden": (1001, "drama"),
                "Komi Can'T Communicate": (69, "slice of life")
            }
        )


    def test_load_shows_2(self) -> None:
        """Test the load_shows function with a larger anime show file"""
        show_catalog = otaku_filing_cabinet.load_shows("data/anime_ratings.dat")
        self.assertEqual(
            show_catalog,
            {
                "Tiger": (89, "sci-fi"),
                "Takopi'S Sin": (1, "suspense"),
                "Your Lie In April": (854, "drama"),
                "Kengan Ashura": (69, "action"),
                "Steins;Gate": (10, "sci-fi"),
                "Naruto": (243, "action"),
                "Yuri On Ice": (7, "sports"),
                "Chainsaw Man": (1337, "horror"),
                "Fruits Basket": (666, "romance"),
                "Kill La Kill": (4, "action"),
                "Shiki": (2, "horror"),
                "Black Clover": (305, "fantasy"),
                "Your Name": (999, "drama"),
                "Trigun": (420, "western"),
                "Sailor Moon": (5, "magical"),
                "Blue Exorcist": (22, "supernatural"),
                "Overlord": (1, "dark"),
                "Haikyuu": (787, "sports"),
                "Bungou Stray Dogs": (3, "mystery"),
                "Steamboy": (88, "steampunk"),
                "Re:Zero": (512, "isekai"),
                "Mob Psycho 100": (6, "comedy"),
                "Erased": (9001, "thriller"),
                "One Punch Man": (1000, "superhero"),
                "Toradora": (4, "romance"),
                "Made In Abyss": (777, "adventure"),
                "Soul Eater": (2, "gothic"),
                "Jujutsu Kaisen": (333, "action"),
                "Death Note": (10000, "psychological"),
                "Beastars": (12, "drama"),
                "Mushishi": (1, "slice of life"),
                "Gintama": (256, "comedy"),
                "Higurashi": (8, "horror"),
                "Code Geass": (999, "mecha"),
                "Spy X Family": (48, "family"),
                "Claymore": (3, "darkfantasy"),
                "Samurai Champloo": (511, "samurai"),
                "Parasyte": (144, "horror"),
                "Fairy Tail": (7, "fantasy"),
                "Durarara": (101, "urban"),
                "Violet Evergarden": (5, "drama"),
                "Hell'S Paradise": (37, "action"),
                "Astro Boy": (2, "classic"),
                "The Promised Neverland": (2500, "thriller"),
                "Devilman Crybaby": (13, "demon"),
                "Komi Can'T Communicate": (69, "comedy"),
                "Fire Force": (404, "action"),
                "Ranking Of Kings": (6, "fantasy"),
                "Akudama Drive": (888, "cyberpunk"),
                "Lucky Star": (1, "slice of life")
            }
        )


    def test_get_new_show_from_user(self) -> None:
        """Test to see if the get_new_show_from_user function is returning a tuple properly."""
        user_catalog_tuple = otaku_filing_cabinet.get_new_show_from_user()
        # self.assertEqal()
        pass