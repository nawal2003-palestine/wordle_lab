"""Module for the Wordle game.

    Functions:
    - check_guess_correct: Checks if a guess is correct.
    - find_all_char_positions: Finds all positions of a character in a word.
    - feed_back_word: Provides feedback on a guess compared to the word.

    Constants:
    - MAX_ATTEMPTS: The maximum number of attempts allowed in the game.
"""


from typing import List


# Max attempts of the game

MAX_ATTEMPTS = 6


def check_guess_correct(word: str, guess: str) -> bool:
    """Check the guess against the word
    Return: True if the guess is correct, False otherwise
    """
    pass


def find_all_char_positions(word: str, char: str) -> List[int]:
    """Given a word and a character, find all the indices of that character."""
    pass


def feed_back_word(word: str, guess: str) -> List[str]:
    """Check the guess against the word and return the feedback
    Return: a list with the feedback for each letter in the guess
    """
    # Initialize the feedback list
    # It will contain the colors for each letter in the guess
    # The default color is RED for all the letters
    # GREEN for the correct letter in the correct position
    # YELLOW for the correct letter in the wrong position
    pass
