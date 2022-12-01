#!/usr/bin/python3
import calculator_1 as calc
if __name__ == "__main__":
    a = 10
    b = 5
    print(a, "+", b, "=", "{}".format(calc.add(a, b)))
    print(a, "-", b, "=", "{}".format(calc.sub(a, b)))
    print(a, "*", b, "=", "{}".format(calc.mul(a, b)))
    print(a, "/", b, "=", "{}".format(calc.div(a, b)))
