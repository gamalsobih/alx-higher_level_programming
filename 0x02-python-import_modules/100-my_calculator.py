#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(len(sys.argv)) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
        exit()
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]
    if c == "+":
        r = a + b
        print("{:d} + {:d} = {:d}".format(a, b, r))
    elif c == "-":
        r = a - b
        print("{:d} - {:d} = {:d}".format(a, b, r))
    elif c == "*":
        r = a * b
        print("{:d} * {:d} = {:d}".format(a, b, r))
    elif c == "/":
        r = a / b
        print("{:d} / {:d} = {:d}".format(a, b, r))
    else:
        print("Unknown operator. Available operators: +, -, * and / ")
