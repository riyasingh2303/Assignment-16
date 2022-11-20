tuple1 = ("Python",[10,20,30],[2,4,16])

for i in range (len(tuple1)):
    if type(tuple1[i]) == list:
        for m in range(len(tuple1[i])):
            if tuple1[i][m]==20:
                print(tuple1[i][m],":",m)