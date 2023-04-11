class Rover:
    def __init__(self, x, y, direction):
        # Initialize Rover object with x and y coordinates and a direction
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        # Return a string representation of the Rover object
        return f"({self.x}, {self.y}, {self.direction})"

    def __eq__(self, other):
        # Compare two Rover objects
        if isinstance(other, Rover):
            return (
                self.x == other.x
                and self.y == other.y
                and self.direction == other.direction
            )
        return False


def turn(rover, action):
    # Turn the rover left or right
    compass = "NESW"
    index = compass.index(rover.direction)
    if action == "L":
        index = (index + 3) % 4
    elif action == "R":
        index = (index + 1) % 4
    return Rover(rover.x, rover.y, compass[index])


# Calculate the next position of the rover based on current position and direction
def get_next_position(position, plateau):
    x, y, direction = (
        int(position[0]),
        int(position[1]),
        position[2],
    )  # explicit typecasting unnecessary?

    max_x, max_y = map(int, plateau.split(" "))
    if direction == "N" and y < max_y:
        y += 1
    elif direction == "E" and x < max_x:
        x += 1
    elif direction == "S" and y > 0:
        y -= 1
    elif direction == "W" and x > 0:
        x -= 1
    return str(x), str(y), direction  # explicit typecasting unnecessary?


# Move the rover to the new position
def move(rover, plateau):
    position = (rover.x, rover.y, rover.direction)
    new_position = get_next_position(position, plateau)
    return Rover(*new_position)


# Apply an instruction L/R/M to the rover
def apply(instruction, rover, plateau):
    if instruction in ["L", "R"]:
        return turn(rover, instruction)
    elif instruction == "M":
        return move(rover, plateau)
    else:
        raise ValueError(f"Invalid instruction: {instruction}")


# Execute a series of instructions for the rover
def execute(instructions, rover, plateau):
    result = rover
    for i in instructions:
        if i != " ":
            result = apply(i, result, plateau)
    return result


# Return a string representation of the rover's state : try and remember why this is needed!!
def print_rover(state):
    return f"{state.x} {state.y} {state.direction}"


# Create an initial rover state based on the current position
def initial_state(position):
    x, y, direction = position.split(" ")
    rover = Rover(int(x), int(y), direction)
    return rover
