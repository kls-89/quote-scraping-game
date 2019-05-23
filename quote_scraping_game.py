"""
May 23, 2019

Scrape data (quotation text, author name, bio) from the website 'quotes.toscrape.com'
and use these to build a terminal-based quiz game.

This program was written by: Keenan Leonard-Solis as part of a web scraping project for
a Python tutorial I'm following (Colt Steele's Python course). I tried to focus on formatting
my code in a logical manner. I'm always looking for opportunities to learn and improve, so
constructive criticism is welcome! I may be reached at: kappsolis@gmail.com

NB: The code was written in Python 3.
"""
from game_logic import play, play_again
from util_functions import scrape_quotes


def main():

    # Make 1 call to scrape_quotes(), when the program is initially run, and
    # not for each time the user chooses to play again.
    quote_db = scrape_quotes()

    play(quote_db)

    while True:
        play_again(quote_db)


if __name__ == '__main__':
    main()
