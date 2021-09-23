problem_title = "Smallest Multiple"
problem_lines = [
    "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.",
    "What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?"
]


def problem_statement():
    print("Problem Statement:")
    print("\t", problem_title)

    for problem_line in problem_lines:
        print("\t\t", problem_line)

    print("\n\n")


def run():
    min_num = 1
    max_num = 20
    series = range(min_num, max_num + 1, 1)
    fac_series = [1]
    combo_num = 1
    for i in range(len(series)):
        i_num = series[i]
        temp_series = fac_series[:]
        while temp_series:
            j_num = temp_series[0]
            new_number = i_num / j_num
            if new_number.is_integer():
                i_num = new_number
            temp_series.pop(0)
        if i_num > 1:
            fac_series.append(i_num)
        combo_num *= i_num
    print("The smallest positive number that is evenly divisible by all the numbers from", min_num, "to", max_num, "is", combo_num)
