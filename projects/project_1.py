problem_title = "Multiples of 3 or 5"
problem_lines = [
    "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.",
    "Find the sum of all the multiples of 3 or 5 below 1000."
]


def problem_statement():
    print("Problem Statement:")
    print("\t", problem_title)

    for problem_line in problem_lines:
        print("\t\t", problem_line)

    print("\n\n")


def sum_of_multiples(num, mul_of):
    num_of_muls = int((num - 1) / mul_of)
    return mul_of * (num_of_muls) * (num_of_muls + 1) / 2


def run():
    number = 1000
    mul_3 = sum_of_multiples(number, 3)
    # print("Sum of multiples of 3", mul_3)

    mul_5 = sum_of_multiples(number, 5)
    # print("Sum of multiples of 5", mul_5)

    mul_15 = sum_of_multiples(number, 15)
    # print("Sum of multiples of 15", mul_15)

    ans = mul_3 + mul_5 - mul_15

    print("The sum of all the multiples of 3 or 5 below 100 is", ans)
