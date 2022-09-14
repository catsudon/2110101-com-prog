
# Task: Duration.py

``` py
h1, m1, s1, h2, m2, s2 = (int(i) for i in input().split('\n'))
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
weird=False
if(t2<t1):
    weird=True
dt = t2 - t1
dh = dt // (60*60)
dt -= dh * 60*60
dm = dt // 60
dt -= dm*60
ds = dt
if(weird):
    print(str((24+dh)%24)+":"+str((60+dm)%60)+":"+str((60+ds)%60))
else:
    print(str(dh)+":"+str(dm)+":"+str(ds))
```
    