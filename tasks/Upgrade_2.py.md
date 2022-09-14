
# Task: Upgrade_2.py

``` py
grade_chart = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A']
id = []
grade = []

cmd = ""
while(cmd != 'q'):
    cmd = input()
    if(cmd=='q'):break
    sid, sgrade = cmd.split()
    id += [sid]; grade += [sgrade]

gradeup = input().split()
for student in gradeup:
    grade[id.index(student)] = grade_chart[grade_chart.index(grade[id.index(student)])+1]

ans = []

for i in range(len(id)):
    ans+=[(int(id[i]), grade[i])]

ans.sort()
for i,j in ans:
    print(i,j)
```
    