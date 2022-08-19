a = input()
b = input()
remove = '''"'(),.'''
for i in remove:
    b=b.replace(i, ' ')
cnt=0
for i in b.split():
    if(a==i):cnt+=1
print(cnt)