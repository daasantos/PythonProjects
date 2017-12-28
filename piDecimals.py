#!/usr/bin/env python3
# python3.5.3
from math import pi

try:
    decimals = int(input("How many decimals should be shown?\n"))
    print("{:.{}f}".format(pi, decimals))
except ValueError:
    print("Invalid value!")
finally:
    raise SystemExit
