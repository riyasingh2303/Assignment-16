tuple1 = (1,2,3,4,5,6)

tuple2 = tuple()
print(tuple2+tuple1[3:-1])
tuple2 = tuple2+tuple1[3:-1]
print(tuple2)