import sys
import re


class StringCompression:
    """
    This is my solution to the exercise at https://techdevguide.withgoogle.com/paths/advanced/compress-decompression
    The goal of this exercise was to build a script that can decompress stings in the $number[$string] format, where
    $string is repeated $number times. The main caveat was that it is possible to stack multiple compressed strings into
    one another. (eg 2[xy23[z]y]x) This was solved using recursion.
    """

    regex = re.compile(r"([0-9]*)(\[)([a-z]+)(\])")
    """
    Matches all groups that are to be repeated
    """

    def do_decoding(self, sub_string):
        """
        Decompresses a string
        :param str sub_string:
        :return string:
        """
        for match in re.finditer(self.regex, sub_string):
            # iterate through all instances of repeated groups
            replace_string = match.group(3) * int(match.group(1))
            sub_string = sub_string.replace(match.group(0), replace_string)
            # replace the groups inside my string
        if re.search(self.regex, sub_string):
            # if the replacements caused new groups to be created, run this function over those as well
            sub_string = self.do_decoding(sub_string)
        return sub_string


compressor = StringCompression()
print(compressor.do_decoding(sys.argv[1]))
