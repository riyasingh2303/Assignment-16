t = (('a',21),('b',37),('c',11),('d',29))
l1 = list(t)
print(l1)
l2 = l1.sort(key=lambda item:item[1])
print(l1)
print(l2)

