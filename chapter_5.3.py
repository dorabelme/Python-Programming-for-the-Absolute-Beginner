print("Hello to 'Who is Your Daddy Game', Sumanyu!")

pairs = {"Steven" : "The Rock",
"Thomas": "Robert Jr.",
"Adam": "Adam Braun",
"Richard": "Richard Hendrickson",
"Jared": "Hitler" 
}

print(pairs.keys())
daddy = input("Whose Daddy do you want to know? ")
print(pairs[daddy])

print(
"""
If you want to exit the program, choose 0,
If you want to add a pair, choose 1,
If you want to replace someone, choose 2,
If you want to delete a pair, choose 3!
"""
)

choices = None

choice = int(input("Choice: "))
print()

if choice == 0:
	print("Good-bye")

elif choice == 1: 
	son = input("What is the son's name? ")
	father = input("What is the father's name? ")
	pairs[son] = father
	print(pairs)

elif choice == 2:
	son = input("Which son's father do you want me to change? ")
	father = input("What is the father's name? ")
	pairs[son] = father
	print(pairs)

elif choice == 3:
	son = input("Which son do you want me to delete? ")
	del pairs[son]
	print(pairs)
else:
	print("I can't do that", choice, "doesn't exist!")

