#!/usr/bin/python
import sys
import math


def do_second(n, i0, i1):
    if i0 > i1 or n < 1 or i0 < 0 or float(i0) != int(i0) or float(i1) != int(i1):
        sys.exit(84)
    k = 1.00
    og = i0
    while (k < 4.00):
        i = 1
        x = float(n)
        while (i < i0):
            x = k * x * ((1000 - x) / 1000)
            i += 1
        while (i0 <= i1):
            print("%.2f %.2f" % (k, x))
            x = k * x * ((1000 - x) / 1000)
            i0 += 1
        i0 = og
        k += 0.01
    return (0)
#induivuial 1 i0 can be 0 and ii 0 and 2000 thing


def error_handling():
    try:
        for i in range(1, len(sys.argv)):
            float(sys.argv[i])
        if (int(sys.argv[1]) != float(sys.argv[1])):
            return (1)
        return (0)
    except ValueError:
        return (1)


def k_given():
    tmp = 0
    k = float(sys.argv[2])
    nb = float(sys.argv[1])
    if k < 1 or 4 < k or nb < 0:
        sys.exit(84)
    for i in range(1, 101):
        print("%i %.2f" % (i, nb))
        tmp = nb
        nb = k * tmp * ((1000 - tmp) / 1000)


def print_help():
    print("USAGE")
    print("    ./106bombyx n [k | i0 i1]")
    print("\nDESCRIPTION")
    print("    n      number of first generation individuals")
    print("    k      growth rate from 1 to 4")
    print("    i0     initial generation (included)")
    print("    i1     final generation (included)")
    sys.exit(0)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print_help()
    elif (len(sys.argv) == 3 or len(sys.argv) == 4) and error_handling() == 0:
        if len(sys.argv) == 3:
            k_given()
        elif len(sys.argv) == 4:
            do_second(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    else:
        exit(84)


main()