id1, gpax1, comprog1, cal1_1, cal2_1 = input().split() 
id2, gpax2, comprog2, cal1_2, cal2_2 = input().split() 

condition = lambda comprog, cal1, cal2 : comprog == 'A' and ord(cal1) <= ord('C') and ord(cal2) <= ord('C')

qualify_1 = condition(comprog1, cal1_1, cal2_1)
qualify_2 = condition(comprog2, cal1_2, cal2_2)



if(qualify_1 and not qualify_2):print(id1)
elif(qualify_2 and not qualify_1):print(id2)
elif(not qualify_1 and not qualify_2):print("None")
else:
    if(float(gpax1) > float(gpax2)):print(id1)
    elif(float(gpax2) > float(gpax1)):print(id2)
    else:
        sum1 = (100-ord(cal1_1))*100 + (100-ord(cal2_1))
        sum2 = (100-ord(cal1_2))*100 + (100-ord(cal2_2))
        if(sum1 == sum2):print("Both")
        elif(sum1 > sum2):print(id1)
        else:print(id2)