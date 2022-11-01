
# Task: Slicing_and_Element-wise_Op.py

``` py
import numpy as np
def sum_2_rows( M ):
    return M[0::2]+M[1::2]

def sum_left_right( M ):
    col_len = M.shape[1]
    l= M[::, 0:col_len//2]
    r= M[::, col_len//2:]
    return l+r
    # just collapse the array
def sum_upper_lower( M ):
    row_len = M.shape[0]
    top = M[:row_len//2,::]
    bot = M[row_len//2:,::]
    return top+bot
def sum_4_quadrants( M ):
    r,c = M.shape
    q1 = M[:r//2, :c//2]
    q2 = M[r//2:, :c//2]
    q3 = M[:r//2, c//2:]
    q4 = M[r//2:, c//2:]
    return q1+q2+q3+q4
def sum_4_cells( M ):
    q1 = M[::2, ::2]
    q2 = M[1::2, ::2]
    q3 = M[::2, 1::2]
    q4 = M[1::2, 1::2]
    return q1+q2+q3+q4
# it's basically
# o x o x     x o x o      x x x x      x x x x
# x x x x  +  x x x x   +  o x o x  +   x o x o
# o x o x  +  x o x o   +  x x x x  +   x x x x
# x x x x     x x x x      o x o x      x o x o
    
def count_leap_years( years ):
    years-=543
    return np.sum((years%400 == 0) | (((years)%4 == 0) & ((years)%100 != 0)) )
exec(input().strip())
```
    