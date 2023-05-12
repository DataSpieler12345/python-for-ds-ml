numbers = [0, 2, 7, 9, 10]

foo = filter(lambda num: num ** 2, numbers)
print(list(foo))


foo = lambda num: num ** 2, numbers
print(list(foo))

foo = map(lambda num: num ** 2, numbers)
print(list(foo))

