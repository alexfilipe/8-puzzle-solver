"""puzzle.py -- Contains methods and classes to represent a 8-puzzle.

Author: Álex Filipe Santos
Date: 17 July 2020
"""

# The solved puzzle goal, represented as a string.
PUZZLE_GOAL_STR = "012345678"

# The puzzle goal, represented as a matrix.
PUZZLE_GOAL = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8]
]

class Puzzle:
  """Represents an 8-puzzle."""

  def __init__(self, puzzle_str=None):
    self.puzzle_str = PUZZLE_GOAL_STR
    self.puzzle_matrix = PUZZLE_GOAL

    if puzzle_str:
      self.puzzle_str = puzzle_str
      self.puzzle_matrix = Puzzle.str_to_matrix(puzzle_str)


  def __str__(self):
    """Pretty representation of the puzzle."""
    return "\n".join(
      " ".join(str(s) for s in r)
      for r in self.puzzle_matrix
    )

  def __hash__(self):
    """Hash representation of the puzzle (for dicts and sets)."""
    return hash(self.puzzle_str)

  def __eq__(self, other):
    """Compares two puzzles."""
    if not isinstance(other, type(self)):
      return NotImplementedError

    return self.puzzle_str == other.puzzle_str


  @staticmethod
  def str_to_matrix(puzzle_str):
    """Transforms a string representation of a puzzle into a matrix.

    Args:
      puzzle_str (str): The string representation of the puzzle, for example
        "012345678", filling a 3x3 matrix left to right.
    Returns:
      list of list: The 3x3 matrix representation of the puzzle.

    """
    if len(puzzle_str) != 9:
      raise ValueError("Puzzle not valid")

    return [
      list(int(s) for s in puzzle_str[0:3]),
      list(int(s) for s in puzzle_str[3:6]),
      list(int(s) for s in puzzle_str[6:9])
    ]


  @staticmethod
  def matrix_to_str(puzzle_matrix):
    """Transforms a matrix representation of a puzzle into a string.

    Args:
      puzzle_matrix (list of list): The 3x3 matrix representation of the
        puzzle.
    Returns:
      str: The string representation of the puzzle.

    """
    return "".join(
      "".join([str(c) for c in r])
      for r in puzzle_matrix
    )
