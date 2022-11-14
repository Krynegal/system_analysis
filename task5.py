import copy
import json


def formatting(input):
    res = []
    for i in input:
        if type(i) is str:
            res.append([i])
        else:
            res.append(i)
    print(res)
    return res


def get_map(input):
    m = {}
    unique = [item for sublist in input for item in sublist]
    index = 0
    for i in unique:
        last = input[index][len(input[index]) - 1]
        m[i] = index
        if i == last:
            index += 1
    print(m)
    return m


def search_in_unique(input, i):
    unique = [item for sublist in input for item in sublist]
    return unique[i]


def get_matrix(input):
    input = formatting(input)
    unique = [item for sublist in input for item in sublist]
    print(unique)
    unique_sorted = copy.copy(unique)
    if unique[0].isdigit():
        unique_sorted.sort(key=int)
    else:
        unique_sorted.sort()
    print(unique_sorted)
    matrix = [[0] * 10 for _ in range(10)]
    m = get_map(input)
    for i in unique_sorted:
        last = input[m[i]][len(input[m[i]]) - 1]
        for j in range(0, unique_sorted.index(last) + 1):
            if m[i] >= m[unique_sorted[j]]:
                matrix[j][unique_sorted.index(i)] = 1
    return matrix


def print_matrix(matrix):
    print()
    for i in matrix:
        print(i)


def get_s_matrix(input, matrix1, matrix2):
    res_matrix = [[0] * 10 for _ in range(10)]
    n = len(matrix1)
    s = []
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] == matrix2[i][j] == 1:
                res_matrix[i][j] = 1
            elif i < j:
                s.append([search_in_unique(input, i), search_in_unique(input, j)])
    return res_matrix, s


def task(j_input1, j_input2):
    input1 = json.loads(j_input1)
    input2 = json.loads(j_input2)

    matrix1 = get_matrix(input1)
    print_matrix(matrix1)
    matrix2 = get_matrix(input2)
    print_matrix(matrix2)

    res_matrix, s = get_s_matrix(input1, matrix1, matrix2)
    print_matrix(res_matrix)
    print(s)
