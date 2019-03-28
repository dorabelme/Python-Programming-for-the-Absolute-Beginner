starting_number = int(input("What is your starting number? "))
ending_number = int(input("What is your ending number? "))
amount = int(input("What is the amount by which to count? "))

for i in range(starting_number, ending_number, amount):
	print(i)

