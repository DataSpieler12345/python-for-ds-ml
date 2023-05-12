def fun(n):
   s = '+'
   for i in range(n):
      s += s
      yield s


for x in fun(2):
   print(x, end='');

