problem_title = "Sum square difference"
problem_lines = [
    "The sum of the squares of the first ten natural numbers is,",
    "1^2 + 2^2 + ...+10^2 = 385",
    "The square of the sum of the first ten natural numbers is,",
    "(1+2+...+10)^2 = 55^2 = 3025",
    "Hence the difference between the sum of the squares of the first ten nautral numbers and the square of the sum is 3025 -385 = 2640",
    "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."
]


def problem_statement():
    print("Problem Statement:")
    print("\t", problem_title)

    for problem_line in problem_lines:
        print("\t\t", problem_line)

    print("\n\n")


def run():
    number = 100

    sum_of_sq = 0
    num_sum = 0
    sq_of_sum = 0
    for i in range(1, number + 1):
        sum_of_sq += i * i
        num_sum += i
    sq_of_sum = num_sum * num_sum

    print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is", sq_of_sum - sum_of_sq)
