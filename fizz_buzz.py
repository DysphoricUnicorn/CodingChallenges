import sys


class FizzBuzz:
    """
    It's FizzBuzz. Everybody knows FizzBuzz, which is why it's no longer used in interviews (hopefully).
    I've included my solution to it because it wasn't any difficult to do so and only took very little time.
    It has the tiny "twist" that users can supply start and end values.
    """
    @staticmethod
    def do_fizz_buzz(starting_point, ending_point):
        """
        Calculates the outputs for FizzBuzz
        :param int starting_point:
        :param int ending_point:
        :return list:
        """
        return_list = []
        for i in range(starting_point, ending_point):
            to_print = ""
            if i % 3 == 0:
                to_print = "Fizz"
                # if the current number is a multiple of 3 start by saying to_print should be Fizz
            if i % 5 == 0:
                to_print += "Buzz"
                # if it is a multiple of 5 add Buzz to the already existing string
            if to_print == "":
                to_print = i
                # if the string is empty (since the number is not a multiple of 5 or 3) replace it with the current num
            return_list.append(to_print)
        return return_list


try:
    starting_point_input = int(sys.argv[1])
    ending_point_input = int(sys.argv[2])
except ValueError:
    print("[ERROR] You supplied something that couldn't be converted to an integer.")
    sys.exit(1)
except IndexError:
    print("[ERROR] You didn't supply start and/or end values. Please call this script like this:")
    print("python3 fizz_buzz.py <start_val> <end_val>")
    sys.exit(1)

fizzy = FizzBuzz()
for print_this in fizzy.do_fizz_buzz(starting_point_input, ending_point_input):
    print(print_this)
