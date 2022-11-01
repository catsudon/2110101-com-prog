W=[('AEILNORSTU',1), ('DG',2), ('BCMP',3), ('FHVWY',4), ('K',5), ('JX',8), ('QZ',10)]
a=input().split();b=[]
for i in a:
    s=0
    for j in i:
        for k in W:
            if(j in k[0]):s+=k[1]
    b+=[[-s,i]]
b.sort()
for i in b:
    print(i[1],-i[0])