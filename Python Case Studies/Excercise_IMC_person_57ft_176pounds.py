# Finally, the code is able to answer the question: What is the BMI of a person who is 5'7" tall and weighs 176 lbs?

def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))

# output = BMI = 27.5652 / 57ft / 176 pounds
