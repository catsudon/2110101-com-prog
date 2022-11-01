color_file = open(input(),'r')
lyrics_file = open(input(),'r')

color_list = []
for i in color_file:
    color_list += i.strip().split()

for i in range(len(color_list)): color_list[i] = color_list[i].lower()

for i in lyrics_file:
    i=i.strip()
    for j in color_list:
        x=i.lower().find()
        # print(i[x:x+len(j)])
        if(x != -1): i=i.replace(i[x:x+len(j)], "<{}>{}</>".format(j, i[x:x+len(j)] ))
    print(i)