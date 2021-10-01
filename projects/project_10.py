import numpy as np


problem_title = "Summation of primes"
problem_lines = [
    "The sum of the primes below 10 is 2+3+5+7 = 17",
    "Find the sum of all the primes below two million."
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


def sieve_of_eratosthenes(max_num):
    num_list = np.arange(2, max_num)
    max_val = int(max_num**(1 / 2)) + 1

    for i in range(2, max_val + 1):
        max_mult = (max_num / i) + 1
        mult_np = i * num_list[np.where((num_list >= i) & (num_list <= max_mult))]
        num_list = num_list[np.in1d(num_list, mult_np, invert=True)]

    return num_list


def run():
    prime_num_max = 5000000
    prime_num_sum = 0
    num = 2
    prime_num_list = sieve_of_eratosthenes(prime_num_max)
    prime_num_sum = np.sum(prime_num_list, dtype=np.int64)

    print("The sum of all the primes below two million is", prime_num_sum)

    # prime_num_sum = 0
    # for i in range(2, prime_num_max + 1):
    #     if check_prime(i):
    #         prime_num_sum += i
    # if check_prime_np(i):
    #     prime_num_sum += i

    # print("The sum of all the primes below two million is", prime_num_sum)
