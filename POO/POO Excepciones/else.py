def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Failed division")
        return None
    else:
        print("Everything went well")
        return n


print(reciprocal(2))
print(reciprocal(0))