
# Task: Bisection_Log10.py

``` py
def ten_pow(x):
    return pow(10, x)

def check(a, powed):
    diff = a-powed
    if(abs(diff) <= pow(10,-10)):
        return True
    return False

a = float(input())
ans = 0
L,U = 0,a

while(L <= U):
    mid = (L+U)/2
    r = ten_pow(mid)
    ck = check(a, r)
   # print("debug ", mid)
    if(ck == True):
        print(round(mid, 6))
        break
    elif(r < a):
        L = mid
    else:
        U = mid
```
    