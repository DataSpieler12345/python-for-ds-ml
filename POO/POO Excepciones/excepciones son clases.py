try:
    i = int("¡Hi!")
except Exception as e:
    print(e)
    print(e.__str__())
    