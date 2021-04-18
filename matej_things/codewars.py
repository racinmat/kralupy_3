from typing import List

import a_file
import datetime


def main():
    print("Hello, world")
    a = "a"
    print(a)
    a = 5
    print(a)
    a = {"b": "c"}
    print(a)


def multiply_by_two(x):
    return x * 2


def subtract_numbers(a, b):
    return a - b


def fun():
    return 1, 2, 3, 4, 5


def print_things(arg1="argument 1", arg2="argument 2", arg3="argument 3", arg4="argument 4"):
    print("arg1:" + arg1 + ", arg2:" + arg2 + ",arg3:" + arg3 + ",arg4:" + arg4)
    print(f"arg1:{arg1}, arg2:{arg2},arg3:{arg3},arg4:{arg4}")


def lifePathNumber(dateOfBirth: str):
    print(f"funkce lifePathNumber se zavolala s argumentem {dateOfBirth} typu {type(dateOfBirth)}")
    year_number = sum(map(int, dateOfBirth[0:4]))
    month_number = sum(map(int, dateOfBirth[5:7]))
    day_number = sum(map(int, dateOfBirth[8:10]))
    total_number = sum(divmod(year_number + month_number + day_number, 10))
    return total_number


# Given the birthdates of two people, find the date when the younger one is exactly half the age of the other.
#
# Notes
# The dates are given in the format YYYY-MM-DD and are not sorted in any particular order
# Round down to the nearest day
# Return the result as a string, like the input dates


def date_diff(bd1, bd2):
    d1 = datetime.datetime.strptime(bd1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(bd2, '%Y-%m-%d')
    older, younger = (d1, d2) if d1 < d2 else (d2, d1)
    days_diff = younger - older
    the_day = younger + days_diff
    return the_day


if __name__ == '__main__':
    # main()
    # print(multiply_by_two(2))
    # print(subtract_numbers(b=2, a=1))
    # print(subtract_numbers(1, 2))
    # print(subtract_numbers(1, b=2))
    # print(subtract_numbers(1, 2))
    # print_things(arg4="parametr 4")
    print(date_diff(bd1="1990-10-05", bd2="2000-05-07"))
    print(lifePathNumber("1879-03-14"))
    arr = [1, 2, 3, 4]
    for key in range(len(arr)):
        print(key, arr[key])
    for key, val in enumerate(arr):
        print(key, val)

    arr = [1, 2, 3, "string", [4, 5, 6], (1, 2)]
    [i + 1 if type(i) == int else i for i in arr]

    a_set = {1, 2, 3, 5}
    my_strings = ["string 1", "můj dlouhý string", """
    toto je víceřádkový string, very pythonic, much wow
    """]
    string_lengths = {i: len(i) for i in my_strings}
    list(map(multiply_by_two, [1, 2, 3, 4]))
    list(map(lambda x: x * 2, [1, 2, 3, 4]))
    list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
    sum(map(lambda x: x * 2, [1, 2, 3, 4]))
    sum(map(int, "1234"))

    # for i in "1879":
    #     print(i)
    # sum([int(i) for i in "1879"])
    #
    # [i*2 for i in arr if i % 2 == 0]

    # new_arr = []
    # for i in arr:
    #     if i % 2 == 0:
    #         new_arr.append(i * 2)

    # array[from:to)
    # lifePathNumber(5)
