# A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.

# Complicated? Not at all. For example, 8 is not a prime number, since you can divide it by 2 and 4 (we cannot use divisors equal to 1 and 8, since the definition forbids it).

# On the other hand, 7 is a prime number, since we cannot find any divisors for it.

# Your task is to write a function that checks whether a number is prime or not.

# he function:

# is called is_prime;
# takes an argument (the value to check)
# returns True if the argument is a prime number, and False otherwise.

# Hint: try dividing the argument by all subsequent values (starting from 2) and check the remainder - if it is zero, your number cannot be a prime number; carefully analyze when you should stop the process.

# If you need to know the square root of any value, you can use the ** operator. Remember: the square root of x is the same as x0.5.

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
