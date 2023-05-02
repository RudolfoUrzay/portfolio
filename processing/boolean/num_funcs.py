def is_equal(num_1, num_2):
    return num_1 == num_2

def is_lower(num_1, num_2):
    return num_1 < num_2

def is_grater_than(num_1, num_2):
    return num_1 > num_2

def is_in_range(num, lower_bound, upper_bound):
    return lower_bound <= num <= upper_bound

def is_even(num):
    return num % 2 == 0

def is_ood(num):
    return not is_even(num)

def is_in_list(num, numbers):
    return num in numbers


