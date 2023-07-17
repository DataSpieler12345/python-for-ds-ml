def addfive(innumber):
    result = innumber + 5
    return result

#The above code doesn't run until it is called
#We call it twice below, resetting x for the second call
x = 5
print(addfive(x))
x = 50
print(addfive(x))

#If we try to print innumber or result it will fail, as it is a local var