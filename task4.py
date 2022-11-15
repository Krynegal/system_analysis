from io import StringIO
import math
import csv


def get_graph(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    graph = []
    for row in reader:
        graph.append(row)
    return graph


def get_arrs(graph):
    a = [[], [], [], [], []]
    for x in graph:
        a[0].append(x[0])
        a[1].append(x[1])
    f, g = graph, graph
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j:
                if f[i][1] == g[j][0]:
                    a[2].append(f[i][0])
                elif f[i][0] == g[j][1]:
                    a[3].append(f[i][1])
                elif f[i][0] == g[j][0]:
                    a[4].append(f[i][1])
    return a


def get_verts(graph):
    verts = []  # количество вершин
    for x in graph:
        for y in x:
            if y not in verts:
                verts.append(y)
    verts.sort()
    return verts


def processing(verts, a):
    res_arr = [[], [], [], [], []]  # результат
    for v in verts:
        for i in range(5):
            res_arr[int(v) - 1].append(a[i].count(v))

    s = 0
    lv = len(verts) - 1
    for j in range(lv + 1):
        for i in range(5):
            r = res_arr[j][i]
            if r != 0:
                s += (r / lv) * math.log(r / lv, 2)
    return -s


def task(csvString):
    graph = get_graph(csvString)
    a = get_arrs(graph)
    verts = get_verts(graph)
    result = processing(verts, a)
    return result
