"""
CP1404 Practical 4
List Exercise
"""


def main():
    numbers = number_list() # function create number lists
    print_numbers(numbers)  # function print the number in the list in a interesting way
    user_verification() # function verify user names
    return 0


def user_verification():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Please enter your username: ")
    verification = False # set default user verification value to False
    for name in usernames:
        if username == name:
            print("Access Granted") # if name matches, grant access
            verification = True
    if not verification:
        print("Access Denied")  # if none of the names matches the user input, deny access


def print_numbers(numbers):
    print("The first number is {}".format(numbers[0])) # print the first number
    print("The last number is {}".format(numbers[-1]))  # print the last number
    print("The smallest number is {}".format(min(numbers))) # print the smallest number
    print("The largest number is {}".format(max(numbers)))  # print the largest number
    average = sum(numbers) / len(numbers)   # calculate the average number in the list
    print("The average of the numbers is {}".format(average))   # print the average number in the list
    print("-------------------------------------------")


def number_list():
    numbers = []  # create an empty list
    while len(numbers) < 5:
        number = int(input("Number: "))
        numbers.append(number)  # add user input number inside the list
    return numbers


main()
