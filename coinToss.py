#!/usr/bin/env python3
# python3.5.3
""" coinToss.py - DS - 07/12/17 """
from random import randint


def toss(ntoss: int) -> []:
    head, tail, outcomes = 0, 0, []

    while ntoss > 0:
        if randint(0, 1) == 0:
            outcomes.append("head")
            head += 1
        else:
            outcomes.append("tail")
            tail += 1
        ntoss -= 1

    print("There was a total of {0} heads and {1} tails".format(str(head), str(tail)) + ".")
    print(", ".join(outcomes))
    return outcomes


def main():
    n = 0
    try:
        n = int(input('How many coin tosses should happen?\n'))
    except ValueError:
        print("Invalid value!")
    toss(n)
    raise SystemExit


if __name__ == "__main__":
    main()