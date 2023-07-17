a = 8
b = 9
c = 10
d = 10
total = 0
today = "Monday"

if a == b:
    print("a is equal to b")

if a != b:
    print("a is not equal to b")
    total += 1

if b+1 == c:
    print("b+1 is equal to c")

if b > 10:
    print("b is greater than 10")

if b <= 9:
    print("b is lessd than or equal to 9")

if today == "Friday":
    print("Have a good weekend")
else:
    print("It's not Friday yet..")

print(total)