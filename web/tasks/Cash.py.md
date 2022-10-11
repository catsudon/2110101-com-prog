
# Task: Cash.py

``` py
from functools import reduce
from typing import *


def total(pocket: Dict):
    return reduce(lambda total, x: total+x*pocket[x], pocket, 0)


def take(pocket: Dict, money_in: Dict):
    for k in money_in:
        if (k in pocket):
            pocket[k] += money_in[k]
        else:
            pocket[k] = money_in[k]


def pay(pocket: Dict, amt: int):
    available = pocket.keys()
    clone = pocket.copy()
    paid = {}

    for k in available:
        while amt >= k and clone[k] > 0:
            clone[k] -= 1
            if(k in paid): paid[k]+=1
            else: paid[k]=1
            amt -= k

    if amt != 0: return {}

    for k, v in clone.items():
        pocket[k] = v
    return paid

exec(input().strip())
```
    