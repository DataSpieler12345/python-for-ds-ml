def my_fun(n):
   s = '+'
   for i in range(n):
      s += s
      yield s


for x in my_fun(2):
   print(x, end='')

