import itertools
import math

def gen_square_corners():
    corners = [1, 1, 1, 1]
    for i in itertools.count():
        # Generate the corners of the square
        corners[3] = (2 * i + 1) ** 2
        side_length = int(math.sqrt(corners[3]))
        index = 2
        for j in range(1,4):
            corners[index] = corners[3] - j * (side_length - 1)
            index -= 1

        yield corners