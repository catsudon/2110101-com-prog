country_to_ancestor = {}
enemy = {}
def disjoint_set(country):
    if(country not in country_to_ancestor 
       or country_to_ancestor[country] == country):
        country_to_ancestor[country] = country
        return country
    else:
        return disjoint_set(country_to_ancestor[country])

while(True):
    a = input()
    if(a == 'End'):break
    
    a = a.split(' ')
    cmd, l = a[0],a[1:]
    
    if(cmd == 'Ally'):
        # find one country that already has an ally
        anc = l[0]
        for country in l:
            country_to_ancestor[disjoint_set(country)] = disjoint_set(anc)
    
    
    if(cmd == 'Enemy'):
        a,b = l
        if disjoint_set(a) not in enemy: enemy[disjoint_set(a)] = [disjoint_set(b)]
        else: enemy[disjoint_set(a)] += [disjoint_set(b)]
        if disjoint_set(b) not in enemy: enemy[disjoint_set(b)] = [disjoint_set(a)]
        else: enemy[disjoint_set(b)] += [disjoint_set(a)]
        
    for k,v in country_to_ancestor.items():
        print(k,":",v)
    for k,v in enemy.items():
        print(k,":",v)
        
    if(cmd == 'Table'):
        ok = True
        for i in range(len(l)):
            main = l[i]
            left = l[i-1]
            right = l[(i+1)%len(l)]
            
            
            
            if(disjoint_set(main) in enemy and disjoint_set(left) in enemy[disjoint_set(main)]):
                ok = False
            if(disjoint_set(main) in enemy and disjoint_set(right) in enemy[disjoint_set(main)]):
                ok= False

            
            # print("main: ",main)
            # if(disjoint_set(main) in enemy):
            #     print()
            # print("L: ",left, disjoint_set(left))
            # print("R: ",right, disjoint_set(right))
            
        if(ok):print("Okay")
        else:print("No")