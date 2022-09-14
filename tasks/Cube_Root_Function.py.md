
# Task: Cube_Root_Function.py

``` py
from math import sqrt

def sqrt_n_times(x, n):
    for i in range(n):
        x=sqrt(x)
    return x
def cube_root(y):
    exp = (1/(2**2)) * (1 + 1/(2**2)) * (1 + 1/(2**4)) * (1 + 1/(2**8)) * (1 + 1/(2**16))* (1 + 1/(2**32))  
    return(y**exp)
def main():
    q = float(input())
    print(cube_root(q))
exec(input())
```
    