# exercise 4
#Obtain the final price to be paid if the 36% discount is applied to the total purchase price

initial_price = float(input("Enter the price to be paid: "))
discount = initial_price*(36/100)
final_price = initial_price - discount
print(f"The final price to be: {final_price:.2f}")
