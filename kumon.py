#!/usr/bin/env python3

import sys
import re


def div(string):
    """
    Divides a by b returning the quotient and the remainder in the Kumon format.
    """

    numbers = re.search(r"^(\d+)\s+(\d+)$", string)
    numerator = int(numbers[1])
    denominator = int(numbers[2])

    return str(numerator // denominator) + 'R' + str(numerator % denominator)


def improper2mixed(string):
    """
    Convert improper fraction to mixed number
    """

    numbers = re.search(r"^(\d+)\s+(\d+)$", string)
    numerator = int(numbers[1])
    denominator = int(numbers[2])

    return f"{numerator // denominator} {numerator % denominator}/{denominator}"


def mixed2improper(string):
    """
    Convert mixed number to improper fraction
    """

    numbers = re.search(r"^(\d+)\s+(\d+)\s+(\d+)$", string)
    whole = int(numbers[1])
    numerator = int(numbers[2])
    denominator = int(numbers[3])

    return f"{whole*denominator + numerator}/{denominator}"


if sys.argv[1] == 'd':
    message = "Please enter the divisor and the dividend (or 'q' to quit):"
    function = div
elif sys.argv[1] == 'i':
    message = "Please enter the numerator and the denominator (or 'q' to quit):"
    function = improper2mixed
elif sys.argv[1] == 'm':
    message = "Please enter the whole number, numerator and the denominator (or 'q' to quit):"
    function = mixed2improper
else:
    print("ERROR!")
    sys.exit()

choice = input(message)
while choice.lower() != 'q':
    print(function(choice))
    choice = input(message)
