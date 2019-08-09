"""
This is my solution to the interview question at https://www.careercup.com/question?id=5101712088498176
The exercise was to write a script that, when given two strings that are the same except that one string has an extra
character, prints out that character.
"""
import sys


def find_extra_char(longer_string, shorter_string):
    """
    Returns the extra char that longer_string has but shorter_string hasn't got
    :param str longer_string:
    :param str shorter_string:
    :return char:
    """
    i = 0
    for char in longer_string:
        try:
            if not char == shorter_string[i]:
                # if the char is not the same as the one in the same position in the shorter string, it is the extra one
                return char
        except IndexError:
            # if an IndexError occurs, we can assume that the extra char is at the end of the longer string
            return char
        i += 1


def main():
    """
    Gets two strings from sys.argv and prints out the extra character
    :return void:
    """
    try:
        string_one = sys.argv[1]
        string_two = sys.argv[2]
    except IndexError:
        print("Could not find strings. Please call this script like this:")
        print("python3 extra_char_finder <string1> <string2>")
        sys.exit(1)
    if len(string_one) > len(string_two):
        # check which string is the longer one to iterate through it inside the find_extra_char function
        char = find_extra_char(string_one, string_two)
    else:
        char = find_extra_char(string_two, string_one)
    print(char)


if __name__ == '__main__':
    main()

