"""
This is my attempt at simulating a randomness calculation problem. The problem is as follows:
A frog is attempting to cross a pond. The pond has many lilly pads, on which the frog can jump, floating on it.
The frog always jumps a random number of lilly pads that is at least 1 and at most the size of the pond, reaching the
last pad.
How many jumps does it take on average for the frog to reach the end of the pond?
"""
import random
from builtins import input, int, ValueError, range, str


class Pond:
    """
    Stores the pond and frog positions
    """
    size = None
    frog_position = None

    def __init__(self, size):
        self.size = size
        self.frog_position = 0

    def has_reached_end(self):
        """
        Checks if the frog has reached the end of the pond.

        :return bool:
        """
        return self.frog_position == self.size

    def do_hop(self):
        """
        Gets a random number between the current position of our frog and the pond's size. The frog will then "jump"
        to that position.

        :return void:
        """
        self.frog_position = random.randint(self.frog_position + 1, self.size)
        print("Frog is not at position " + str(self.frog_position) + " of " + str(self.size))


def main():
    print("How large is the pond?")
    pond_size = input()
    try:
        pond_size = int(pond_size)
    except ValueError:
        print("Malformed input. Please only enter integers. Assuming the default of 10.")
        """
        For simplicity I decided to just use default values when malformed input is encountered..
        Good I/O is not really part of this exercise and this makes it easy to just keep on repeating with the default
        values
        """
        pond_size = 10
    print("How often do you want to simulate the crossing?")
    sim_count = input()
    try:
        sim_count = int(sim_count)
    except ValueError:
        sim_count = 100
        print("Malformed input. Please only enter integers. Assuming the default of 100.")
    total_jumps = 0
    for c in range(0, sim_count):
        """Creates sim_count ponds and simulates the frog jumping for each one"""
        pond = Pond(pond_size)
        while not pond.has_reached_end():
            pond.do_hop()
            total_jumps += 1
    print("The average amount of jumps in " + str(sim_count) + " runs was: " + str(total_jumps / sim_count))


if __name__ == "__main__":
    main()
