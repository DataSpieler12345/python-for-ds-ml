class Mouse:
    pass
 
 
mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey) # print "False True".