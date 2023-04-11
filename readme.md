# Mars Rover Project

This project is a Python implementation of the Mars Rover problem. It simulates the movement of a Mars Rover on a plateau, given a set of instructions. The project consists of three source code files: `model.py`, `io_functions.py`, and `test_rover.py`.

## Source Code Files

1. **`model.py`**: This file contains the implementation of the `Rover` class, which represents a Mars Rover, and functions to change the Rover's position and direction based on the provided instructions.

2. **`io_functions.py`**: This file contains functions to parse input, run the Mars Rover program, and generate the output.

3. **`test_rover.py`**: This file contains unit tests for the Rover class and the Mars Rover program. It uses the `pytest` framework to check correctness of the implemented functions and the Rover's __repr__ method.

## Installation and Dependencies

To set up the project and install its dependencies, follow these steps:

1. Make sure you have Python 3.x installed on your system.
2. Download the source code files and requirements.txt file.
3. Create a virtual environment for the project (optional).
4. Install the required dependencies using the command

```
pip install -r requirements.txt
```

## Running Tests

To run the unit tests, simply execute the following command in the project directory:

```
pytest test_rover.py
```

## Usage

You can use the functions in `model.py` and `io_functions.py` to create your own script to run the Mars Rover program, or use them in a larger application.

Here's a example script you could run:

```python
from io_functions import parse_input, run

input_string = """
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
"""

parsed_input = parse_input(input_string)
result = run(parsed_input)
print(result)

This will output the two rovers final positions:

1 3 N
5 1 E


