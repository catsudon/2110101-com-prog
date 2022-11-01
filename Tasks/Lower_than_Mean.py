import numpy as np


def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    score = data[..., 1]*weight[0] + data[..., 2]*weight[1] + data[..., 3]*weight[2]
    # print(score)
    mean = np.mean(score)
    failed = sum(score < mean)
    if( failed == 0 ): print("None")
    else:
        l = [];c=0
        for i in (score < mean):
            if i: l.append(str(data[c,0]))
            c+=1
        print(", ".join(l))

exec(input().strip())
