# Final Project Report

* Student Name: Michalia Lewis
* Github Username: Michalia-Lewis
* Semester: Fall 2025
* Course: CS 5001 Intensive Foundations of Computer Science

## Description

For my project, I created The Otaku Filing Cabinet. This program allows users to browse a catalog of anime recommendations and build their own personal collection. As an avid anime fan, I loved the opportunity to combine that passion with programming. I also drew inspiration from the Star Rating App we built for a homework assignment and wanted to expand on it with my own otaku-themed twist.

## Key Features

Users can search through a curated catalog of 50 anime shows, complete with ratings and genres. Users can filter by title, genre, or rating to find exactly what they're looking for, and they can build their own list using the catalog or by adding shows manually. The auto-save feature is a personal favorite of mine because it ensures no progress is lost if someone forgets to save.

## Guide

After running the program, you'll be greeted with a welcome message. Type `help` to see all available commands.

![Welcome Message](/screenshots/welcome_message.png)

![Help Message](/screenshots/help_message.png)

A typical session might look like:

1. `list catalog` — browse the anime catalog

   ![List Catalog](/screenshots/list_catalog_snippet.png)

2. `list catalog action` — filter by genre

    ![List Catalog Action](/screenshots/list_catalog_action.png)

3. `add Death Note` — add a show from the catalog to your list

    ![Add Death Note](/screenshots/add_death_note.png)

4. `add` — add your own custom show

    ![Add](/screenshots/add.png)

5. `list mine` — view your personal list

    ![List Mine](/screenshots/list_mine.png)

6. `update Naruto` — change a rating

    ![Update Rating](/screenshots/update_rating.png)

7. `save mylist` — saves your collection in a file titled "mylist"

    ![Save mylist](/screenshots/save_mylist.png)
    ![mylist](/screenshots/mylist.png)

8. `exit` — quit (auto-saves!)

    ![Exit](/screenshots/exit.png)

## Installation Instructions

### Prerequisites

* Python 3.x installed on your machine (Python 3.10 or higher recommended)

### Download

1. Download the repository as a ZIP file (Code → Download ZIP)
2. Extract the ZIP to your desired location

### Running the Program

**Using VS Code (Recommended for beginners):**

1. Open VS Code
2. File → Open Folder → Select the extracted project folder
3. Open `src/otaku_filing_cabinet.py`
4. Click the "Run" button (▶️) in the top right corner

**Using Command Prompt/Terminal (Advanced):**

1. Open Command Prompt (Windows) or Terminal (Mac/Linux)
2. Navigate to the project's `src` folder:

```
   cd path/to/CS5001-Final-Project/src
```

3. Run the program:

```
   python otaku_filing_cabinet.py
```

### Dependencies

This project uses only Python's built-in libraries — no additional installation needed!

## Code Review

The main application code can be found in [`src/otaku_filing_cabinet.py`](src/otaku_filing_cabinet.py).

### Data Structures

For The Otaku Filing Cabinet, I wanted to provide a catalog of anime shows that users could search through, and dictionaries were a natural fit because of their key-value structure. Using anime titles as keys and tuples as values (storing rating and genre) was the simplest way to achieve the catalog I envisioned. I chose tuples because they group related data together, and their immutability adds a layer of reliability. When a user updates a rating, the entire tuple is replaced rather than individual elements being modified, ensuring the pairing stays intact.

**Example:**

```python
# Dictionary with title as key, tuple of (rating, genre) as value
catalog = {
    "Death Note": (10000, "psychological"),
    "Naruto": (243, "action"),
    ...
}
```

### load_shows()

In a previous homework assignment, we built a star rating program that allowed users to add movies and ratings through the terminal. At the time, we hadn't learned how to work with files, so I wanted to expand on that foundation. I created a .dat file containing 50 anime titles, each with a rating and genre, and used the [`load_shows()`](src/otaku_filing_cabinet.py) function to read the file and store its contents in a dictionary. I also incorporated a try/except block, both to aid in testing and to provide users with helpful feedback if an error occurred.

**Snippet:**

```python
user_file = open(filename)
read_user_file = user_file.read()
show_list = read_user_file.split('\n')

for line in show_list:
    # ... parsing logic ...
    
    try:
        rating = int(rating_str)
    except ValueError:
        print(f"⚠️ Skipping '{title}' - rating must be a number")
        continue

    catalog[title] = (rating, genre)
```

### check_filter()

The star rating program included a filter function that I really liked, so I expanded it to not only let users search by title and rating but by genre as well. Sometimes you just want to find a good romance or slice of life anime to watch 😂. I also included a try/except block to catch any non-integer values entered as a rating.

**Snippet:**

```python
if filter.lower() == show[2].lower():  # filter by genre
        return True
    
    parts_of_filter = filter.split()  # split filter into operator and value

    if len(parts_of_filter) != 2:  # Operator and value required
        return False
    
    operator = parts_of_filter[0]

    if operator not in __FILTER_OPERATION_OPTIONS:
        return False
    
    # Validate and convert rating value
    try:
        rating = int(parts_of_filter[1])
    except ValueError:
        print(f"⚠️ Invalid filter - rating must be a number (found: '{parts_of_filter[1]}')")
        return False

    if operator == "<":
        return show[1] < rating
```

### convert_rating()

For the [`convert_rating()`](src/otaku_filing_cabinet.py) function I took the same function from the stars rating app but decided to create a scale so that the amount of stars would be a better fit for a 1-10 scale since most shows are rated 1-10 in other anime show tracker apps. However, I was still sure to include numbers above 10 (max of 5 stars) and below 1 (minimum of 1 star). This allows the user to enter unique ratings into their catalog but retain a simple display when printed to the terminal. I think being able to rate a show at 1000 or at -284 is a great way for the user to express how they felt about the show. Furthermore, once learning that I could use emojis in my code I opted to update the original star (*) to an emoji star to provide an even more eye-pleasing display.

**Snippet:**

```python
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
```

### save_shows()

For our star rating app assignment, I noticed that our professor included a message informing users that their list would not be saved, since we hadn't yet learned how to write files. This was one of the deciding factors for choosing to build The Otaku Filing Cabinet. I wanted users to be able to save their list as a file they could return to later, so I included a function to write files as well. I took my [`save_shows()`](src/otaku_filing_cabinet.py) function a step further by storing a dedicated directory path and writing an if statement to create the directory automatically if it didn't already exist.

**Snippet:**

```python
# Set up directory for saved anime lists
    directory = "anime_shows_list"

    # Create directory if it doesn't exist yet
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Build full path to save file
    filepath = os.path.join(directory, filename)

    # Write each show to file in title::rating::genre format
    with open(filepath, "w") as file:
        for title, (rating, genre) in catalog.items():
            file.write(f"{title}::{rating}::{genre}\n")
```

### Auto Save Feature

I wanted to include a feature that auto saves the user's catalog in case they exit before manually saving. It turned out to be simple to implement, and it's something I look forward to reusing in future projects involving file I/O.

**Snippet:**

```python
if user_catalog:  # save if user has added shows
        save_shows(user_catalog, "auto_save.dat")
        print("\nYour list has been auto-saved to 'anime_shows_list/auto_save.dat'! 💾")
```

## Major Challenges

One of my major challenges was formatting. This was the first program I had written that required a lot of user-facing text. I had to learn new ways to format strings as well as write a helper function for creating bordered boxes instead of manually typing them out for each message. This project helped me realize not only how important formatting is but how much fun it can be to provide the user with an aesthetically pleasing program. Being able to use emojis and create an experience instead of plain strings brought me a lot of joy, and I had fun crafting an "otaku" vibe that anime enthusiasts can enjoy.

Another challenge was writing unit tests for The Otaku Filing Cabinet. For example, the [`get_new_show_from_user()`](src/otaku_filing_cabinet.py) and [`update_rating()`](src/otaku_filing_cabinet.py) functions require user input, so I had to research the best ways to test them. To test `get_new_show_from_user` I learned how to use `side_effect` and for `update_rating`,  I used mocking to simulate user input. I also learned about capturing stdout for [`print_shows()`](src/otaku_filing_cabinet.py), which allowed me to verify the function's output.

## Example Runs

[The Otaku Filing Cabinet Demonstration](https://youtu.be/3v3gH7VHznE)

## Testing

I used a combination of doctests and unit tests to verify my code.

### Doctests

Functions like `clean_title()`, `convert_rating()`, and `check_filter()` include doctests within their docstrings for quick validation. To verify they passed, I temporarily commented out `run()` and ran `doctest.testmod(verbose=True)` instead.

**Doctests Results:**

![Doctest Results](/screenshots/doctest_results.png)

### Unit Tests

I wrote 22 unit tests in [`tests/test_otaku_filing_cabinet.py`](tests/test_otaku_filing_cabinet.py) covering:

* File I/O (`load_shows`, `save_shows`)
* User input (`get_new_show_from_user`, `update_rating`)
* Filtering and display (`check_filter`, `print_shows`)
* Utility functions (`box`, `clean_title`, `convert_rating`)

**Unit Test Results:**

![Unit Test Results](/screenshots/unit_test_results.png)

## Missing Features / What's Next

Originally, I wanted to create a web app using Flask. However, due to my limited time and knowledge, I was unable to do so. This constraint allowed me to focus on strengthening my current skills by practicing recently learned topics. My overall goal for The Otaku Filing Cabinet is to create a website and app that focus more on Human-Computer Interaction (HCI) than information storage. As someone who uses anime show trackers, I've noticed that many fail to provide a smooth and visually pleasing experience alongside their extensive databases and features. One day, I would like to fill that gap, using this project as the foundation.

## Final Reflection

This course taught me how important it is to look at the big picture and break it into smaller pieces. Before CS 5001, I struggled with many tasks because I didn't know how to identify manageable steps within a larger goal. After practicing writing functions and understanding how even a small function plays a big role in the overall program, I can now step back and see what smaller tasks are needed to craft the resulting masterpiece. The biggest takeaway for me, though, was that it's okay to make mistakes and try again. I sometimes lose focus and get frustrated if something isn't perfect on the first run, but through this class I came to see the value of making mistakes and learning from them to improve not only my skills but my confidence as well. Moving forward, I'm excited to learn about web development and databases, both of which are vital to my goal of creating a website and app version of The Otaku Filing Cabinet.
