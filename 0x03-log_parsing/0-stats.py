#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys


if __name__ == "__main__":

    def print_stat(status_codes, file_size):
        """Prints File size and status code count."""
        print("File size: {}".format(file_size))
        for k, v in sorted(status_codes.items()):
            if v != 0:
                print("{}: {}".format(k, v))

    file_size, count = 0, 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for line in sys.stdin:
            data = line.split(" ")
            try:
                file_size += int(data[-1])
                if data[-2] in status_codes.keys():
                    count += 1
                    status_codes[data[-2]] += 1
                    if (count % 10) == 0:
                        print_stat(status_codes, file_size)
            except:
                continue
        print_stat(status_codes, file_size)
    except KeyboardInterrupt:
        print_stat(status_codes, file_size)
        raise
