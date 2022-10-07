import csv
from io import StringIO


def managment_print(mgmt_list):
    mgmt_dict = {1: "Прямое управление",
                 2: "Прямое подчинение",
                 3: "Опосредованное уравление",
                 4: "Опосредованное подчинение",
                 5: "Coподчинение"}
    for i in range(len(mgmt_list)):
        print(f'{mgmt_dict[i + 1]}: {mgmt_list[i]}')


def process(out):
    rs = [set() for _ in range(5)]
    for i in range(len(out)):
        rs[0].add(out[i][0])
        rs[1].add(out[i][1])
        for j in range(i + 1, len(out)):
            if out[i][1] == out[j][0]:
                rs[2].add(out[i][0])
                rs[3].add(out[j][1])
            if out[i][0] == out[j][0]:
                rs[4].add(out[j][1])
                rs[4].add(out[i][1])
    return rs


def get_result_list(rs):
    r = [list(x) for x in rs]
    for el in r:
        el.sort()
    print(r)
    return r


def parse_edge(line):
    return [int(node) for node in line]


def get_edges(csv_string):
    f = StringIO(csv_string)
    reader = csv.reader(f, delimiter=',')
    edges = [parse_edge(line) for line in reader]
    print(edges)
    return edges


def task(csv_string):
    edges = get_edges(csv_string)
    rs = process(edges)
    managment_print(rs)
    return get_result_list(rs)


if __name__ == '__main__':
    task("1,2\n1,3\n3,4\n3,5\n")
