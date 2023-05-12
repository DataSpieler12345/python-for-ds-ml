#It looks strange, doesn't it? It is clear that the for loop has no chance to finish its first execution, since the return will break it irrevocably.

#Moreover, invoking the function will not change anything: the for loop will start from zero and break immediately.

#We can say that such a function cannot save and restore its state on subsequent invocations.

#This also means that such a function cannot be used as a generator.

def fun(n):
    for i in range(n):
        return i

