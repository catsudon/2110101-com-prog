
# Task: Roman_Numeral.py

``` py
r2n = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

n2r = [
    (1,"I"),
    (5,"V"),
    (10,"X"),
    (50,"L"),
    (100,"C"),
    (500,"D"),
    (1000,"M")
]

exc = {
    "IV": 4-1-5,
    "IX": 9-1-10,
    "XL": 40-10-50,
    "XC": 90-10-100,
    "CD": 400-100-500,
    "CM": 900-100-1000,
}

def roman2int(roman):
    sum = 0
    for i in exc:
        if i in roman: sum+=exc[i]
    for i in roman: sum += r2n[i]
    return sum

def int2roman(a):
    ans = ''
    for num,rom in n2r[::-1]:
        while(a >= num):
            a-=num
            ans+=rom
    
    rp = [
        ("VIIII", "IX"),
        ("LXXXX", "XC"),
        ("DCCCC", "CM"),
        ("XXXX", "XL"),
        ("IIII", "IV"),
        ("CCCC", "CD")
    ]
    # print(a,ans)
    
    for x,y in rp:
        ans = ans.replace(x,y)
        
    return ans
    
class romanron :
    def __init__(self, r):
        self.roman = r
        self.num = roman2int(r)
    def __lt__(self, rhs):
        return self.num < rhs.num
    def __str__(self):
        return self.roman
    def __int__(self):
        return self.num
    def __add__(self, rhs):
        return romanron( int2roman(self.num + rhs.num) )



t, r1, r2 = input().split() 
a = romanron(r1); b = romanron(r2) 
if t == '1' : print(a < b) 
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b)) 
else : print(str(a + b))
```
    