import os
from typing import List

from word_generator import get_random_word
from display import get_hangman
from util import masked_word, update_masked_word

# ------------------------------------------------------------------------------
# TODO Functions - Implement the logic as per instructions
# ------------------------------------------------------------------------------


def start(life: int, random_word: str) -> None:
    """
    TODO: Implement this method to start the hangman game by displaying the hangman interface, initializing the game state,
    and handling user input for guessing letters. The game continues until the player guesses
    the word correctly or runs out of lives.

    Args:
        life (int): The number of lives the player has.
        random_word (str): The word to be guessed.

    Returns:
        None
    """
    raise NotImplementedError("This function is not implemented yet.")


# ------------------------------------------------------------------------------
# Starter Code - TOUCH AT YOUR OWN RISK!
# ------------------------------------------------------------------------------


def __clear_screen() -> None:
    """
    Clears the terminal screen.

    This function checks the operating system and uses the appropriate command
    to clear the screen. On Windows, it uses the "cls" command, and on Unix-like
    systems, it uses the "clear" command.
    """
    os.system("cls" if os.name == "nt" else "clear")


def __message(msg: str) -> None:
    """
    Display a message on the screen.

    Args:
        msg (str): The message to display.

    Returns:
        None
    """
    __clear_screen()
    print(msg)
    input("\nPress enter to continue...")


def __display(life: int, unknown: str, guesses: List[str]) -> None:
    """
    Display the hangman game interface.

    Args:
        life (int): The remaining life of the player.
        unknown (str): The word to guess, with hidden letters represented by underscores.
        guesses (List[str]): The list of letters guessed by the player.

    Returns:
        None
    """
    hangman = get_hangman(life)
    __clear_screen()
    print("Welcome to Hangman!")
    print(hangman)
    print(f"Life: {life}")
    print(f"Guesses: {', '.join(guesses)}")
    print(f"Word to guess: {unknown}")


if __name__ == "__main__":
    file_path = "resources/words.txt"
    random_word = get_random_word(file_path)
    start(6, random_word)
