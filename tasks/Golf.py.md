
# Task: Golf.py

``` py
sum_diff_stroke = sum_stroke = sum_par = 0
for i in range(9):
    par, stroke, select = list(map(int, input().split()))
    sum_par += par
    sum_stroke += stroke
    if(select):
        sum_diff_stroke += min(par+2, stroke)

x = (1.5*sum_diff_stroke - sum_par)*0.8
if(x < 0): x = int(x)-1
else: x = int(x)
y = sum_stroke - x
print('{}\n{}\n{}'.format(sum_stroke, x, y))
```
    