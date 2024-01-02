"""
Problem Statement:
Write a Python program to do arithmetical operations addition and division.
"""


def solution():
    number1 = float(input("Enter 1st number:"))
    number2 = float(input("Enter 2nd number:"))
    while number2 == 0.0:
        number2 = float(input("It can't be zero. Again enter 2nd number:"))
    sum = number1 + number2
    division = number1 / number2
    print(f"sum = {number1} {sum}")
    pass


if __name__ == '__main__':
    solution()
