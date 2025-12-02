input_file = open("./input.txt", "r")
password_array = input_file.readlines()


def password_count(dial:int = 50, passwords:list = password_array) -> tuple:
    """
    Part A: Given a list of inputs from the input.txt file, return the number of times the dial landed on 0 exactly.
    Part B: Given the same list of inputs, return the number of times the dial passes 0 during rotations.
    """
    # Initialize count variables
    part_a_count, part_b_count = 0,0

    for password in passwords:
        # Set modifier to -1 if turning left, otherwise set to 1; L => smaller, R => larger
        modifier = -1 if password[0] == "L" else 1
        # String slice to get the integer form of the rotation number.
        rotation = int(password[1:]) 
        # For every rotation, check if we are passing 0, and if so, increment part_b_count.
        for _ in range(0, rotation):
            # As we have numbers from 0-99, % 100 gives us the current number the dial points to.
            dial = (dial + modifier) % 100
            if dial == 0:
              part_b_count += 1 
        # If we end on 0, increment part_a_count
        if dial == 0:
            part_a_count +=1

    return (part_a_count, part_b_count)

answer_a, answer_b = password_count(50, password_array)

print(f"Part 1 Password Count: {answer_a}\nPart 2 Password Count: {answer_b}")
