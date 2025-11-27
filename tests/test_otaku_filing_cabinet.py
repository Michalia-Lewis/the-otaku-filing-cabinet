import unittest
import io
import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import otaku_filing_cabinet

# Test data for filter and print_shows tests
TEST_CATALOG = [
    ("Death Parade", 643, "psychological"),
    ("Steins;Gate", 100, "scifi"),
    ("Akira", 1000, "cyberpunk"),
    ("Fruits Basket", 774, "romance"),
    ("Mob Psycho 100", 482, "comedy"),
    ("Naruto", 456, "action"),
    ("Death Note", 999, "psychological"),
    ("Your Name", 50, "drama"),
]

# Test data for print_shows tests (dict format)
TEST_CATALOG_DICT = {
    "Death Parade": (643, "psychological"),
    "Steins;Gate": (100, "scifi"),
    "Akira": (1000, "cyberpunk"),
    "Fruits Basket": (774, "romance"),
    "Mob Psycho 100": (482, "comedy"),
    "Naruto": (456, "action"),
    "Death Note": (999, "psychological"),
    "Your Name": (50, "drama"),
}

class TestOtakuFilingCabinet(unittest.TestCase):
    def test_box(self) -> None:
        """Test the box function"""
        boxed_text = otaku_filing_cabinet.box("Testing 123")
        lines = boxed_text.split('\n')

        # Check structure
        self.assertEqual(len(lines), 3)  # top border + 1 line + bottom border
        self.assertEqual(lines[0], "=" * 60)  # top border
        self.assertEqual(lines[-1], "=" * 60)  # bottom border
        self.assertIn("Testing 123", lines[1])  # content is there

    def test_load_shows(self) -> None:
        """Test the load_shows function with a smaller anime show file"""
        show_catalog = otaku_filing_cabinet.load_shows("tests/test_data/test_anime_ratings_short.dat")
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

    def test_load_shows_empty_file(self) -> None:
        """Test load_shows with an empty file"""
        show_catalog = otaku_filing_cabinet.load_shows("tests/test_data/test_empty.dat")
        self.assertEqual(show_catalog, {})
    
    def test_load_shows_invalid_rating(self) -> None:
        """Test load_shows skips entries with non-numeric ratings"""
        show_catalog = otaku_filing_cabinet.load_shows("tests/test_data/test_invalid_rating.dat")
        self.assertNotIn("Bad Show", show_catalog)
    
    def test_clean_title(self) -> None:
        """Test clean_title function"""
        self.assertEqual(otaku_filing_cabinet.clean_title("death note  "), "Death Note")
        self.assertEqual(otaku_filing_cabinet.clean_title("    your lie in april    "), "Your Lie In April")
        self.assertEqual(otaku_filing_cabinet.clean_title("DeMoN sLaYeR"), "Demon Slayer")
        self.assertEqual(otaku_filing_cabinet.clean_title("SPY X FAMILY"), "Spy X Family")
        self.assertEqual(otaku_filing_cabinet.clean_title("STEINS;GATE"), "Steins;Gate")
        self.assertEqual(otaku_filing_cabinet.clean_title(""), "")
    
    def test_convert_rating(self) -> None:
        """Test convert_rating function"""
        self.assertEqual(otaku_filing_cabinet.convert_rating(1), "⭐")
        self.assertEqual(otaku_filing_cabinet.convert_rating(4), "⭐⭐")
        self.assertEqual(otaku_filing_cabinet.convert_rating(5), "⭐⭐⭐")
        self.assertEqual(otaku_filing_cabinet.convert_rating(8), "⭐⭐⭐⭐")
        self.assertEqual(otaku_filing_cabinet.convert_rating(10), "⭐⭐⭐⭐⭐")
        self.assertEqual(otaku_filing_cabinet.convert_rating(-10), "⭐")
        self.assertEqual(otaku_filing_cabinet.convert_rating(1000000), "⭐⭐⭐⭐⭐")
    
    def test_check_filter_no_filter(self) -> None:
        """Tests the check_filter function with no filter."""
        for show in TEST_CATALOG:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, ""))
    
    def test_check_filter_show_title_filter(self) -> None:
        """Tests the check_filter function with a show title filter."""
        for show in [x for x in TEST_CATALOG if 'death' in x[0].lower()]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "death"))
        for show in [x for x in TEST_CATALOG if 'fruit' in x[0].lower()]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "fruit"))

    def test_check_filter_show_rating_filter(self) -> None:
        """Tests the check_filter function with a show rating filter."""
        for show in [x for x in TEST_CATALOG if x[1] >= 500]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, ">= 500"))
        for show in [x for x in TEST_CATALOG if x[1] < 500]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "< 500"))
        for show in [x for x in TEST_CATALOG if x[1] == 999]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "= 999"))
        for show in [x for x in TEST_CATALOG if x[1] != 643]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "!= 643"))
        for show in [x for x in TEST_CATALOG if x[1] > 50]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "> 50"))
        for show in [x for x in TEST_CATALOG if x[1] <= 100]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "<= 100"))

    def test_check_filter_invalid_operator(self) -> None:
        """Tests the check_filter function with invalid operators."""
        self.assertFalse(otaku_filing_cabinet.check_filter(("Akira", 1000, "cyberpunk"), ">> 500"))
        self.assertFalse(otaku_filing_cabinet.check_filter(("Naruto", 456, "action"), "<> 100"))
    
    def test_check_filter_genre(self) -> None:
        """Tests the check_filter function with a genre filter."""
        for show in [x for x in TEST_CATALOG if x[2] == "psychological"]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "psychological"))
        for show in [x for x in TEST_CATALOG if x[2] == "romance"]:
            self.assertTrue(otaku_filing_cabinet.check_filter(show, "romance"))

    def test_check_filter_case_insensitive(self) -> None:
        """Tests the check_filter function is case insensitive."""
        self.assertTrue(otaku_filing_cabinet.check_filter(("Mob Psycho 100", 482, "comedy"), "mOb PsYcHo"))
        self.assertTrue(otaku_filing_cabinet.check_filter(("Naruto", 456, "action"), "ACTION"))      
    
    def test_print_shows(self) -> None:
        """Test print_shows function"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        otaku_filing_cabinet.print_shows({"Naruto": (456, "action")})
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Naruto", output)
        self.assertIn("action", output)
        self.assertIn("⭐", output)

    def test_print_shows_empty_dict(self) -> None:
        """Test print_shows with empty dictionary"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        otaku_filing_cabinet.print_shows({})
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Zannen!", output)
    
    def test_print_shows_no_matches(self) -> None:
        """Test print_shows with filter that matches nothing"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        otaku_filing_cabinet.print_shows(TEST_CATALOG_DICT, "xyz")
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Gomen!", output)
    
    def test_print_shows_filter(self) -> None:
        """Test print_shows with filter"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        otaku_filing_cabinet.print_shows(TEST_CATALOG_DICT, "death")
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Death Parade", output)
        self.assertIn("Death Note", output)
        self.assertNotIn("Naruto", output)
        self.assertNotIn("Akira", output)
    
    def test_update_rating_show_not_found(self) -> None:
        """Test update_rating with show not in catalog"""
        catalog = {"Naruto": (456, "action")}
        result = otaku_filing_cabinet.update_rating(catalog, "Akira")
        
        self.assertFalse(result)

    def test_update_rating_success(self) -> None:
        """Test update_rating successfully updates rating"""
        # Create a test catalog with one show
        catalog = {"Naruto": (456, "action")}
        
        # Mock input() so it returns '999' instead of waiting for user
        # This simulates the user typing '999' when prompted for new rating
        with patch('builtins.input', return_value='999'):
            # Call the function — it will use our fake input
            result = otaku_filing_cabinet.update_rating(catalog, "Naruto")
        
        # Check that function returned True (success)
        self.assertTrue(result)
        
        # Check that the catalog was actually updated
        # Rating should be 999, genre should still be "action"
        self.assertEqual(catalog["Naruto"], (999, "action"))
    
    def test_save_shows(self) -> None:
        """Test save_shows writes correct format to file"""
        otaku_filing_cabinet.save_shows(TEST_CATALOG_DICT, "test_save.dat")

        file = open("anime_shows_list/test_save.dat", "r")
        content = file.read()
        file.close()
        
        self.assertIn("Death Parade::643::psychological", content)
        self.assertIn("Naruto::456::action", content)
        self.assertIn("Your Name::50::drama", content)

if __name__ == '__main__':
    unittest.main()
