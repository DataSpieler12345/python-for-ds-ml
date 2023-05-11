import math

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("ok")
finally:
    print("fin")