def o(p):
   def q():
      return '*' * p
   return q


r = o(1)
s = o(2)
print(r() + s())

