filename = input()
f = open(filename, "r")
pattern = input()
a = input()

def check(a,b):
    if(len(a) != len(b)): return False
    for i in range(len(a)):
        if(a[i].lower() == b[i].lower()): continue
        if(b[i] == '?'): continue
        return False
    return True

for path in f:
    cur = ''
    ans = ''
    for ch in path:
        if(ch == '/'):
            if(check(cur, pattern)):ans+=a+'/'
            else:ans+=cur+'/'
            cur = ""
        else:cur+=ch
    ans+=cur
    print(ans)