"""
This is my solution to the interview question at https://www.careercup.com/question?id=5167719024951296
The goal was to output the largest number inside a list that 1000000 numbers constrained by both smallest and largest
indices.
"""
import random


class ListContainer:
    list = []

    def __init__(self):
        """
        Creates the list and fills it with random numbers
        """
        print("Filling list.. This could take a while.")
        for i in range(1000000):
            self.list.append(random.randint(0, 99999))

    def find_largest(self, start, end):
        """
        Finds the largest number inside the list between start and end indices
        :param int start:
        :param int end:
        :return:
        """
        subset = []
        for i in range(start, end + 1):
            # get all numbers inside the range
            subset.append(self.list[i])
        subset = sorted(subset, reverse=True)
        # sort them high to low and return the highest one
        return subset[0]


def safely_get_int():
    """
    Gets an int between 0 and 99999 from console.
    Re-prompts every time the user enters something that is not an int between 0 and 99999 until they input a valid
    value.
    :return int:
    """
    ret = None
    while ret is None or ret > 999999 or ret < 0:
        try:
            ret = int(input())
        except ValueError:
            print("Could not parse your input Please only enter an integer between 0 and 999999.")
        if ret > 999999 or ret < 0:
            print("Please only enter numbers between 0 and 999999.")
    return ret


def main():
    """
    Prompts the user for ranges and returns the largest number inside them
    :return void:
    """
    continue_input = "start"
    list_container = ListContainer()
    while not continue_input == "n":
        print("Enter smallest index:")
        num_1 = safely_get_int()
        print("Enter largest index:")
        num_2 = safely_get_int()
        if num_2 < num_1:
            print("The largest index cannot be smaller than the smallest one.")
        else:
            print("The largest number in that range is: " + str(list_container.find_largest(num_1, num_2)))
        print("Get another range? Y/n")
        continue_input = input()


main()
