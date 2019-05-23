from os import system
from random import choice
from util_functions import get_hints


def play(db):
	"""
	Randomly pick a quote from the master collection of quote data.
	Allow users 4 guesses, providing hints after each incorrect answer.
	The hints are stored as a list [hint 1 (dob and location), hint 2 (author's initials), hint 3 (number of letters in the author's first and last names)]
	"""

	playing = True
	guess_count = 0
	# random_quote is formatted as: [quote text, author name, bio link]
	random_quote = choice(db)
	hints = get_hints(random_quote[2])

	print(f"Who said, {random_quote[0]}?")

	while playing:

	    guess = input("Your guess: ")

	    # Guess correctly
	    if guess == random_quote[1]:
	        print(f"Correct!\n")
	        break
	    
	    # Guess incorrectly 3 times
	    if guess_count == 3:
	    	print("\nGAME OVER!")
	    	print(f"The correct answer was: {random_quote[1]}\n")
	    	break
	    
	    # Guess incorrectly
	    else:
	        print("\nIncorrect!")
	        print(f"Here's a hint: {hints[guess_count]}\n")
	        guess_count += 1




def play_again(db):
	"""
	Reset the game if the user wishes to play again, otherwise, quit.
	"""

	play_again = input("Play again? (y/n) ")

	if play_again == 'y':
		# Clear the terminal window. This is purely for aesthetics.
	    system("clear")
	    print("Fetching a new quote...")
	    play(db)

	elif play_again == 'n':
		system("clear")
		exit("Thanks for playing!")
