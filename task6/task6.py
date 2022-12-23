import json
import numpy as np


def get_estimations_matrix(experts, ind):
    num_exp_est = len(experts[ind])
    m = [[0] * num_exp_est for _ in range(num_exp_est)]
    for i in range(num_exp_est):
        for j in range(num_exp_est):
            if experts[ind][i] < experts[ind][j]:
                m[i][j] = 1
            elif experts[ind][i] == experts[ind][j]:
                m[i][j] = 0.5
    return m


def get_k1(m, v1, est_num):
    ones_matrix = [1] * est_num
    y = np.dot(m, v1)
    t = np.dot(ones_matrix, y)
    k1 = np.dot(1 / t, y)
    return k1


def task(input):
    experts = json.loads(input)
    estimations_matrices = []
    for expert in experts:
        expert_index = experts.index(expert)
        estimations_matrix = get_estimations_matrix(experts, expert_index)
        estimations_matrices.append(estimations_matrix)

    m_num = len(estimations_matrices[0])
    m = [[0] * m_num for _ in range(m_num)]
    for i in range(m_num):
        for j in range(m_num):
            for k in range(len(estimations_matrices)):
                m[i][j] += 1 / len(estimations_matrices[k][0]) * estimations_matrices[k][i][j]

    est_num = len(estimations_matrices[0][0])
    v1 = [(1 / est_num) for _ in range(est_num)]
    v2 = get_k1(m, v1, est_num)

    while max(abs(v2 - v1)) >= 0.001:
        v1 = v2
        v2 = get_k1(m, v1, est_num)

    return v2
