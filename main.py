# import task3
#
# reference = [[1, 3], [2, 3, 4, 5], [1], [4, 5], [2, 3, 4, 5]]
#
# with open('data.csv') as file:
#     csvString = file.read()
#     result = task3.task(csvString)
#     print(result == reference)

# with open("inputData.txt", "r") as f:
#     data = f.read()
# print(data)
# print(data.split(";"))
import copy

input1 = [["a"], ["b", "c"], ["d"], ["e", "f", "g"], ["h"], ["i"], ["j"]]
print(input1)
input2 = [["a", "b"], ["c", "d", "e"], ["f"], ["g"], ["i"], ["h", "j"]]
print(input2)


def get_matrix(input):
    unique = [item for sublist in input for item in sublist]
    print(unique)
    unique_sorted = copy.copy(unique)
    unique_sorted.sort()
    print(unique_sorted)
    matrix = [[0] * 10 for _ in range(10)]
    index = 0
    for i in unique_sorted:
        #if i in input[index]:
        last = input[index][len(input[index]) - 1]
        for j in range(0, unique.index(last) + 1):
            matrix[j][unique.index(i)] = 1
        if i == last:
            index += 1
    return matrix


def print_matrix(matrix):
    print()
    for i in matrix:
        print(i)


#matrix1 = get_matrix(input1)
#print_matrix(matrix1)
matrix2 = get_matrix(input2)
print_matrix(matrix2)
