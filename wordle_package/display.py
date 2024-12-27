"""Module for displaying colored text in the terminal for the Wordle game.

    Functions:
        - header: Prints a header in the terminal.
        - game_instructions: Prints the game instructions in the terminal.
        - game_start_display: Prints the starting message for the game.
        - display_word_feedback: Displays the colored feedback for a guess.

    Constants:
        - COLORS: A dictionary containing ANSI color codes for GREEN, YELLOW, RED, and RESET.
"""


from typing import List

# ANSI color formatting
COLORS = {
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "RED": "\033[31m",
    "RESET": "\033[0m"
}


# def header(text: str) -> None:
#     """Print a header in the terminal."""
#     pass


def game_instructions():
    """Print the game instructions in the terminal."""
    pass


def game_start_display():
    """Print the starting message for the game."""
    pass


def display_word_feedback(guess: str, feedback: List[str]) -> str:
    """Display the coloured feedback for a guess."""
    pass


def display_win(word: str, attempt: int) -> None:
    """Display for winning"""
    pass


def display_lost(word: str) -> None:
    """Display for losing"""
    pass
