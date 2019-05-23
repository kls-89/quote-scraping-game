# quote-scraping-game
## Scrape quotes from a website to build a quiz game.

This program, written in Python 3, uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the website *http://quotes.toscrape.com/* and scrape every quotation, author, and link to their bio page. With this data, a terminal-based quiz game is built.

Users get 4 chances to guess who authored the quote, and they're afforded a hint after each incorrect answer. If they don't guess correctly, the game ends, and the correct author name is presented.

The users are then offered the opportunity to play again.

### File Organization
+ **quote_scraping_game.py** -- This is the main project file. 
+ **util_functions.py** -- This file stores the functions that scrape the website data, generate the list of quote data, as well as hints to be used during gameplay.
+ **game_logic.py** -- This file stores the logic of the game and the *play again* functionality.

To run the program, download all 3 files and run: ```python3 quote_scraping_game.py```
