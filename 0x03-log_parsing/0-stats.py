#!/usr/bin/python3
""" Status Log module  """
import sys


def getLine(line):
    """Get line for stdin """
    split_line = line.split()
    f_size = int(split_line[-1])
    s_code = int(split_line[-2])
    return f_size, s_code


def print_stats(f_size, s_code):
    """ Return output of status code and count"""
    print("File size: {}".format(f_size))
    for code in sorted(s_code_count.keys()):
        print("{}: {}".format(code, s_code_count[code]))


try:
    """"Logs the status codes"""
    line_count = 0
    total_f_size = 0
    s_code_count = {}

    for line in sys.stdin:
        f_size, s_code = getLine(line)

        if f_size is not None and s_code is not None:
            total_f_size += f_size
            s_code_count[s_code] = s_code_count.get(s_code, 0) + 1

        line_count += 1
        if line_count == 10:
            print_stats(total_f_size, s_code)
            line_count = 0

except Exception as e:
    pass
finally:
    print_stats(total_f_size, s_code)
