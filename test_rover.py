import pytest
from model import Rover
from io_functions import run, parse_input

# Test the Rover class __repr__ method
def test_rover_repr():
    rover = Rover(3, 3, "N")
    assert repr(rover) == "(3, 3, N)"


# Test the Mars Rover program
def test_program():

    # Define an input string
    program = """
    5 5
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM
    """
    # Parse the input string into separate lines
    program = parse_input(program)

    # Define the expected output string
    expected_output_string = """
    1 3 N
    5 1 E
    """

    # Format the expected output string
    expected_output = "\n".join(
        line.strip() for line in expected_output_string.split("\n")
    ).strip()

    # Check that the output of 'run' function matches expected output
    assert run(program) == expected_output
