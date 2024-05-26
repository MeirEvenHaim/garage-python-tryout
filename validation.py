def is_valid_input(index, length_of):
    return index <= length_of


def is_valid_choice(choice, maxnum):
    return choice <= maxnum


def is_valid_year(year):
    return year >= 1924 and year <= 2023
