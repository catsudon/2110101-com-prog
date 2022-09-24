mp = {}
a = input()

for i in a:
    mp[i] = True

ans = ''

found = False
for i in "0123456789":
    try:
        mp[i]
    except Exception:
        ans+=i+','
        found = True
if (not found):
    print(None)
else :
    print(ans[0:-1])
