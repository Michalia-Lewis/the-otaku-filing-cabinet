# The Otaku Filing Cabinet 📁✨

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-22%20passed-brightgreen)

A CLI anime collection manager — browse a curated catalog, build your personal list, and rate your shows.

Built with Python. No external dependencies. Just you, your terminal, and your questionable taste in anime.

## Features

- **Curated Catalog** — 50 anime titles with ratings and genres, ready to browse
- **Smart Filtering** — Search by title, genre, or rating to find exactly what you're looking for
- **Personal Collection** — Add shows from the catalog or enter your own manually
- **Flexible Ratings** — Rate shows on any scale you want (yes, even -284 or 10000 — we don't judge)
- **Auto-Save** — Never lose your list, even if you forget to save before exiting

## Quick Start

After running the program, you'll see a welcome message. Type `help` to see all available commands.

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

7. `save mylist` — save your collection to a file

   ![Save mylist](/screenshots/save_mylist.png)
   ![mylist](/screenshots/mylist.png)

8. `exit` — quit (auto-saves!)

   ![Exit](/screenshots/exit.png)

## Installation

### Prerequisites

- Python 3.x (3.10 or higher recommended)

### Download

1. Download the repository as a ZIP file (Code → Download ZIP)
2. Extract the ZIP to your desired location

### Run

**VS Code (recommended for beginners):**

1. Open VS Code
2. File → Open Folder → Select the extracted project folder
3. Open `src/otaku_filing_cabinet.py`
4. Click the Run button (▶️) in the top right corner

**Command Line:**

```bash
cd path/to/otaku-filing-cabinet/src
python otaku_filing_cabinet.py
```

## Technical Highlights

### Data Structure

The catalog uses dictionaries with anime titles as keys and tuples (rating, genre) as values. Tuples keep related data grouped and immutable — when a rating updates, the entire tuple is replaced, keeping the pairing intact.

```python
catalog = {
    "Death Note": (10000, "psychological"),
    "Naruto": (243, "action"),
}
```

### Rating Display

Ratings can be any integer (go wild), but display as a clean 1-5 star scale:

```python
def convert_rating(val: int) -> str:
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

### File I/O with Auto-Save

User collections save to a dedicated directory (created automatically if needed), and an auto-save triggers on exit so nothing gets lost.

```python
if user_catalog:
    save_shows(user_catalog, "auto_save.dat")
    print("\nYour list has been auto-saved to 'anime_shows_list/auto_save.dat'! 💾")
```

## Testing

22 unit tests covering file I/O, user input (with mocking), filtering, display output, and utility functions.

```bash
python -m pytest tests/
```

![Unit Test Results](/screenshots/unit_test_results.png)

## Demo

[Watch The Otaku Filing Cabinet in action](https://youtu.be/3v3gH7VHznE)

## What's Next

- [ ] Web app version with Flask
- [ ] "Plan to Watch" and "Currently Watching" categories  
- [ ] Database integration
- [ ] Focus on HCI — building a smooth, visually pleasing experience that current anime trackers lack

## License

[MIT](LICENSE)
