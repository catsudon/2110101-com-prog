
# Task: Cut_n_Shuffle.py

``` py
def cut(a):
    llenn = len(a)
    a = a[llenn//2:llenn]+a[0:llenn//2]
    return a
def shuffle(a):
    llenn = len(a)
    f,s = a[llenn//2:llenn],a[0:llenn//2]
    a = []
    for i in range(llenn):
        if(i%2==0):a+=[s[i//2]]
        else:a+=[f[i//2]]
    return a

deck = input().split()
cmd = input()
for i in cmd:
    if(i=='C'):deck=cut(deck)
    if(i=='S'):deck=shuffle(deck)
    
print(" ".join(deck))
```
    