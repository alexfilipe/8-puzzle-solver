"""tests.py -- contains tests for different classes

Author: Álex Filipe Santos
Date: 19 July 2020
"""
import random
from puzzle import Puzzle
from solver import PuzzleNode, PuzzleSolver

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

puzzle4 = [
    [1, 2, 5],
    [3, 4, 8],
    [6, 7, 0]
] # Solution depth 4

puzzle5 = [
    [1, 2, 5],
    [4, 0, 8],
    [3, 6, 7]
] # Solution depth 8

puzzle8 = [
    [2, 6, 5],
    [8, 0, 7],
    [1, 4, 3]
] # Solution depth 20

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
    """Tests different puzzles to see if they are solvable."""
    p1 = Puzzle(puzzle1)
    p2 = Puzzle(puzzle2)

    print(p1)
    print("Solvable:", p1.is_solvable(), '\n')

    print(p2)
    print("Solvable:", p2.is_solvable(), '\n')

    p3 = Puzzle()
    print(p3)
    print("Solvable:", p3.is_solvable())


def test_next_moves():
    """Tests a number of allowed moves coming from a Puzzle."""
    p3 = Puzzle(puzzle3)
    node = PuzzleNode(p3)

    print("Puzzle: ")
    print(node.puzzle)

    frontier = node.next_moves()

    for i, n in enumerate(frontier):
        print("---")
        print(f"Puzzle #{i}:")
        print(n.puzzle)
        print("Cumulative cost:", n.cumulative_cost)
        print("f1 = ", n.evaluation(1))
        print("f2 = ", n.evaluation(2))


def test_search():
    """Tests an A* search run to find the puzzle solution."""
    puzzle = Puzzle(puzzle3)
    solver = PuzzleSolver(puzzle, heuristic=2)
    solution = solver.find_solution()

    steps = solution["steps"]
    cost = solution["cost"]

    for p in steps:
        print(p)
        print()

    print("Solution depth:", len(steps))
    print("Search cost:", cost)


if __name__ == '__main__':
    # test_allowed_moves()
    # test_solvable()
    # random_moves()
    # test_frontier()
    test_search()
