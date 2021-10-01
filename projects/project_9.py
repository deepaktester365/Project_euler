problem_title = "Special pythagorean triplet"
problem_lines = [
    "A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,",
    "a^2 + b^2 = c^2",
    "For example, 3^3 + 4^2 = 9+ 16 = 25 = 5^2",
    "There exists exactly one Pythagoran triplet for which a + b + c = 1000."
    "Find the product abc."
]


def problem_statement():
    print("Problem Statement:")
    print("\t", problem_title)

    for problem_line in problem_lines:
        print("\t\t", problem_line)

    print("\n\n")


def just_loop(num_sum):
    num_prod = None
    i_max = int((num_sum / 3) + 1)
    for i in range(i_max):
        j_max = int(((2 * num_sum) / 3) + 1)
        for j in range(i + 1, j_max):
            k_max = int(num_sum + 1)
            for k in range(j + 1, k_max):
                if (i + j + k == num_sum):
                    if ((i * i) + (j * j)) == k * k:
                        return i * j * k


def better_loop(num_sum):
    num_prod = None
    i_max = int((num_sum / 3) + 1)
    for i in range(1, i_max):
        j_max = int(((2 * num_sum) / 3) + 1)
        for j in range(i + 1, j_max):
            k = num_sum - (i + j)
            if k > j:
                if ((i * i) + (j * j)) == k * k:
                    return i * j * k


def run():
    num_sum = 1000
    # num_prod = just_loop(num_sum)
    num_prod = better_loop(num_sum)

    print("The product is", num_prod)
