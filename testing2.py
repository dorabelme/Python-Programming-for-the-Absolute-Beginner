starting_number = int(input("What's your starting number?"))
ending_number = int(input("What's your ending number?"))
amount = int(input("What's the amount by which to count?"))

for i in range(starting_number, ending_number, amount):
  print(i)

