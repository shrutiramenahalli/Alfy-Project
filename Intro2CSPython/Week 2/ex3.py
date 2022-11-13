import numpy as np


def input_list():
    num = []
    while 1:
        input1 = input()
        if input1 != " ":
            if input1 != "":
                num.append(input1)
            else: break
        else:
            break
    list_count(num)
    return num


def list_count(num):
    count = 0
    for i in num:
        count += int(i)
    return num.append(str(count))


def monotonic_check(operator, sequence):
    output = []
    for i in range(len(sequence) - 1):
        if operator == '<=':
            if sequence[i] <= sequence[i + 1]:
                output.append(True)
            else:
                output.append(False)

        if operator == '<':
            if sequence[i] < sequence[i + 1]:
                output.append(True)
            else:
                output.append(False)

        if operator == '>=':
            if (sequence[i] >= sequence[i + 1]):
                output.append(True)
            else: output.append(False)

        if operator == '>':
            if (sequence[i] > sequence[i + 1]):
                output.append(True)
            else: output.append(False)
    if False in output:
        return False
    else:
        return True


def check_monotonic_sequence(sequence):
    n = len(sequence)
    up = True
    down = True
    strongup = True
    strongdown = True

    if len(sequence) < 2:
        return [up, strongup, down, strongdown]
    else:
        up = monotonic_check('<=', sequence)
        strongup = monotonic_check('<', sequence)
        down = monotonic_check('>=', sequence)
        strongdown = monotonic_check('>', sequence)
        return [up, strongup, down, strongdown]



def check_monotonic_sequence_inverse(bool_def):
    result = []
    if(bool_def == [True, True, False, False]):
        result = [1, 2, 3, 4, 5, 6, 7, 8]

    elif(bool_def == [True, False, False, False]):
        result = [1, 2, 2, 3]
    elif(bool_def ==[True, False, True, False]):
        result = [1, 1, 1, 1]
    elif (bool_def == [False, False, True, False]):
        result = [3, 2, 1, 1]
    elif (bool_def == [False, False, True, True]):
        result = [7.5, 4, 3.141, 0.111]
    elif (bool_def == [False, False, False, False]):
        result = [1, 0, -1, 1]
    elif (bool_def == [True, True, True, True]):
        result = [0]
    else: return None
    return result


def primes_generator(n):
    primenumbers = []
    count = 2
    while len(primenumbers) < int(n):
        for i in range(2, count):
            if (count % i) == 0:
                count +=1
                break
        else:
            primenumbers.append(count)
            count += 1
    return primenumbers


def is_empty_vector(vec_lst):
    if len(vec_lst) != 0:
        for row in vec_lst:
            if len(row) == 0:
                return True
    return False


def vectors_list_sum(vec_lst : list) -> list:
    if not is_empty_vector(vec_lst):
        num_fields = len(vec_lst[0])
        sum_vector = [sum(vector[i] for vector in vec_lst) for i in range(num_fields)]
    return sum_vector


def calc_the_inner_product(vec_1, vec_2):
    if len(vec_1) == 0 and len(vec_2) == 0:
        return 0

    if len(vec_1) != len(vec_2):
        return None

    v1 = np.array(vec_1)
    v2 = np.array(vec_2)
    dot_product = np.sum(v1 * v2)
    return dot_product


def orthogonal_number(vectors):
    count = 0
    for vector in range(len(vectors)):
        for j in range(vector + 1, len(vectors)):
            if calc_the_inner_product(vectors[vector], vectors[j]) == 0:
                count += 1
    return count

