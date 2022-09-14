
# Task: AbbrevNum.py

``` py
inp = input()
llenn = len(inp)
postfix = ['','','','','K','K','K','M','M','M','B','B','B','B','B','B','B']
post = postfix[llenn]

if(llenn < 4):
    print(inp)
elif(llenn > 10):
    num = int(inp[0:llenn-9])
    if int(inp[llenn-9]) >= 5:num+=1
    print(str(num)+'B')

elif(llenn % 3 == 1):
    num = int(inp[0:2])
    if int(inp[2]) >=5:num+=1
    print(str(num)[0]+'.'+str(num)[1]+post)
else:
    lm3 = llenn % 3
    if(llenn % 3 == 0): lm3=3
    num = int(inp[0:lm3])
    if int(inp[lm3]) >= 5:num+=1
    print(str(num)+post)
```
    