
# Task: AddVector.py

``` py
a = input().strip('[]').split(', ')
b = input().strip('[]').split(', ')
a = list(map(float,a))
b = list(map(float,b))

print('{} + {} = {}'.format(a, b, list(map(lambda x, y: x+y, a, b))))
```
    