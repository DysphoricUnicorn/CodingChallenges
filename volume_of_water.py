import sys


class VolumeOfWater:
    """
    This is my solution to the exercise at: https://techdevguide.withgoogle.com/paths/advanced/volume-of-water/
    The goal of this exercise was to build a script that calculates how much rain water can accumulate on a
    2-Dimensional island. The island has varying heights for all of it's positions, which are supplied inside a list.
    """

    highest_left = 0
    highest_right = 0
    highest_pos = 0
    island_size = 0
    heights = []

    def __init__(self, heights):
        """
        The island's constructor.
        For readability's sake I re-assign all vars
        :param list heights:
        """
        self.heights = heights
        self.island_size = len(heights)
        self.highest_right = self.get_highest_right(0)
        self.highest_left = 0
        self.highest_pos = 0

    def calculate_volume(self):
        """
        Iterate through the heights and check how much water could accumulate on a given spot
        :return int:
        """
        volume = 0
        position = 0
        for this_height in self.heights:
            this_height_int = int(this_height)
            if self.highest_left >= self.highest_right:
                """
                If the highest point on the right side is lower than the one on the left, water would flow out to the 
                right and vice versa
                """
                this_volume = self.highest_right - this_height_int
            else:
                this_volume = self.highest_left - this_height_int
            if this_volume < 0:
                """
                If the spot that is currently looked at is higher than the spots to it's sides, water will not collect
                here because it flows away
                """
                self.highest_left = this_height_int
            else:
                volume += this_volume
            position += 1
            if position >= self.highest_pos:
                """
                If the current position is further to the right than the last highest spot, we have to get the next one
                """
                self.highest_right = self.get_highest_right(position)
        return volume

    def get_highest_right(self, position):
        """
        Calculate the highest point on the island that's right to a given starting position
        :param int position:
        :return int:
        """
        current_highest = 0
        if position < self.island_size:
            highest_pos = 0
            while position < self.island_size:
                height_int = int(self.heights[position])
                if height_int > current_highest:
                    current_highest = height_int
                    highest_pos = position
                position += 1
            self.highest_pos = highest_pos
        return current_highest


volume_of_water = VolumeOfWater(sys.argv[1].split(','))
"""
Take the heights of the island as a csv from console and split them into a list.
In a production env this would have to be sanitized but that's not the point of this exercise.
"""
print(volume_of_water.calculate_volume())
