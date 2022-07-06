#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as extra
    import sys
argnum = len(sys.argv) # indicate arguments number
both = sys.argv # keep sys module
if argnum != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    a = int(both[1])
    b = int(both[3])
    if both[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, extra.sub(a, b)))
    elif both[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, extra.mul(a, b)))
    elif both[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, extra.div(a, b)))
    elif both[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, extra.add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
