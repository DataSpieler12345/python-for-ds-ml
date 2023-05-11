def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Failed division")
        n = None
    else:
        print("Everything went well")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))
    