import sys


def is_subsequence(word, of, word_length):
    """
    Checks if word is a subsequence of of.
    :param string word:
    :param string of:
    :param int word_length:
    :return bool:
    """
    i = 0
    c = 0
    found = True
    of_len = len(of)
    while i < word_length and word_length - i >= of_len - c and found:
        """
        Iterate through word but stop once it's clear that it is no subsequence either because a char was not found or
        the remaining amount of chars in of is smaller than the amount of remaining chars in word
        """
        found = False
        while c < of_len and not found:
            # iterate through of starting at the char after the last found char or 0
            if of[c] == word[i]:
                found = True
            c += 1
        i += 1
    return found


def find_largest_subsequence(input_string, input_word_list):
    """
    This function returns the longest word inside the input_word_list that is a subsequence of input_string.
    It is my solution to
    https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/#!
    where that was asked for.
    :param input_string:
    :param input_word_list:
    :return string:
    """
    largest_len = 0
    largest_match = ""
    for word in input_word_list:
        word_length = len(word)
        # iterate through the word list
        if word_length > largest_len:
            # if there already was a match that's longer than this word, checking if it is a subsequence is useless
            if is_subsequence(word, input_string, word_length):
                # we only care about words that are subsequences of input_string
                largest_len = word_length
                largest_match = word
    return largest_match


def main():
    """
    Get user input and catch errors on bad input.
    This is inside a function to avoid global variable declaration.
    I know in my solutions for other exercises I did not do it that way because some people dislike it.
    Doing this I'm trying to prove I am able of 'code switching', depending on what is asked from me.
    I'm calling the word list dictionary inside the error handling because it was called dictionary in the exercise.
    Calling it that way inside the python code would be confusing because it is of the data type list and not, in fact,
    a dictionary in the python sense.
    :return void:
    """
    try:
        input_string = sys.argv[1]
        input_word_list = sys.argv[2].split(",")
    except IndexError:
        print("[ERROR] You didn't supply a string or dictionary. Please use this script like this:")
        print("python3 largest_subsequence.py <string> <dictionary_as_csv>")
        sys.exit(1)
    largest_subsequence = find_largest_subsequence(input_string, input_word_list)
    if largest_subsequence == "":
        print("None of the words inside your dictionary are a subsequence of your string")
    else:
        print("The largest match is:")
        print(largest_subsequence)


main()
