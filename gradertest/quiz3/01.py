n = int(input())
team_to_country = {}
for i in range(n):
    a,b = input().split(' ')
    team_to_country[a] = b

ans_list = []
while True :
    a = input().strip().split(' ')
    if(a==['q']): break
    
    ok = True
    seen_country = dict()
    for team in a:
        if(team not in team_to_country):
            ok = False
            break

        if(team_to_country[team] in seen_country):
            ok = False
            break
        
        seen_country[team_to_country[team]] = True
    
    if ok: ans_list.append("OK")
    else: ans_list.append("Not OK")

for ii in ans_list:
    print(ii)