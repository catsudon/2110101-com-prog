a = input()
b = input()
cnt=0
remove = '''"'(),.'''
for i in remove:
    b=b.replace(i, ' ')
for i in b.split():
    if(a==i):cnt+=1
print(cnt)