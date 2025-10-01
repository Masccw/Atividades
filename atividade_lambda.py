from functools import reduce
#1
print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5])))

#2
print(list(filter(lambda x: x % 2 == 0, [10, 15, 20, 25, 30])))

#3
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

#4
print(sorted(["uva", "banana", "maçã", "laranja"], key=lambda x: len(x)))

#5
print(list(map(lambda x: x.capitalize(), ["ana", "pedro", "maria"])))

#6
print(reduce(lambda x, y: x * y, [2, 3, 4, 5]))

#7
print(sorted(["banana", "uva", "maçã", "laranja"], key=lambda x: x[-1]))
