from bs4 import BeautifulSoup
import requests

URL = 'http://quotes.toscrape.com/'


def scrape_quotes():
    """
    Programmatically scrape all the quotes from every page of the website (URL), saving them to a list "quote_db" as a collection of [quote text, author name, and link for additional information].
    """

    # page_count is 1 because the home page of the site is the 1st page with quotes.
    page_count = 1

    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    quote_db = []

    # Each quote on the page is formatted as div. I refer to these objects
    # here as "quote_cards."
    quote_cards = soup.select('.quote')

    # Loop runs until it reaches a page with no quotes.
    while len(quote_cards) > 0:

        quote_cards = soup.select('.quote')

        for quote in quote_cards:
            quote_text = quote.select('.text')[0].get_text()
            quote_author = quote.select(".author")[0].get_text()
            quote_link = quote.select(".author")[0].find_next_sibling()['href']

            quote_stats = [quote_text, quote_author, quote_link]

            quote_db.append(quote_stats)

        page_count += 1

        # Send a new request to the next page.
        res = requests.get(f"{URL}page/{page_count}")
        soup = BeautifulSoup(res.text, "html.parser")

    return quote_db


def get_hints(link):
    """
    Scrape the biography link for a given author, generate and return a list of hints based on the author's dob, place of birth, and name.
    """
    res = requests.get(f"{URL}{link}")
    soup = BeautifulSoup(res.text, "html.parser")

    author_name = soup.select('.author-title')[0].get_text()
    author_born_location = soup.select('.author-born-location')[0].get_text()
    author_born_date = soup.select('.author-born-date')[0].get_text()

    # Split the author's name into a list ['first_name', 'last_name'] so that
    # their initials and lengths of their first and last names can be used as
    # hints.
    author_name_split = author_name.split(" ")

    # Initials: e.g. "Bob Marley" -> "B.M."
    author_initials = f"{author_name_split[0][0]}.{author_name_split[1][0]}."

    # Determine the number of letters in the author's first and last names.
    # Store as a list. e.g. "Bob Marley" -> [3, 6]
    author_name_letter_count = [len(name) for name in author_name_split]

    hints = [
        f"This author was born {author_born_date} {author_born_location}.",
        f"This author's initials are: {author_initials}",
        f"This author's first and last names have {author_name_letter_count[0]} and {author_name_letter_count[1]} letters, respectively."
    ]

    return hints
