txt = input("Enter a text  ")

longest = max(txt.split(), key = len)
print(longest)