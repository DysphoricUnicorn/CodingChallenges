"""
This is my solution to the interview question at https://www.careercup.com/question?id=5713593060818944
The exercise was to calculate the 10 most viewed videos out of a list of video name - view pairs where video names can
be contained multiple times.
"""


def safely_get_int():
    """
    Gets an int from console.
    Re-prompts every time the user enters something that is not an int until the user inputs a valid one.
    :return int:
    """
    ret = None
    while ret is None:
        try:
            ret = int(input())
        except ValueError:
            print("Could not parse your input Please only enter an integer.")
    return ret


def get_top_10(videos):
    """
    Sorts the dict and turns it into a tuple because python dicts aren't really sortable and returns the top 10
    :param dict videos:
    :return list:
    """
    videos = sorted(videos.items(), key=lambda x: x[1], reverse=True)
    # sort the videos dict by values and return a list of (key, value) tuples
    ret = []
    for i in range(10):
        try:
            ret.append(videos[i][0])
            # We only care about the videos' names so only those are added to the returned list
        except IndexError:
            # If there are less than 10 videos, break out the loop after the last one
            break
    return ret


def main():
    """
    Get the dict of videos and their views from user input and print the top 10 that then is calculated by another
    function
    :return void:
    """
    name_input = "start"
    videos = dict()
    while not name_input == "":
        print("Enter the name for a video. Leave empty once you are done.")
        name_input = input()
        if not name_input == "":
            print("Enter the amount of views the video has gotten.")
            view_input = safely_get_int()
            try:
                # add the amount of views to the video
                videos[name_input] += view_input
            except KeyError:
                # if the video hasn't already gotten any views, add it to the dict
                videos[name_input] = view_input
    top_10 = get_top_10(videos)
    for video in top_10:
        print(video)


main()
