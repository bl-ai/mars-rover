from model import initial_state, print_rover, execute

# Parse a multi-line input and split into separate lines.
def parse_input(input):
    lines = input.strip().split("\n")
    return [line.strip() for line in lines]


# Run the Mars Rover program based on the provided input.
def run(program):
    output = []
    plateau = program.pop(0)

    # Get each rover's position and instructions from the array
    while len(program) > 0:
        position, instructions = program[:2]
        program = program[2:]

        # Execute instructions for the current rover
        state = execute(instructions, initial_state(position), plateau)

        # Append the new state of the rover to output
        output.append(print_rover(state))

    # Return final output as a multi-line string
    return "\n".join(output)
