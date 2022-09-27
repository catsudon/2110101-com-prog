n = input()
a = "'\".,@!#$%^&*()_+-=:;?<> "
camal = 0
ans = ''
for i in n:
    if(i in a):
        camal = 1
    else:
        ans+=i.upper() if camal else i.lower()
        camal=0
print(ans[0].lower()+ans[1:])