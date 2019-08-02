"""
This is my solution to the interview question at https://www.careercup.com/question?id=6292672159940608.
The exercise was to seat people on a bench. Every new person is seated as far away from the other people as possible.
"""
import math


class Bench:
    seats = []
    """
    All seats of the bench
    """
    taken_seats = 0
    """
    The amount of seats that are occupied
    """
    seat_count = 0
    """
    The amount of seats
    """
    last_seat = 0
    """
    The amount of seats -1/ The last filled index of the seats list. This is stored because it's commonly used and saves
    some calculations this way
    """

    def __init__(self, seat_count):
        """
        Create the bench and set every seat as empty
        :param int seat_count:
        """
        for i in range(seat_count):
            self.seats.append(False)
        self.seat_count = seat_count
        self.last_seat = seat_count - 1

    def add_person(self):
        """
        Ads a person to the bench.
        If the bench is full returns False and True otherwise
        :return bool:
        """
        if self.taken_seats < self.seat_count:
            current_dist = 0
            longest_dist = -1
            current_seat = 0
            longest_dist_last_seat = 0
            for seat in self.seats:
                if not seat:
                    # if the seat is vacant, add to the current distance
                    current_dist += 1
                    if current_dist > longest_dist:
                        # if the current distance is longer than the previous longest distance save information about it
                        longest_dist = current_dist
                        longest_dist_last_seat = current_seat
                else:
                    # if the seat is occupied, start the distance counting by zero
                    current_dist = 0
                current_seat += 1
            if longest_dist_last_seat < self.last_seat:
                # make sure to first seat people at the start and end of the bench
                sit_here = longest_dist_last_seat - (math.floor(longest_dist / 2))
            else:
                if longest_dist < self.seat_count:
                    # seat a person at the end of the bench
                    sit_here = self.last_seat
                else:
                    # seat a person at the start of the bench
                    sit_here = 0
            print("Sitting down at: " + str(sit_here))
            # this output was wanted by the exercise text
            self.seats[sit_here] = True
            self.taken_seats += 1
            return True
        else:
            return False

    def show_bench(self):
        """
        Displays the current bench.
        Uses Xs to show used spots and _s to display vacant ones
        :return void:
        """
        to_print = "("
        for seat in self.seats:
            if seat:
                to_print += "X"
            else:
                to_print += "_"
        print(to_print + ")")


def safely_get_int():
    """
    Safely gets an integer from console by re-prompting the user until they enter a valid one
    :return:
    """
    ret = None
    while ret is None:
        try:
            ret = int(input())
        except ValueError:
            print("Could not parse your input. Please enter an integer.")
    return ret


def main():
    """
    Asks the user how many seat the bench should have and fills it up.
    :return void:
    """
    print("How many seats do you want your bench to have?")
    bench = Bench(safely_get_int())
    while bench.add_person():
        bench.show_bench()


main()
