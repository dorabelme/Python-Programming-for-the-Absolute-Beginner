base_price = int(input("What is the base price of your car? "))
dealer_prep = 500
destination_charge = 150
tax = base_price * 0.2
license = base_price * 0.01

actual_price = base_price + dealer_prep + destination_charge + tax + license
print("Your actual price of the car with all extras is", actual_price)