import pdb

def addlines(lst):
    lst = "\n".join(lst)
    return(lst)

fh = open('test.txt','w+')
mylst = ['hippo','panda','lion','tiger','cat','dog']
pdb.set_trace()

mylst = addlines(mylst)
fh.writelines(mylst)
fh.seek(0)
print(fh.readline())