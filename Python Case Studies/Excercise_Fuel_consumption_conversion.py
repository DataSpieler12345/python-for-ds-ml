# The fuel consumption of a car can be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

# In the USA, it is shown as the number of miles traveled by a car on a gallon of fuel.

# Your task is to write a couple of functions that convert l/100km to mpg (miles per gallon), and vice versa.

# The functions:

# are called liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;

# take one argument (the value corresponding to their names)


# Here is some information to help you:

# 1 mile = 1609.344 meters.
# 1 gallon = 3.785411784 liters.


def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons


def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    liters = 3.785411784
    return liters / km100


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
