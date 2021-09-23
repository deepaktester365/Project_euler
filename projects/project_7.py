import numpy as np

problem_title = "10001st prime"
problem_lines = [
    "By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.",
    "What is the 10001st prime number?"
]


def problem_statement():
    print("Problem Statement:")
    print("\t", problem_title)

    for problem_line in problem_lines:
        print("\t\t", problem_line)

    print("\n\n")


def check_prime(ck_num):
    max_val = int(ck_num**(1 / 2)) + 1
    for i in range(2, max_val):
        if (ck_num / i).is_integer():
            return False
    return True


def check_prime_np(ck_num):
    max_val = int(ck_num**(1 / 2)) + 1
    ck_np = np.arange(2, max_val)
    ck_num_np = np.ones(len(ck_np))
    ck_num_np *= ck_num
    ck_div_np = ck_num_np / ck_np
    ck_div_np_int = ck_div_np.astype(int)
    ck_div_ck = (ck_div_np_int / ck_div_np).astype(int)
    if np.sum(ck_div_ck) > 0:
        return False
    else:
        return True


def run():
    prime_num_loc = 10000
    prime_num_list = []
    num = 2
    while len(prime_num_list) < prime_num_loc:
        if check_prime(num):
            prime_num_list.append(num)

        num += 1

    print("The 10001st prime number is", prime_num_list[-1])
