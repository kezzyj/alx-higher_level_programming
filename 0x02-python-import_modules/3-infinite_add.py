#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""

    import sys

    count = len(sys.argv) - 1
    result = 0
    for index in range(count):
        result += int(sys.argv[index + 1])
    print(f"{result}")
