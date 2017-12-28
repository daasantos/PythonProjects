#!/usr/bin/env python3
# python3.5.3


def factorial(n: int) -> int:
    """ Calculate factorial with recursion """

    if n > 1:
        return n * factorial(n-1)
    elif n < 0:
        return -1  # Invalid value
    else:
        return 1  # 0! and 1! = 1


def main():
    while True:
        fac = input("Enter a positive number to calculate"
                    " the resulting factorial or a letter to quit.\n")
        if not fac.isnumeric():
            print("Quiting...")
            raise SystemExit
        result = factorial(int(fac))
        print("{0}!= {1}".format(fac, str(result))) if result != -1 else print("Invalid value. "
                                                                               "Enter a non-negative number.")


if __name__ == "__main__":
    main()
