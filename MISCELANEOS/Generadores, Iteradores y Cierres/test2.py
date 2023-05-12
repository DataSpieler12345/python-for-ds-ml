# We define the lambda function that takes an integer argument and adds 2 to it.
sum_two = lambda x: x + 2

# We use the map() function to apply the lambda function to each element of the list.
result = map(sum_two, [1, 2, 2, 3])

# We convert the result into a string of characters separated by spaces.
result_string = " ".join(map(str, result))

# We print the result in the console
print(result_string)

# We use the map() function to obtain a list with the even elements of the original list.
any_list = [1, 2, 3, 4]
even_list = list(map(lambda x: x if x % 2 == 0 else None, any_list))
even_list = list(filter(lambda x: x is not None, even_list))

# We print the resulting list in the console.
print(even_list)