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

class IllegalMoveException(Exception):
  """Move not allowed."""

class Puzzle:
  """Represents an 8-puzzle."""

  def __init__(self, puzzle_str=None, puzzle_matrix=None):
    self.matrix = PUZZLE_GOAL

    if puzzle_str:
      self.matrix = Puzzle.str_to_matrix(puzzle_str)

    elif puzzle_matrix:
      self.matrix = puzzle_matrix


  def __str__(self):
    """Pretty-print representation of the puzzle."""
    return "\n".join(
      " ".join(str(s) for s in r)
      for r in self.matrix
    )

  def __hash__(self):
    """Hash representation of the puzzle (for dicts and sets)."""
    return hash(self.as_string())

  def __eq__(self, other):
    """Compares two puzzles."""
    if not isinstance(other, type(self)):
      return NotImplementedError

    return self.as_string() == other.as_string()

  def as_string(self):
    return Puzzle.matrix_to_str(self.matrix)

  def as_matrix(self):
    return self.matrix


  def is_solved(self):
    """Returns True if this puzzle is solved."""
    return self.as_string() == PUZZLE_GOAL_STR

  def zero_index(self):
    """Returns (i, j) representing the index of the zero element."""
    i, j = 0, 0

    while self.matrix[i][j] != 0 and i < 3 and j < 3:
      if i < 2:
        i += 1

      if i == 2:
        i = 0
        j += 1

    return i, j

  def allowed_moves(self):
    """Returns a set of allowed moves for the current puzzle."""
    moves = set(["up", "right", "down", "left"])
    i, j = self.zero_index()

    if i == 0:
      moves.remove("down")

    if i == 2:
      moves.remove("up")

    if j == 0:
      moves.remove("right")

    if j == 2:
      moves.remove("left")

    return moves

  def move(self, direction):
    """Moves the puzzle in certain direction."""
    if direction not in self.allowed_moves():
      raise IllegalMoveException

    i, j = self.zero_index()

    if direction == "up":
      self.__move_up(i, j)
    elif direction == "right":
      self.__move_right(i, j)
    elif direction == "down":
      self.__move_down(i, j)
    elif direction == "left":
      self.__move_left(i, j)

  def __move_up(self, i, j):
    self.matrix[i][j] = self.matrix[i+1][j]
    self.matrix[i+1][j] = 0

  def __move_right(self, i, j):
    self.matrix[i][j] = self.matrix[i][j-1]
    self.matrix[i][j-1] = 0

  def __move_down(self, i, j):
    self.matrix[i][j] = self.matrix[i-1][j]
    self.matrix[i-1][j] = 0

  def __move_left(self, i, j):
    self.matrix[i][j] = self.matrix[i][j+1]
    self.matrix[i][j+1] = 0


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
  def matrix_to_str(matrix):
    """Transforms a matrix representation of a puzzle into a string.

    Args:
      matrix (list of list): The 3x3 matrix representation of the
        puzzle.
    Returns:
      str: The string representation of the puzzle.

    """
    return "".join(
      "".join(str(c) for c in r)
      for r in matrix
    )
