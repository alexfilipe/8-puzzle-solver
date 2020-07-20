"""puzzle.py -- Contains methods and classes to represent a 8-puzzle.

Author: Álex Filipe Santos
Date: 19 July 2020
"""

# The solved puzzle goal, represented as a string.
PUZZLE_GOAL_STR = "012345678"

# The puzzle goal, represented as a matrix.
PUZZLE_GOAL = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Puzzle positions (for faster calculations)
PUZZLE_POSITIONS = {
    0: (0, 0),
    1: (0, 1),
    2: (0, 2),
    3: (1, 0),
    4: (1, 1),
    5: (1, 2),
    6: (2, 0),
    7: (2, 1),
    8: (2, 2)
}

def str_to_matrix(puzzle_str):
    """Transforms a string representation of a puzzle into a matrix.

    Args:
        puzzle_str (str): The string representation of the puzzle, for
        example "012345678", filling a 3x3 matrix left to right.
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

def matrix_to_str(matrix):
    """Transforms a matrix representation of a puzzle into a string.

    Args:
        matrix (list of list): The 3x3 matrix representation of the puzzle.
    Returns:
        str: The string representation of the puzzle.
    """
    return "".join(
        "".join(str(c) for c in r)
        for r in matrix
    )


class NotSolvableException(Exception):
    """Puzzle not solvable."""

class IllegalMoveException(Exception):
    """Move not allowed."""


class Puzzle:
    """Represents an 8-puzzle."""

    def __init__(self, puzzle_matrix=PUZZLE_GOAL, puzzle_str=None):
        self.matrix = puzzle_matrix

        if puzzle_str:
            self.matrix = str_to_matrix(puzzle_str)

        self.__update_state()


    def __update_state(self):
        """Refreshes the state of the puzzle after updating its matrix
        (allowed moves, string representation, zero index, etc.)"""
        self.string = matrix_to_str(self.matrix)
        self.zero_index = self.__zero_index()
        self.allowed_moves = self.__allowed_moves()


    def __str__(self):
        """Pretty-print representation of the puzzle."""
        return "\n".join(
            " ".join(str(s) for s in r)
            for r in self.matrix
        )

    def __hash__(self):
        """Hash representation of the puzzle (for dicts and sets)."""
        return hash(self.string)

    def __eq__(self, other):
        """Compares two puzzles."""
        if not isinstance(other, type(self)):
            return NotImplementedError

        return self.string == other.string


    def is_solved(self):
        """Returns True if this puzzle is solved."""
        return self.string == PUZZLE_GOAL_STR

    def is_solvable(self):
        """Returns True if the current puzzle is solvable."""
        inversions = 0

        for i in range(8):
            for j in range(i + 1, 9):
                fst = int(self.string[i])
                snd = int(self.string[j])

                if fst > 0 and snd > 0 and fst > snd:
                    inversions += 1

        return inversions % 2 == 0

    def misplaced_heuristic(self):
        """Calculates the heuristic for number of misplaced tiles."""

        # The tile is in the correct place if string[i] = i
        misplaced = 0

        for i, s in enumerate(self.string):
            s = int(s)
            if s != 0 and i != s:
                misplaced += 1

        return misplaced

    def manhattan_heuristic(self):
        """Calculates the heuristic for Manhattan distance."""
        total_distance = 0

        for i1 in range(3):
            for j1 in range(3):
                # The Manhattan distance is |i1 - i2| + |j1 - j2|
                # for two points (i1, i2) <-> (j1, j2)

                # Number in tile
                n = int(self.matrix[i1][j1])

                if n != 0:
                    # Where the number is supposed to be
                    i2, j2 = PUZZLE_POSITIONS[n]

                    # Distance
                    dist = abs(i1 - i2) + abs(j1 - j2)

                    total_distance += dist

        return total_distance


    def __zero_index(self):
        """Returns (i, j) representing the index of the zero element."""
        i, j = 0, 0

        while i < 3 and j < 3 and self.matrix[i][j] != 0:
            if i < 2:
                i += 1

            elif i == 2:
                i = 0
                j += 1

        return i, j

    def __allowed_moves(self):
        """Returns a set of allowed moves for the current puzzle."""
        moves = set(["up", "right", "down", "left"])
        i, j = self.__zero_index()

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
        if direction not in self.allowed_moves:
            raise IllegalMoveException

        i, j = self.zero_index

        if direction == "up":
            self.__move_up(i, j)
        elif direction == "right":
            self.__move_right(i, j)
        elif direction == "down":
            self.__move_down(i, j)
        elif direction == "left":
            self.__move_left(i, j)

        self.__update_state()

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
