n = int(input()) - 1
if(n == -1):
    print(0,'\n',0)
    exit()
st = input().split()
a = b = set(st)
while(n):
    st = set(input().split())
    a = a.union(st)
    b = b.intersection(st)
    n-=1

# print(a,b)
print(len(a))
print(len(b))