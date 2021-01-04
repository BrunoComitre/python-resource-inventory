s1 = {1, 2, 3, 4, 5}
print(s1)
for v in s1:
    print(v)


s2 = set()
print(s2)
s2.add(1)
s2.add(2)
print(s2)
s2.discard(2)
print(s2)
s2.update('a')
print(s2)
s2.update('Python')
print(s2)
s2.update([1, 2, 3, 4, 5])
print(s2)


l1 = [1,2,3,3,2,54,4,5,6,5,34,1,2]
l1 = set(l1)
print(l1)
l1 = list(l1)
print(l1)


s3 = {1,2,3,4,5}
s4 = {1,2,3,4,5,6}
s5 = s3 | s4  # union
print(s5)
s5 = s3.union(s4)  # union
print(s5)
s5 = s3 & s4  # intersection
print(s5)
s3 = {1,2,3,4,5,7}
s5 = s3 - s4  # difference
print(s5)
s5 = s4 - s3  # difference
print(s5)
s5 = s3 ^ s4  # symetric difference
print(s5)
