#!/usr/bin/env python3
# python3.5.3
""" fileManipulation.py - DS - 07/12/17 """
import os

with open("stuff.txt", mode="w", encoding="UTF-8") as myFile:
    myFile.write("Lemme\nsay \nsome\nstuff\nboi")

with open("stuff.txt", encoding="UTF-8") as myFile:
    print(myFile.read())

raise SystemExit

# for line in myFile
#   print(line)

os.remove("stuff.txt")
# os.rename(old,new) os.remove(name) os.mkdir(name) os.chdir(name) os.getcwd() current directory
