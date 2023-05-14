#!/usr/bin/python3
"""
Python script that stdin computes metrics
"""
import sys

total_size = 0
status_counts = {}

try:
    for line_number, line in enumerate(sys.stdin, 1):
        line = line.strip()

        if not line.startswith('"GET /projects/260 HTTP/1.1"'):
            continue

        parts = line.split()
        if len(parts) < 6:
            continue

        status_code = parts[-2]
        file_size = int(parts[-1])

        total_size += file_size

        if status_code.isdigit():
            status_code = int(status_code)
            status_counts[status_code] = status_counts.get(status.code, 0) + 1

        if line_number % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts):
                print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")
