import re


def sanitize_map_name(string):
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', string)
