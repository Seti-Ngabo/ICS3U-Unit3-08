#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program tells you if the year is a leap year


def main():
    # this function checks if year is divisible by 4,100 and 400

    # input
    user_input_string = input("Enter the number of the year (integer): ")
    print("")

    # process and output
    try:
        user_input_number = int(user_input_string)
        if user_input_number % 4 == 0:
            if user_input_number % 100 == 0:
                if user_input_number % 400 == 0:
                    print("{0} is a leap year".format(user_input_string))
                    print("")
                else:
                    print("{0} is a common year".format(user_input_string))
                    print("")
            else:
                print("{0} is a leap year".format(user_input_string))
                print("")
        else:
            print("{0} is a common year".format(user_input_string))
            print("")
    except Exception:
        print("{0} is an invalid input, try again.".format(user_input_string))
        print("")
    finally:
        print("Thanks for checking.")
    print("\nDone.")


if __name__ == "__main__":
    main()
