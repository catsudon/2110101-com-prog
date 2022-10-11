def reverse(d):
    new = {}
    for key in d: new[d[key]] = key
    return new

def keys(d, v):
    ans = []
    for key in d:
        if(d[key] == v):
            ans+=[key]
    return ans

exec(input().strip())  
