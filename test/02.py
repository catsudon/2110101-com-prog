#Sathana Laolugsanalerd
def f1(a,b,c):
 for i in sorted([a,b,c]):
  if(i>0):return i
def f2(a,b,c):
 r=sorted([a,b,c])
 if(r[1]<0):return r[1]
 return r[0]
def f3(a,b,c):return int(str(abs(a+b+c))[0])
def f4(a,b,c):return abs(a+b+c)%10
def main():
 y,z,a,b,c = list(map(int,input().split()))
 try:exec("print(f{}({},{},{}))".format(str(y*2+z+1),a,b,c))
 except:print("Error")
exec(input().strip())
