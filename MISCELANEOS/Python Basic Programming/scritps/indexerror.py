import pdb
x = ['1']
print("hello")

pdb.set_trace()
try:
    y = x[10]
except IndexError:
    print("X wasn't long enough")
except:
    print("I don't know the issue!")

print("hello again")