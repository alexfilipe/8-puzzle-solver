"""solve_puzzle.py -- Command-line interface for 8-puzzle solving.

Author: Álex Filipe Santos
Date: 19 July 2020
"""
import re
import time
from random import shuffle
from puzzle import Puzzle, NotSolvableException
from solver import PuzzleSolver


def generate_random_puzzle():
    """Generates a random puzzle, which might be solvable or not.

    Returns:
        obj:`Puzzle`: a puzzle
    """
    permutation = list("012345678")
    shuffle(permutation)
    puzzle_str = "".join(permutation)
    return Puzzle(puzzle_str=puzzle_str)

def generate_solvable_puzzle():
    """Generates a solvable random puzzle.

    Returns:
        obj:`Puzzle`: a solvable puzzle.
    """
    puzzle = generate_random_puzzle()

    while not puzzle.is_solvable():
        puzzle = generate_random_puzzle()

    return puzzle

def input_to_puzzle(input_str):
    """Transforms an input string from the CLI into a Puzzle object.

    Returns:
        obj:`Puzzle`: a puzzle
    """
    input_str = re.sub(r"[ \n]+", "", input_str)
    return Puzzle(puzzle_str=input_str)


if __name__ == '__main__':
    print("CS 4200 Project 1")
    print("8-Puzzle Solver")

    input_mode = 0

    while input_mode != 3:
        print("--------------------------\n")
        print("Select option:")
        print("[1] Solve random puzzle")
        print("[2] Solve puzzle from input")
        print("[3] Exit")

        input_mode = int(input())
        puzzle = Puzzle()


        # Random Puzzle Input
        if input_mode == 1:
            puzzle = generate_solvable_puzzle()

            # Display puzzle
            print("\nPuzzle:")
            print(puzzle)

        # Input Puzzle
        elif input_mode == 2:
            print("\nType in your puzzle in 3 lines:")

            puzzle_input = ""
            for _ in range(3):
                puzzle_input += input()

            puzzle = input_to_puzzle(puzzle_input)

        elif input_mode == 3:
            continue

        else:
            print("Invalid option")
            continue

        if not puzzle.is_solvable():
            print("\nPuzzle is not solvable. Please try again")
            continue


        # Select type of heuristic
        print("\nSelect heuristic to solve:")
        print("[1] h1 = Number of Misplaced Tiles")
        print("[2] h2 = Manhattan Distance")

        heuristic = int(input())

        if heuristic not in [1, 2]:
            print("Invalid option")
            continue


        # Invokes puzzle solver
        solver = PuzzleSolver(puzzle, heuristic=heuristic)

        try:
            # Tries to find solution and records running time
            start_time = time.time()
            solution = solver.find_solution()
            end_time = time.time()
            solve_time = end_time - start_time

            print("\nSolution Found")

            for i, step in enumerate(solution["steps"]):
                if i == 0:
                    print("\nInitial state:")
                    print(step)
                else:
                    print("\nStep #{}: move {}".format(i, step.last_move))
                    print(step)

            print()
            print("Solution Depth: {}".format(solution["depth"]))
            print("Search Cost for heuristic h{}: {} nodes"
                  .format(heuristic, solution["cost"]))
            print("Search Time: {0:.4f} seconds".format(solve_time))

        except NotSolvableException:
            print("The puzzle solver failed to find a solution.")
