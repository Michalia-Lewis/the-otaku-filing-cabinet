"""
Final Project: The Otaku Filing Cabinet
===========================
Course:   CS 5001
Student:  Michalia Lewis
Semester: Fall 2025

Description:
    The Otaku Filing Cabinet is a dual-catalog anime management system that allows users to:
    - Browse a curated catalog of 40+ recommended anime with ratings and genres
    - Build a personalized anime list by selecting from the catalog or adding custom entries
    - Filter both catalogs by title, genre, or rating comparisons
    - Update ratings for shows in their personal collection
    - Save their customized anime list to a file for future reference
    
    The app maintains two separate dictionaries: a read-only recommendation catalog
    and the user's personal collection, providing a complete anime tracking experience.

Acknowledgments:
    Portions of this project were developed with assistance from:
    - Claude (Anthropic) for architecture design and implementation guidance
    - ChatGPT (OpenAI) for initial concepts and debugging support
    All final implementations have been written, adapted, and verified by the author.
"""
from typing import List, Tuple, Dict
import string
import os

def box(text, width=60):
    """Creates a box with centered text for welcome/goodbye messages."""
    line = "=" * width
    lines = text.strip().split('\n')
    
    boxed = [line]
    for text_line in lines:
        centered = text_line.center(width)
        boxed.append(centered)
    boxed.append(line)
    
    return '\n'.join(boxed)

welcome_text = """
🏮WELCOME TO THE OTAKU FILING CABINET🏮

こんにちは! Welcome, anime enthusiast!

Build your perfect anime list!
40+ shows to browse, or add your own!

🆕 First time? Type 'help' for a complete guide
⚡ Quick start: Type 'list catalog' to browse!

✨Let's build your anime collection together!✨
""".strip()


goodbye_text = """
SAYONARA!👋
  
Your anime collection has been saved!
Thanks for using the Otaku Filing Cabinet!

Until next time, happy watching!
""".strip()

# uses box function to put messages into a formatted box
__WELCOME_MESSAGE = box(welcome_text)

__GOODBYE_MESSAGE = box(goodbye_text)

__HELP_MESSAGE = """
=================== 🌸 Otaku Filing Cabinet HELP 🌸 ===================

Here's how to use the app:

📚 BROWSING ANIME
  • list catalog     - Browse our legendary anime collection! ⚔️
  • list mine        - Check out your personal list! 📝✨
  • list catalog action - Find all the Shounen goodness! 💪
  • list mine > 8    - See your top-tier anime (the ones that made you cry)

➕ ADDING SHOWS  
  • add              - Add a hidden gem we don't know about yet! 💎
  • add Death Note   - Steal a show from our catalog (we won't tell) 🎭

⭐ UPDATING RATINGS
  • update           - Changed your mind? No judgment here! 🤔
  • update Naruto    - Give Naruto-kun the rating he deserves! 🍜

💾 SAVING YOUR LIST
  • save             - Create a backup of your precious collection! 📜
  • save summer2024  - Save with a custom name (memories included) 🌻

🚪 OTHER
  • help             - Summon this guide again! 📖
  • exit             - Ja ne~ (Your list is safe with us! Auto-saves on exit 💖)

📝 FILTER TIPS:
  Become a search ninja with these techniques:
  
  🗡️ BY GENRE: 
     list catalog action     → Find all the epic battles! 💥
     list mine romance       → Your collection of feels~ 💕
  
  🔍 BY TITLE:
     list catalog Death      → Catches "Death Note", "Death Parade"... 💀
     list mine Psycho        → Finds "Mob Psycho 100", "Psycho-Pass"! 🧠
     
  ⭐ BY RATING:
     list catalog > 700     → Only the legendary stuff! 🏆
     list mine < 5          → Your guilty pleasures (we all have them) 🤫
     list catalog = 1000    → The perfect 1000/1000 masterpieces! ✨
     
  🎯 COMBO MOVES:
     list catalog cyberpunk  → All that neon aesthetic! 🌃
     list mine >= 900       → Your hall of fame anime! 👑

✨ Pro tip: Just typing 'list' will ask which list you want!

=============== Ready to build your anime empire? 🎌 Ganbatte! ===============
""".strip()

# prompts the user for a command
__PROMPT = """What would you like to do? """

# COMMAND OPTION RETURNS
__ADD_COMMAND = "add"
__LIST_COMMAND = "list"
__EXIT_COMMAND = "exit"
__UPDATE_COMMAND = "update"
__SAVE_COMMAND = "save"
__HELP_COMMAND = "help"

# for filtering shows by rating
__FILTER_OPERATION_OPTIONS = ['<', '>', '=', '<=', '>=', '!=']

# some program constants
__MIN_STARS = 1
__MAX_STARS = 5
__SPACER = 2


def load_shows(filename: str) -> Dict[str, Tuple[int, str]]:
    """
    Loads the anime shows from the given file and returns a dictionary of anime shows and their rating.

    Example:
        >>> load_shows("data/anime_ratings_short.dat")                    # doctest: +NORMALIZE_WHITESPACE
        {"Steins;Gate": (2, "sci-fi"),
        "Naruto": (456, "action"),
        "Yuri On Ice": (7, "sports"),
        "Chainsaw Man": (8888, "horror"),
        "Fruits Basket": (5, "romance"),
        "Kill La Kill": (1, "action"),
        "Shiki": (1337, "horror"),
        "Black Clover": (69, "fantasy"),
        "Your Name": (3, "drama"),
        "Trigun": (911, "western")}

    Args:
        filename (str): The name of the file to load the shows from.

    Returns:
        Dict[str, Tuple[int, str]]: A dictionary of anime shows titles as the keys 
        and tuples of the ratings and genres as the values.
    """
    catalog = {}  # empty dict to store data from file

    user_file = open(filename)  # open the file
    read_user_file = user_file.read()  # read the file
    show_list = read_user_file.split('\n')  # creates list where each line is an element

    for line in show_list:
        line = line.strip()  # strips the whitespace from the line
        if not line:  # if line is empty it's skipped
            continue
        clean_key = line.split('::')  # splits line into [title, rating, genre]
        if len(clean_key) != 3:  # if the list doesn't have 3 elements skip
            continue
        title = clean_key[0].strip()  # extract title
        rating_str = clean_key[1].strip()  # extract rating (still a string)
        genre = clean_key[2].strip()  # extract genre

        # checks for proper value for rating (must be an int)
        try:
            rating = int(rating_str)  # convert rating to int
        except ValueError:
            print(f"Warning: Skipping '{title}' - rating must be a number (found: '{rating_str}')")  # prints error message if rating is not an int
            continue

        catalog[title] = (rating, genre)  # stores show in dictionary with title as key

    user_file.close()  # close the file 

    return catalog


def get_new_show_from_user() -> Tuple[str, int, str]:
    """
    Gets the user's input for show title, rating, and genre when they use the add command.
    
    Prompts the user for three pieces of information and validates each input,
    re-prompting if invalid. Title is cleaned to title case and genre is converted
    to lowercase.
    
    Args:
        None
    
    Returns:
        Tuple[str, int, str]: A tuple containing the cleaned title, rating as an integer,
        and genre in lowercase.
    """
    # get the title from the user and call clean_title function
    while True:
        user_title = (input("Enter the show's title: "))
        cleaned_user_title = clean_title(user_title)

        if cleaned_user_title != "":
            break
        else:
            print("Title cannot be blank. Please enter a show title.")  # if user doesn't enter a title re-prompt the user for a valid input

    # get the rating from the user
    while True:
        user_rating = input("What do you rate this show? ")

        try:
            int_rating = int(user_rating)  # convert rating to int
            break
        except ValueError:
            print("Rating must be a whole number.")  # if rating is string or float re-prompt the user for a valid input
            continue
    
    # get the genre from the user
    while True:
        user_genre = input("What is the show's genre? (e.g. action, slice of life, sports, etc.): ")
        cleaned_user_genre = user_genre.lower().strip()

        if cleaned_user_genre != "":  # if user doesn't enter a genre re-prompt the user for a valid input
            break
        else:
            print("Genre cannot be blank. Please enter a genre.")

    user_catalog = (cleaned_user_title, int_rating, cleaned_user_genre)  # create a tuple containing user's inputs

    return user_catalog


def clean_title(title: str) -> str:
    """
    Cleans a string stripping trailing and leading whitespaces,
    and converts it to title case. 

    Examples:
        # Standard cases
        >>> clean_title("death note  ")
        'Death Note'
        >>> clean_title("mob psycho 100")
        'Mob Psycho 100'
        >>> clean_title("attack on titan")
        'Attack On Titan'
        
        # Edge cases - extreme spacing
        >>> clean_title("     v")
        'V'
        >>> clean_title("      your lie in april        ")
        'Your Lie In April'
        >>> clean_title("fruits    basket")
        'Fruits Basket'

        # Edge case - random/mixed casing
        >>> clean_title("DeMoN sLaYeR")
        'Demon Slayer'
        >>> clean_title("ViOlEt EvErGaRdEn")
        'Violet Evergarden'
        >>> clean_title("cOdE gEaSs")
        'Code Geass'
        
        # Edge case - all caps
        >>> clean_title(" STEINS;GATE  ")
        'Steins;Gate'
        >>> clean_title("RE:ZERO")
        'Re:Zero'
        >>> clean_title("SPY X FAMILY")
        'Spy X Family'
        
        # Edge case - empty string
        >>> clean_title("")
        ''

    Args:
        title (str): show title to clean
    Returns:
        str : the show in title case, and leading and trailing spaces removed
    """

    return title.strip().title()


def convert_rating(val: int, min_stars: int = __MIN_STARS, max_stars: int = __MAX_STARS) -> str:
    """Converts int rating (1-10 scale) to stars (⭐) (1-5 scale). 
    
        Scales the input rating to fit within the star range:
        - Ratings 1-2 return '⭐' (1 star)
        - Ratings 3-4 return '⭐⭐' (2 stars)  
        - Ratings 5-6 return '⭐⭐⭐' (3 stars)
        - Ratings 7-8 return '⭐⭐⭐⭐' (4 stars)
        - Ratings 9-10 return '⭐⭐⭐⭐⭐' (5 stars)
        
        Any value below 1 returns min_stars (⭐).
        Any value above 10 returns max_stars (⭐⭐⭐⭐⭐).

    Examples:
        # Standard cases (normal ratings 1-10)
        >>> convert_rating(2, 1, 5)
        '*'
        >>> convert_rating(3, 1, 5)
        '**'
        >>> convert_rating(7, 1, 5)
        '****'
        
        # Edge cases - below minimum
        >>> convert_rating(0, 1, 5)
        '*'
        >>> convert_rating(-100, 1, 5)
        '*'
        >>> convert_rating(-5, 1, 5)
        '*'
        
        # Edge cases - extreme high values
        >>> convert_rating(1000, 1, 5)
        '*****'
        >>> convert_rating(1234567890, 1, 5)
        '*****'
        >>> convert_rating(9999999999999, 1, 5)
        '*****'

    Args:
        val (int): the rating value
        min_stars (int, optional): the minimum number of stars to return. Defaults to _MIN_STARS.
        max_stars (int, optional): the maximum number of stars to return. Defaults to _MAX_STARS.

    Returns:
        str: stars between min_stars and max_stars
    """
    if val <= 2:
        star_rating = 1
    elif val <= 4:
        star_rating = 2
    elif val <= 6:
        star_rating = 3
    elif val <= 8:
        star_rating = 4
    else:
        star_rating = 5

    return "⭐" * star_rating


def check_filter(show: Tuple[str, int, str], filter: str) -> bool:
    """Checks if the show meets the filter.

    The filter can either be a string  (case insensitive) that will map to the title, genre
    or a filter operation and a number. The filter operation can be
    one of the following: <, >, =, <=, >=, !=. Which is meant to check
    the rating of the show based on the number that follows. 

    If an empty string ("") is passed in, then the function will return True.

    Examples:
        # Standard cases
        >>> check_filter(("Death Parade", 643, "psychological"), "Death")
        True
        >>> check_filter(("Mob Psycho 100", 482, "comedy"), "> 400")
        True
        
        # Edge cases - No matches
        >>> check_filter(("Steins;Gate", 100, "scifi"), "Naruto")
        False
        >>> check_filter(("Your Lie in April", 10, "drama"), "action")
        False
        
        # Edge case - Invalid operators/format
        >>> check_filter(("Akira", 1000, "cyberpunk"), ">> 500")
        False
        >>> check_filter(("Spy x Family", 799, "family"), "> ")
        False
        >>> check_filter(("Wolf's Rain", 850, "drama"), "850")
        False
        
        # Edge case - Boundary ratings
        >>> check_filter(("Akira", 1000, "cyberpunk"), ">= 1000")
        True
        >>> check_filter(("Akira", 1000, "cyberpunk"), "> 1000")
        False
        >>> check_filter(("Your Lie in April", 10, "drama"), "<= 10")
        True
        
        # Edge case - Empty string
        >>> check_filter(("Fruits Basket", 774, "romance"), "")
        True
        
        # Edge case - Case sensitivity
        >>> check_filter(("Death Parade", 643, "psychological"), "DEATH")
        True
        >>> check_filter(("Death Parade", 643, "psychological"), "PSYCHOLOGICAL")
        True
        
        # Edge case - Partial matches that shouldn't work
        >>> check_filter(("Mob Psycho 100", 482, "comedy"), "com")
        False

    Args:
        show (Tuple[str, int, str]): The show tuple
        filter (str): The filter to check

    Returns:
        bool: True the show meets the filter requirements.
    """
    if filter == "":  # if empty str return True
        return True
    
    if filter.lower() in show[0].lower():  # if str in title return True
        return True
    
    if filter.lower() == show[2].lower():  # filter by genre
        return True
    
    parts_of_filter = filter.split()

    if len(parts_of_filter) != 2:
        return False
    
    operator = parts_of_filter[0]

    if operator not in __FILTER_OPERATION_OPTIONS:
        return False
    
    try:
        rating = int(parts_of_filter[1])
    except ValueError:
        print(f"Invalid numeric filter: '{parts_of_filter[1]}'. Please enter a whole number.")
        return False

    if operator == "<":
        return show[1] < rating
    elif operator == ">":
        return show[1] > rating
    elif operator == "=":
        return show[1] == rating
    elif operator == "<=":
        return show[1] <= rating
    elif operator == ">=":
        return show[1] >= rating
    elif operator == "!=":
        return show[1] != rating
    
    return False  # should not be reached but just in case


def print_shows(catalog: Dict[str, Tuple[int, str]], filter: str = '', spacer: int = __SPACER, max_stars: int = __MAX_STARS) -> None:
    """Prints shows from a dictionary with star ratings.

    Displays each show's title with a star rating representation. 
    
    Can filter the shows before printing based on an optional filter 
    parameter. See: check_filter() for filter options (by title, genre, 
    or rating comparison).

    Examples:
        >>> shows = {"Attack on Titan": (9, "action"), "Your Lie in April": (8, "drama"), "Haikyu!!": (7, "sports")}
        >>> print_shows(shows)
        *****  Attack on Titan
        ****   Your Lie in April
        ****   Haikyu!!
        
        >>> print_shows(shows, "Titan")
        *****  Attack on Titan
        
        >>> print_shows(shows, "sports")
        ****   Haikyu!!
        
        >>> print_shows(shows, "> 7")
        *****  Attack on Titan
        ****   Your Lie in April
        
        >>> print_shows(shows, "= 8")
        ****   Your Lie in April
        
        >>> shows_small = {"One Piece": (10, "adventure"), "Naruto": (6, "action"), "Bleach": (4, "action")}
        >>> print_shows(shows_small, "action")
        ***    Naruto
        **     Bleach
        
        >>> print_shows({})  # Empty dictionary
        
        >>> print_shows(shows, "nothing")  # No matches


    Args:
       shows (Dict[str, Tuple[int, str]]): Dictionary of shows with title as key and (rating, genre) as value
    """
    if filter != "":
        filtered_catalog = {}
        for title, (rating, genre) in catalog.items():
            if check_filter((title, rating, genre), filter):
                    filtered_catalog[title] = (rating, genre)
    else:
        filtered_catalog = catalog
    
    # Check if there are any shows to display
    if not filtered_catalog:
        if filter:
            print(f"Gomen! No anime found matching '{filter}' 😭")
        else:
            print("Your list is empty! Start adding shows! 📝")
        return

    # Extract title, rating, and genre from each dictionary entry
    for title, (rating, genre) in filtered_catalog.items():
        stars = convert_rating(rating)  # call convert_rating function and store in a variable
        num_stars = stars.count("⭐")  # Count the actual number of stars
        spaces_needed = (5 - num_stars) * 2  # Calculate spaces needed (5 max stars - current stars) * 2 for emoji width
        print(f"{stars}{' ' * spaces_needed}  |  {title:^28}  |  {genre:^15}")  # prints the formatted string

def update_rating(catalog: Dict[str, Tuple[int, str]], title: str) -> bool:
    """Updates the rating for an existing show in the dictionary.
    
    Displays the current rating, then prompts the user for a new rating
    while preserving the show's genre. Modifies the dictionary in place.
    
    Args:
        shows (Dict[str, Tuple[int, str]]): Dictionary of shows to modify
        title (str): Title of the show to update
    
    Returns:
        bool: True if show was found and updated, False if show not found
    """
    if title not in catalog:
        print('Show not found. Please use the "add" command to add this show.')
        return False
    
    value_from_catalog = catalog[title]
    current_rating_for_show = value_from_catalog[0]
    genre = value_from_catalog[1]
    print(f"Current rating: {current_rating_for_show}")

    while True:
        new_rating = input("What do you rate this show? (1 through 10): ")

        try:
            int_rating = int(new_rating)  # convert rating to int
            break
        except ValueError:
            print("Rating must be a whole number.")
            continue

    catalog[title] = (int_rating, genre)
    return True


def save_shows(catalog: Dict[str, Tuple[int, str]], filename: str) -> None:
    """Saves the show dictionary to a file.

    Writes each show to the specified file in the format:
    title::rating::genre
    
    This format matches the input format used by load_shows(), allowing
    saved files to be loaded back into the program.

    Example:
        >>> shows = {"Attack on Titan": (9, "action"), "Your Lie in April": (8, "drama")}
        >>> save_shows(shows, "my_anime_list.dat")
        # Creates file with:
        # Attack on Titan::9::action
        # Your Lie in April::8::drama

    Args:
        shows (Dict[str, Tuple[int, str]]): Dictionary of shows where keys are titles
            and values are tuples of (rating, genre)
        filename (str): The path/name of the file to write to. Will overwrite if exists.

    Returns:
        None
    """
    directory = "anime_shows_list"

    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join(directory, filename)

    with open(filepath, "w") as file:
        for title, (rating, genre) in catalog.items():
            file.write(f"{title}::{rating}::{genre}\n")


def menu() -> Tuple[str, str]:
    """
    Prompts the user for their command.

    See HELP_MESSAGE for more options. Will also
    parse the command and return the command and
    any options that were passed in.

    Returns:
        Tuple[str, str]: the command OPTION, and the value after the command, or 
        the empty string if there was no value.
    """
    valid = {__ADD_COMMAND, __LIST_COMMAND, __EXIT_COMMAND, __UPDATE_COMMAND, __SAVE_COMMAND, __HELP_COMMAND}
    while True:
        check = input(__PROMPT).strip()

        if not check:
            # empty input — re-prompt
            continue

        # this unpacks the string split by spaces into a variable, and a list of values
        command, *rest = check.split()
        command = command.casefold()

        # Basic validation
        if command in valid:
            return command, " ".join(rest)

        print(__HELP_MESSAGE)


def run() -> None:
    """
    Runs the Otaku Filing Cabinet application.
    """
    print(__WELCOME_MESSAGE)
    
    catalog = load_shows("data/anime_ratings.dat")  # Load the recommendations
    user_catalog = {}  # User's list starts empty
    
    command = ''
    while command != __EXIT_COMMAND:
        result = menu()  # get user input
        command = result[0]
        options = result[1]
        
        if command == __LIST_COMMAND:
            if options == "":
                which_list = input("Which list would you like to view? (catalog/mine): ").lower()
                filter = ""
            else:
                parts = options.split(maxsplit=1)  # splits at first space
                which_list = parts[0]
                filter = parts[1] if len(parts) > 1 else ""

            if which_list == "catalog":
                print_shows(catalog, filter)
            elif which_list == "mine":
                print_shows(user_catalog, filter)
            else:
                print("Invalid choice. Please specify 'catalog' or 'mine'")
        
        elif command == __ADD_COMMAND:
            if options == "":  # Just "add" - custom show
                title, rating, genre = get_new_show_from_user()
                user_catalog[title] = (rating, genre)
                print(f"Added '{title}' to your list with rating {rating}!")
                
            else:  # add from catalog
                title = clean_title(options)
                
                if title in catalog:
                    user_catalog[title] = catalog[title]
                    rating, genre = catalog[title]
                    print(f"Added '{title}' ({genre}, rating: {rating}) from catalog to your list!")
                else:
                    print(f"'{title}' not found in catalog.")
                    print("Use 'add' without a title to add a new show.")
                
        elif command == __UPDATE_COMMAND:
            if options == "":
                title = clean_title(input("Which show would you like to update? "))
            else:
                title = clean_title(options)
            
            success = update_rating(user_catalog, title)
            if success:
                print(f"Successfully updated '{title}'!")

        elif command == __SAVE_COMMAND:
            if options == "":
                filename = "my_anime_list.dat"
            else:  # "save [filename]"
                filename = options
            
            save_shows(user_catalog, filename)
            print(f"Your list has been saved to 'anime_shows_list/{filename}'!")
        
        elif command == __HELP_COMMAND:
            print(__HELP_MESSAGE)
        
    if user_catalog:  # Only save if user has added shows
        save_shows(user_catalog, "auto_save.dat")
        print("\n✨ Your list has been auto-saved to 'anime_shows_list/auto_save.dat'")

    print(__GOODBYE_MESSAGE)

if __name__ == "__main__":
    run()
