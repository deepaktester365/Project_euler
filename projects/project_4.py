import math
import numpy as np

problem_title = "Largest Palindrome Product"
problem_lines = [
    "A palindrome number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.",
    "Find the largest palindrome made from the product of two 3-digit numbers."

]


def problem_statement():
    print("Problem Statement:")
    print("\t", problem_title)

    for problem_line in problem_lines:
        print("\t\t", problem_line)

    print("\n\n")


def get_digit_numbers(num_of_digits):
    start = 10 ** (num_of_digits - 1) - 1
    end = 10 ** (num_of_digits) - 1
    return range(end, start, -1)


def check_palindrome(number):
    num_list = [i for i in str(number)]
    nl = len(num_list)
    for i in range(math.ceil(nl / 2)):
        if num_list[i] != num_list[(nl - 1) - i]:
            return False
    return True


def check_palindrome_list(main_list):
    pal_list = []
    for number in main_list.ravel():
        check = True
        num_list = [i for i in str(number)]
        nl = len(num_list)
        for i in range(math.ceil(nl / 2)):
            if num_list[i] != num_list[(nl - 1) - i]:
                check = False
                break
        if check:
            pal_list.append(number)
    return np.asarray(pal_list)


def get_products(series):
    nl = len(series)
    series_1 = np.zeros((nl, nl), int)
    series_1[0] = series
    series_2 = np.zeros((nl, nl), int)
    series_2[:, 0] = series
    product = np.matmul(series_2, series_1)
    return product


def run():
    digits = 3

    series = get_digit_numbers(digits)

    largest_palindrome = 0
    for i in series:
        for j in series:
            pro = i * j
            if pro > largest_palindrome:
                if check_palindrome(pro):
                    largest_palindrome = pro

    print("The largest palindrome made from the product of two 3-digit numbers is", largest_palindrome)


def run_brute_force_np():
    digits = 1

    series = get_digit_numbers(digits)

    products = get_products(series)

    pal_list = check_palindrome_list(products)

    print("The largest palindrome made from the product of two 3-digit numbers is", pal_list.max())
