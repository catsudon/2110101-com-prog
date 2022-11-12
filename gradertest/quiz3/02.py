n,m,k = input().split()
n = int(n)
m = int(m)
k = int(k)

name_to_faculty = {}

for i in range(n):
    a,b = input().split()
    name_to_faculty[a] = b

go_vst = {}
for i in range(m):
    a = input().split()
    visitor = a[0]
    visit = []
    for i in range(1,len(a)):
        visit += [a[i]]
    
    go_vst[visitor] = visit
    
for i in range(k):
    a = input().split()
    ans = set()
    st = 1
    for name in a:
        s = set()
        for visitee in go_vst[name]:
          s.add(name_to_faculty[visitee])
        # print(*s,st)  
        if st:
            st = 0
            ans = ans.union(s)
        else:
          ans = ans.intersection(s)
        
    l = list(ans)
    l.sort()
    if(len(l) == 0 ):
        print("None")
    else: print(" ".join(l))
    