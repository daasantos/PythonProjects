#!/usr/bin/env python3
# python3.5.3


def isHappy(n: str) -> str:
    aux = tries = 0
    while n != "1" and tries < 10 and n not in seen:
        for i in n:
            aux += int(i) ** 2
        n, aux = str(aux), 0
        tries += 1
    if n == "1":
        return "Happy Number!"
    else:
        if n not in seen:
            seen.add(n)
        return "Not a Happy Number."


seen = set()


def main():
    while True:
        num = input("Enter a number to test if it's a Happy Number"
                    " or a letter to quit.\n")
        if not num.isnumeric():
            print("Quitting...")
            raise SystemExit
        print(isHappy(num))


if __name__ == "__main__":
    main()
