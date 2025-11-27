# Final Project Report

* Student Name: Michalia Lewis
* Github Username: Michalia-Lewis
* Semester: Fall 2025
* Course: CS 5001 Intensive Foundations of Computer Science

## Description

For my project I created The Otaku Filing Cabinet. This program allows users to browse a catalog of anime recommendations and build their own personal collection. Users can add shows, update ratings, filter by genre or rating, and save their list for later. As for the why: I am an avid anime fan and really enjoy being able to combine that love with programming. Furthermore, I took inspiration from the Star Rating App that we programmed for a homework assignment and wanted to expand on it with my own otaku-themed twist.

## Key Features

This program allows the user to search through a curated catalog of 50 anime shows, complete with ratings and genres. Users can filter shows by title, genre, or rating to find exactly what they're looking for. The user is able to create their own list using the catalog or by adding shows not in the catalog, as well as save their list. One of my favorite features is the auto save function in case the user forgets to save their list. The app also includes a fun otaku personality with Japanese expressions and emojis throughout!

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

* Python 3.x installed on your machine

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

Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did.

### Major Challenges

Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

## Example Runs

Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing

How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission.

> _Make it easy for us to know you _ran the project_ and _tested the project_ before you submitted this report!_

## Missing Features / What's Next

Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future.

## Final Reflection

Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
