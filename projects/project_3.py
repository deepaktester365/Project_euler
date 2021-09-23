problem_title = "Largest Prime Factor"
problem_lines = [
    "The prime factor of 13195 are 5, 7, 13 and 29.",
    "What is the largest prime factor of the number 600851475143?"
]


def problem_statement():
    print("Problem Statement:")
    print("\t", problem_title)

    for problem_line in problem_lines:
        print("\t\t", problem_line)

    print("\n\n")


def get_prime_factors(number):
    prime_factors = []
    test_fac = 2
    while number > 1:
        new_number = (number / test_fac)
        if new_number.is_integer():
            if test_fac in prime_factors:
                number = new_number
            else:
                number = new_number
                prime_factors.append(test_fac)
        else:
            test_fac += 1

    return prime_factors


def run():
    number = 600851475143

    series = get_prime_factors(number)
    # print("The prime factors are", series)

    print("The largest prime factor of the number 600851475143 is", series[-1])
