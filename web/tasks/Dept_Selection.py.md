
# Task: Dept_Selection.py

``` py
depart2num = {}
n = int(input())
for i in '^'*n:
    a,b = input().split()
    depart2num[a] = int(b)



m = int(input())
student_list = []
for i in range(m):
    idx, score, a, b, c, d = input().split()
    hoshii = [a,b,c,d]
    student_list.append([-float(score),idx,hoshii])

student_list.sort()

ans = []

for i in student_list:
    score,idx = -i[0],i[1]
    hoshii = i[2]
    for j in hoshii:
        if(depart2num[j]):
            depart2num[j]-=1
            ans += [(idx, j)]
            break
            
ans.sort()
for i in ans:
    print(" ".join(i))
```
    