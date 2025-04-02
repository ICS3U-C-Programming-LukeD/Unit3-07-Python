#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: April 2, 2025

# adds random module
import random

# adds math module
import math


def main():
    user_age = str(input("Enter your age: "))
    try:
        user_age = int(user_age)
        if user_age > 25 and user_age < 40:
            print("You can date their daughter")
        else:
            print("You cannot date their daughter")
    except:
        print(user_age, "was not an integer")
    finally:
        print("Have a good day")


if __name__ == "__main__":
    main()
