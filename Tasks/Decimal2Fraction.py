from math import gcd

inp = input()
a,b,c = inp.split(',') 
a = int(a) ## xxxx.yyy.zzz

coef_of_b = len(b)
coef_of_c = len(c)
# if(coef_of_b == 0 and coef_of_c == 0):coef_of_b=len(inp)
# if(coef_of_c == 0):coef_of_c=coef_of_b

try:
    int_of_b = int(b)
except Exception:
    int_of_b = 0
try:
    int_of_c = int(c)
except Exception:
    int_of_c = 0

oct1 = 10 ** coef_of_b 
oct2 = oct1 * (10 ** coef_of_c)

xy_z = a * oct1 + int_of_b ## xxxxyyy.zzz
xyz_z = xy_z * (10 ** coef_of_c) + int_of_c     ## xxxxyyyzzz.zzz

top = xyz_z - xy_z
bot = oct2 - oct1

gcd = max(gcd(top, bot), 1)


print("DEBUG MODE")
print("xy_z", xy_z)
print("xyz_z", xyz_z)
print("oct1", oct1)
print("oct2", oct2)
print("top", top)
print("bot", bot)
print("gcd", gcd)


print(int(top//gcd), '/', int(bot//gcd))
# althrough gcd is confirmed to be divideable
# if we use / operator dividing a very large number
# the result will be in a form like this: 9.841651984980989e+164
# which is judged as wrong by grader