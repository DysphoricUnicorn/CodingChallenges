"""
This is my version of a Minesweeper game that is played inside the console.
"""
import random


class MineField:
    spaces = []
    height = 0
    width = 0
    open_spaces = 0
    space_count = 0

    def __init__(self, height, width, mine_count):
        """
        Initializes the playing field and places mines
        :param int height: the height of the field
        :param int width: the width of the field
        :param int mine_count: the amount of mines to place
        """
        self.height = height
        self.width = width
        self.space_count = height * width
        if mine_count > self.space_count:
            # If there would be more mines than there are spaces that would be bad so we prevent it
            mine_count = self.space_count
        for i in range(width):
            # Initialize the playing field
            self.spaces.append([])
            for c in range(height):
                self.spaces[i].append([0, False])
                """
                the first value in the list specifies the amount of adjacent mines, the second is whether or not the 
                tile's value is visible
                """
        b = 0
        while b < mine_count:
            # place mines
            rand_x = random.randint(0, width - 1)
            rand_y = random.randint(0, height - 1)
            if not self.spaces[rand_x][rand_y][0] == 9:
                # make sure there is no mine in the randomly generated spot
                self.spaces[rand_x][rand_y][0] = 9
                b += 1
                for x in range(rand_x - 1, rand_x + 2):
                    for y in range(rand_y - 1, rand_y + 2):
                        if 0 <= y < self.height and 0 <= x < self.width and self.spaces[x][y][0] < 8:
                            # get all adjacent tiles and add one to their value if they don't contain mines
                            self.spaces[x][y][0] += 1
        self.open_spaces = b

    def draw_field(self, alive):
        """
        Display the playing field
        :param alive: Whether or not the player is alive. If they aren't all tiles are displayed
        :return:
        """
        for y in range(-1, self.height):
            to_print = ""
            for x in range(-1, self.width):
                if y == -1:
                    # Print the first line containing the x coordinate
                    if x == -1:
                        to_print += "  "
                    else:
                        to_print += str(x) + " "
                else:
                    if x == -1:
                        # Print the first char in all lines containing the y coordinate
                        to_print += str(y) + " "
                    else:
                        for filler in range(0, x // 10):
                            # Fill up tiles to always be the same width as their corresponding x coordinate
                            to_print += " "
                        if self.spaces[x][y][1] or not alive:
                            # Display the current tile if it was checked or the player is dead
                            to_print += str(self.spaces[x][y][0]) + " "
                        else:
                            # Display a minus otherwise
                            to_print += "-" + " "
            print(to_print)

    def has_won(self):
        """
        Checks if the player has checked all tiles
        :return bool:
        """
        return not self.open_spaces <= self.space_count

    def check_tile(self, x, y):
        """
        Checks the value of a tile and makes it visible.
        Returns False if it contains a bomb and True otherwise.
        :param int x: the x coordinate of the tile
        :param int y: the y coordinate of the tile
        :return bool:
        """
        if self.spaces[x][y][0] == 0:
            self.turn_all_adjacent_zeroes(x, y)
        elif self.spaces[x][y][0] == 9:
            return False
        elif not self.spaces[x][y][1]:
            self.spaces[x][y][1] = True
            self.open_spaces += 1
        return True

    def turn_all_adjacent_zeroes(self, x, y):
        """
        Turns all adjacent tiles with 0 adjacent mines visible
        :param x: The x coordinate of the starting tile
        :param y: The y coordinate of the starting tile
        :return void:
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.open_spaces += 1
            self.spaces[x][y][1] = True
            for i in range(x - 1, x + 2):
                for c in range(y - 1, y + 2):
                    try:
                        if self.spaces[i][c][0] == 0 and not self.spaces[i][c][1]:
                            # recursively also turn all adjacent zero value tiles' adjacent zero value tiles
                            self.turn_all_adjacent_zeroes(i, c)
                    except IndexError:
                        # ignore tiles that don't exist
                        pass


def main():
    """
    The setup for the game and game loop, contained inside a function to avoid global variable declarations
    :return void:
    """
    print("Welcome to Minesweeper.\n")
    print("Please enter how wide you want the field to be")
    width = int(input())
    print("Please enter how high you want the field to be")
    height = int(input())
    print("Please enter how many mines you want placed inside the field")
    mine_count = int(input())
    mine_field = MineField(height, width, mine_count)
    alive = True
    mine_field.draw_field(alive)
    while not mine_field.has_won() and alive:
        check_y = -1
        while 0 > check_y or check_y >= height:
            # if the user enters an invalid value
            print("Which line do you want to check?")
            check_y = int(input())
        check_x = -1
        while 0 > check_x or check_x >= width:
            print("Which position in that line do you want to check?")
            check_x = int(input())
        alive = mine_field.check_tile(check_x, check_y)
        mine_field.draw_field(alive)
    if alive:
        print("Congratulations, you won!")
    else:
        print("Ouch! You've hit a mine.")


main()
