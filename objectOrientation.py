#!/usr/bin/env python3
# python3.5.3
""" objectOrientation.py - DS - 07/12/17 """


class Dog:

    def __init__(self, name="", height=0, weight=0):
        self.__name, self.__height, self.__weight = name, height, weight

    @property
    def name(self) -> str:
        print("Retrieving name")
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.isalpha():
            self.__name = value
        else:
            print("Please, only letters for name")

    @property
    def height(self) -> str:
        print("Retrieving height")
        return self.__height

    @height.setter
    def height(self, value: str):
        if value.isdigit():
            self.__height = value
        else:
            print("Please, only enter positive numbers for height")

    @property
    def weight(self) -> str:
        print("Retrieving weight")
        return self.__weight

    @weight.setter
    def weight(self, value: str):
        if value.isdigit():
            self.__weight = value
        else:
            print("Please, only enter positive numbers for weight")

    def run(self):
        print("{}, the dog runs.".format(self.name))

    def eat(self):
        print("{}, the dog eats.".format(self.name))

    def bark(self):
        print("{}, the dog barks.".format(self.name))


def main():
    spot = Dog()

    spot.name = input("Enter name: ")
    spot.height = input("Enter height: ")
    spot.weight = input("Enter weight: ")

    spot.bark()
    spot.eat()
    spot.run()

    print("{}, the dog is {} tall and {} kilos", spot.name, spot.height, spot.weight)
    raise SystemExit


if __name__ == "__main__":
    main()
