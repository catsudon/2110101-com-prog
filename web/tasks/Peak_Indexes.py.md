
# Task: Peak_Indexes.py

``` py
import numpy as np
def peak_indexes(x):
    L = np.copy(x) # 0 a b c d x
    L = np.delete(L, -1)
    L = np.concatenate(([9999999],L))
    
    
    R = np.copy(x) # x b c d e 0
    R = np.delete(R, 0)
    R = np.concatenate((R,[9999999]))
    
    
    peak = (x>L) & (x>R)

    return np.arange(0, x.size)[peak]
    

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0: print(", ".join([str(e) for e in pos]))
    else: print("No peaks")


exec(input().strip())
```
    