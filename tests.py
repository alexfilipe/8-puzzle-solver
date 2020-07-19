"""tests.py -- contains tests for different classes
Author: Álex Filipe Santos
Date: 19 July 2020
"""
import random
from puzzle import Puzzle

puzzle1 = [
  [1, 8, 2],
  [0, 4, 3],
  [7, 6, 5]
] # Solvable

puzzle2 = [
  [1, 2, 4],
  [0, 5, 6],
  [8, 3, 7]
] # Not solvable

puzzle3 = [
  [7, 2, 4],
  [5, 0, 6],
  [8, 3, 1]
]

def test_allowed_moves():
  p1 = Puzzle(puzzle3)
  print(p1)
  print("Solvable:", p1.is_solvable())
  print("h1 =", p1.misplaced_heuristic())
  print("h2 =", p1.manhattan_heuristic())


  # Random permutations
  for i in range(10):
    print("----")
    print("Allowed moves:", p1.allowed_moves)

    move = random.sample(p1.allowed_moves, 1)[0]

    print("Moving", move)
    p1.move(move)
    print(p1)
    print("h1 =", p1.misplaced_heuristic())
    print("h2 =", p1.manhattan_heuristic())


def random_moves():
  """Tries to solve puzzle by randomly moving"""
  p1 = Puzzle(puzzle1)
  print(p1)

  count = 0

  while not p1.is_solved():
    move = random.sample(p1.allowed_moves, 1)[0]
    p1.move(move)
    count += 1

  print("Moves:", count)
  print(p1)


def test_solvable():
  p1 = Puzzle(puzzle1)
  p2 = Puzzle(puzzle2)

  print(p1)
  print("Solvable:", p1.is_solvable(), '\n')

  print(p2)
  print("Solvable:", p2.is_solvable(), '\n')

  p3 = Puzzle()
  print(p3)
  print("Solvable:", p3.is_solvable())


if __name__ == '__main__':
  test_allowed_moves()
  # test_solvable()
  # random_moves()
