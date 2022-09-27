
# Task: File_Merge.py

``` py
def read_next(f):
    t = f.readline()
    if len(t) == 0:return "", ""
    x = t.strip().split()
    return x[0], x[1]
     

f1,f2 = input().split(' ')
a = []
f1 = open(f1, "r")
f2 = open(f2, "r")

sid,grade=0,0
while(sid!=''):
    sid,grade = read_next(f1)
    a.append([sid[-2:], sid, grade])

sid,grade=0,0
while(sid!=''):
    sid,grade = read_next(f2)
    a.append([sid[-2:], sid, grade])

a.sort()

for i in a:
    print(i[1],i[2])
```
    