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
        self.open_spaces = mine_count
        temp_list = []
        for i in range(self.space_count):
            if i < mine_count:
                temp_list.append([9, False])
            else:
                temp_list.append([0, False])
        random.shuffle(temp_list)
        # fill a list with mine_count mines and empty tiles and shuffle it
        i = 0
        for y in range(height):
            self.spaces.append([])
            for x in range(width):
                self.spaces[y].append(temp_list[i])
                i += 1
        # fill the list into the multi-dimensional self.spaces list
        y = 0
        while y < height:
            x = 0
            while x < width:
                if self.spaces[y][x][0] == 9:
                    for i in range(y - 1, y + 2):
                        for c in range(x - 1, x + 2):
                            if 0 <= i < height and 0 <= c < width and self.spaces[i][c][0] < 8:
                                self.spaces[i][c][0] += 1
                x += 1
            y += 1
        # count the adjacent mines for every tile

    def draw_field(self, alive):
        """
        Display the playing field
        :param alive: Whether or not the player is alive. If they aren't all tiles are displayed
        :return void:
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
                        to_print += str(y)
                        for filler in range(0, len(str(self.height - 1)) - len(str(y)) + 1):
                            to_print += " "
                    else:
                        for filler in range(0, len(str(x)) - 1):
                            # Fill up tiles to always be the same width as their corresponding x coordinate
                            to_print += " "
                        if self.spaces[y][x][1] or not alive:
                            # Display the current tile if it was checked or the player is dead
                            to_print += str(self.spaces[y][x][0]) + " "
                        else:
                            # Display a minus otherwise
                            to_print += "-" + " "
            print(to_print)

    def check_tile(self, x, y):
        """
        Checks the value of a tile and makes it visible.
        Returns False if it contains a bomb and True otherwise.
        :param int x: the x coordinate of the tile
        :param int y: the y coordinate of the tile
        :return bool:
        """
        if self.spaces[y][x][0] == 0:
            self.turn_all_adjacent_zeroes(x, y)
        elif self.spaces[y][x][0] == 9:
            return False
        elif not self.spaces[y][x][1]:
            print("uncovered regular tile")
            self.spaces[y][x][1] = True
            self.open_spaces += 1
        else:
            print("You already have uncovered this tile")
        return True

    def turn_all_adjacent_zeroes(self, x, y):
        """
        Turns all adjacent tiles with 0 adjacent mines visible
        :param x: The x coordinate of the starting tile
        :param y: The y coordinate of the starting tile
        :return void:
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            for i in range(x - 1, x + 2):
                for c in range(y - 1, y + 2):
                    if 0 <= i < self.width and 0 <= c < self.height:
                        try:
                            if not self.spaces[c][i][1]:
                                # recursively also turn all adjacent zero value tiles' adjacent zero value tiles
                                self.open_spaces += 1
                                self.spaces[c][i][1] = True
                                if self.spaces[c][i][0] == 0:
                                    self.turn_all_adjacent_zeroes(i, c)
                        except IndexError:
                            # ignore tiles that don't exist
                            pass

    def get_current_play_info(self):
        """
        Returns the amount of tiles that have to be uncovered to win
        :return int:
        """
        return self.space_count - self.open_spaces


def safely_get_int():
    """
    Attempts to get an integer from input and puts out an error message every time the user enters something wrong
    :return int:
    """
    ret = None
    while ret is None:
        try:
            ret = int(input())
        except ValueError:
            print("Please only input an integer")
    return ret


def main():
    """
    The setup for the game and game loop, contained inside a function to avoid global variable declarations
    :return void:
    """
    print("Welcome to Minesweeper.\n")
    print("Please enter how wide you want the field to be")
    width = safely_get_int()
    print("Please enter how high you want the field to be")
    height = safely_get_int()
    print("Please enter how many mines you want placed inside the field")
    mine_count = safely_get_int()
    mine_field = MineField(height, width, mine_count)
    alive = True
    mine_field.draw_field(alive)
    current_info = mine_field.get_current_play_info()
    while current_info > 0 and alive:
        print("You still have " + str(current_info) + " tiles to uncover.")
        check_y = -1
        while 0 > check_y or check_y >= height:
            # if the user enters an invalid value
            print("Which line do you want to check?")
            check_y = safely_get_int()
        check_x = -1
        while 0 > check_x or check_x >= width:
            print("Which position in that line do you want to check?")
            check_x = safely_get_int()
        alive = mine_field.check_tile(check_x, check_y)
        mine_field.draw_field(alive)
        current_info = mine_field.get_current_play_info()
    if alive:
        print("Congratulations, you won!")
    else:
        print("Ouch! You've hit a mine.")


main()
