
# Task: Telephone_Directory.py

``` py
n = int(input())
name_to_num = {}
num_to_name = {}
for i in 'あ'*n:
    a,b,tel = input().split()
    name = a+' '+b
    name_to_num[name]=tel
    num_to_name[tel]=name

q = int(input())
for i in 'あ'*q:
    ans = "Not found"
    key = input()
    try: ans = name_to_num[key]
    except KeyError: pass
    
    try: ans = num_to_name[key]
    except KeyError: pass
    
    print("{} --> {}".format(key,ans))
```
    