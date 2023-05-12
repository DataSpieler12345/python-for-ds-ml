def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)

