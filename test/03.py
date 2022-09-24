#Sathana Laolugsanalerd
a=input();s=t=0;m=1
for i in a:
 if(i.isdigit()):t=m*(abs(t*10)+int(i))
 else:s+=t;m=int(i+'1');t=0
print(s+t)