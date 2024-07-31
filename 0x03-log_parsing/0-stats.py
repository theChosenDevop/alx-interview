#!/usr/bin/python3
"""
    Log stats module
"""
import sys

allowed_status_code = {200, 301, 400, 401, 403, 404, 405, 500}


def parse_line(line):
    """Process each line to extract status code
     and file size.
     """
    parts = line.split()
    if len(parts) < 7:
        return None, None

    try:
        f_size = int(parts[-1])
    except ValueError:
        return None, None

    try:
        s_code = int(parts[-2])
        if s_code in allowed_status_code:
            return s_code, f_size
    except ValueError:
        pass

    return None, f_size


def print_stats(total_fs, s_code_count):
    """Prints the accumulated stats.
    """
    print("File size: {}".format(total_fs))
    for code in sorted(s_code_count):
        print("{}: {}".format(code, s_code_count[code]))


def main():
    total_fs = 0
    s_code_count = {}
    line_count = 0

    try:
        for line in sys.stdin:
            s_code, f_size = parse_line(line.rstrip())
            if f_size is not None:
                total_fs += f_size
            if s_code is not None:
                s_code_count[s_code] = s_code_count.get(s_code, 0) + 1

            line_count += 1

            if line_count == 10:
                print_stats(total_fs, s_code_count)
                line_count = 0
    except KeyboardInterrupt:
        print_stats(total_fs, s_code_count)
        raise

    print_stats(total_fs, s_code_count)


if __name__ == "__main__":
    main()
