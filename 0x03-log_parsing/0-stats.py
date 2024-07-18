#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
line_count = 0


def print_stats():
    """Function to print statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Signal handler function for CTRL+C."""
    print_stats()
    sys.exit(0)


# Register signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read from stdin
    for line in sys.stdin:
        line = line.strip()

        # Parse the line using regex
        match_pattern = (
            r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] '
            r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
        )
        match = re.match(match_pattern, line)

        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    # Handle exceptions
    pass

# Print final stats on program exit
print_stats()
