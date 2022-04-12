#1
def Tup(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
tuple= ('a','b' ,'e' ,'c', 'd')
print(tuple)
str = Tup(tuple)
print(str)

#2
tuple1 = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(tuple1)
count = tuple1.count(4)
print(count)

#3
def convert(list):
    return tuple(list)
list = [1, 2, 3, 4]
print(convert(list))

#4


#5
A = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
A = [t for t in A if t]
print(A)

#7
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 )
fifth = a[4]
fifth_last = a[-5]
print(fifth, fifth_last)

#8
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 1}

if set1.isdisjoint(set2):
    print("Set1 and Set2 have no elements in common")
else:
    print("Set1 and Set2 have elements in common")

#9
tup = ("h", "a", "k", "k", "u", "n", "a", "m", "a", "t", "a", "t", "a")
print("h" in tup)
print("k" in tup)

#10
Set1 = {21, 33, 35, 47, 89, 1}
print("Original sets: ", Set1)
print("\n")
print(77 in Set1)
