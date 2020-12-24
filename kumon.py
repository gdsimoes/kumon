#!/usr/bin/env python3

import re


def div(a, b):
    """
    Divides a by b returning the quotient and the remainder in the Kumon format.
    """
    return str(a // b) + 'R' + str(a % b)


def improper2mixed(numerator, denominator):
    """
    Convert improper fraction to mixed number
    """
    return f"{numerator // denominator} {numerator % denominator}/{denominator}"


def mixed2improper(proper, numerator, denominator):
    """
    Convert mixed number to improper fraction
    """
    return f"{proper*denominator + numerator}/{denominator}"


choice = input("Please enter the divisor and the dividend (or 'q' to quit):")
while choice.lower() != 'q':
    numbers = re.search(r"(\d*)\s*(\d*)", choice)
    print(div(int(numbers[1]), int(numbers[2])))
    choice = input(
        "Please enter the divisor and the dividend (or 'q' to quit):")
