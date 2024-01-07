# ------------------------------------------------------------------------------
# Starter Code - TOUCH AT YOUR OWN RISK!
# ------------------------------------------------------------------------------


def get_hangman(life: int) -> str:
    """
    Returns the ASCII art representation of the hangman based on the remaining life.

    Args:
        life (int): The remaining life of the hangman.

    Returns:
        str: The ASCII art representation of the hangman.
    """
    if life == 6:
        hangman = """
        _______
        |     |
              |
              |
              |
              |
      ________|
      """

        return hangman
    elif life == 5:
        hangman = """
      _______
      |     |
      O     |
            |
            |
            |
    ________|
    """
        return hangman
    elif life == 4:
        hangman = """
      _______
      |     |
      O     |
      |     |
            |
            |
    ________|
    """
        return hangman
    elif life == 3:
        hangman = """
      _______
      |     |
      O     |
     /|     |
            |
            |
    ________|
    """
        return hangman
    elif life == 2:
        hangman = """
      _______
      |     |
      O     |
     /|\\    |
            |
            |
    ________|
    """
        return hangman
    elif life == 1:
        hangman = """
      _______
      |     |
      O     |
     /|\\    |
     /      |
            |
    ________|
    """
        return hangman
    elif life == 0:
        hangman = """
      _______
      |     |
      O     |
     /|\\    |
     / \\    |
            |
    ________|
    """
        return hangman
