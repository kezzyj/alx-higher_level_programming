#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    import sys
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    else:
        operator = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(operator.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        else:

            a = int(sys.argv[1])
            b = int(sys.argv[3])

            print(f"{a} {sys.argv[2]} {b} = {operator[sys.argv[2]](a, b)}")
