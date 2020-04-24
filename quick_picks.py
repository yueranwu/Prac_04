"""
CP1404
This program generate lines with 6 random numbers according to user input line numbers
Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
"""
import random


def main():
    picks = generate_quick_picks()
    print_picks(picks)


def print_picks(picks):
    index1 = 0
    while index1 < len(picks):
        index2 = 0
        while index2 < 6:
            print("{:<2}".format(picks[index1][index2]), end=' ')
            index2 += 1
        index1 += 1
        print("")


def generate_quick_picks():
    number = int(input("How many quick picks? "))
    lines = []  # create an empty list to store list of picks
    while len(lines) < number:
        picks = []  # create an empty list to store picks
        while len(picks) < 6:
            pick= random.randint(1, 46)
            if pick not in picks:  # no repeat numbers
                picks.append(pick)
        picks.sort()  # sort the list in ascending order
        lines.append(picks)  # append the list to the list
    return lines


main()
