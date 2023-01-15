#!/usr/bin/env python3
# Created by: Venika Sem
# Created on: Jan 2023
# This program passes by reference

from typing import List


def round_off_number(decimal_number: List[float], decimal_places: int) -> None:
    # This function rounds off decimal numbers

    rounded_off = decimal_number[0] * (10**decimal_places)
    rounded_off = rounded_off + 0.5
    rounded_off = int(rounded_off)
    rounded_off = rounded_off / (10**decimal_places)

    decimal_number[0] = rounded_off


def main():
    # this function gets a decimal number how many decimal places it rounds to

    decimal_number = []

    # input
    user_number = input("Enter the number you want to round: ")
    decimal_places = input("Enter how many decimal places you want to round by: ")

    try:
        user_number = float(user_number)
        decimal_places = int(decimal_places)

        decimal_number.append(user_number)

        # calls function
        round_off_number(decimal_number, decimal_places)

        print("\nThe rounded number is {0}".format(decimal_number[0]))

    except Exception:
        print("\nInvalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
