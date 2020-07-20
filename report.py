"""report.py -- generates a runtime report from different test cases

Author: Álex Filipe Santos
Date: 19 July 2020
"""
import sys
import time
import json
from puzzle import Puzzle
from solver import PuzzleSolver
from solve_puzzle import generate_solvable_puzzle, input_to_puzzle


def file_to_puzzle_list(filepath):
    """Converts a test file from the /output folder into a list of puzzles.

    Args:
        filepath (str): the file output path.
    """
    puzzles = []

    with open(filepath) as fp:
        current_line = 0
        puzzle_str = ""

        # Ignore first line
        line = fp.readline()

        while line:
            current_line += 1
            line = fp.readline()

            if current_line % 4 == 0:
                puzzle = input_to_puzzle(puzzle_str)
                puzzles.append(puzzle)
                puzzle_str = ""

            else:
                puzzle_str += line

    return puzzles


def report(cases):
    """Generates a statistical report based on an arbitrary list of input
    cases.

    Args:
        cases (list of obj:`Puzzle`): list of puzzles to be solved.
    """

    # Filters only solvable puzzles
    filtered_cases = []
    for puzzle in cases:
        if puzzle.is_solvable():
            filtered_cases.append(puzzle)

    total_cost_h1 = 0
    total_cost_h2 = 0

    total_time_h1 = 0
    total_time_h2 = 0

    total_cases = len(filtered_cases)

    # Solver for heuristic h1
    for puzzle in filtered_cases:
        solver = PuzzleSolver(puzzle, heuristic=1)

        start_time = time.time()
        solution = solver.find_solution()
        end_time = time.time()

        total_cost_h1 += solution["cost"]
        total_time_h1 += end_time - start_time

    # Solver for heuristic h2
    for puzzle in filtered_cases:
        solver = PuzzleSolver(puzzle, heuristic=2)

        start_time = time.time()
        solution = solver.find_solution()
        end_time = time.time()

        total_cost_h2 += solution["cost"]
        total_time_h2 += end_time - start_time

    return {
        "cases_tested": total_cases,
        "total_cost_h1": total_cost_h1,
        "average_cost_h1": total_cost_h1 / total_cases,
        "total_time_h1": total_time_h1,
        "average_time_h1": total_time_h1 / total_cases,
        "total_cost_h2": total_cost_h2,
        "average_cost_h2": total_cost_h2 / total_cases,
        "total_time_h2": total_time_h2,
        "average_time_h2": total_time_h2 / total_cases
    }


def report_sample_cases(filepath):
    """Writes report to file based on the sample cases provided."""
    length4 = file_to_puzzle_list("test/Length4.txt")
    length8 = file_to_puzzle_list("test/Length8.txt")
    length12 = file_to_puzzle_list("test/Length12.txt")
    length16 = file_to_puzzle_list("test/Length16.txt")
    length20 = file_to_puzzle_list("test/Length20.txt")

    report4 = report(length4)
    report8 = report(length8)
    report12 = report(length12)
    report16 = report(length16)
    report20 = report(length20)

    data = [
        {"depth": 4, "stats": report4},
        {"depth": 8, "stats": report8},
        {"depth": 12, "stats": report12},
        {"depth": 16, "stats": report16},
        {"depth": 20, "stats": report20}
    ]

    with open(filepath, 'w') as output:
        json.dump(data, output, indent=4)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("USAGE: python report.py [report-mode] [output-file]")

    else:
        report_mode = int(sys.argv[1])
        report_file = sys.argv[2]

        # Report mode 1: sample cases
        if report_mode == 1:
            report_sample_cases(report_file)

        # TODO: Finish report type 2
        # Report mode 2: random cases
        elif report_mode == 2:
            pass
