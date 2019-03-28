attributes = {
	"strength": 0,
	"health": 0,
	"wisdom": 0,
	"dexterity": 0
}

pool = 30

while pool > 0:
	attribute = input("Which attribute?: ").lower()

	if attribute not in attributes:
		print("Hey, attribute doesn't exist.")
		continue

	points = int(input("How many points?: "))

	if points > pool:
		print("Hey, you can't do that! Points has to be less than pool: ", pool)
	else:
		current_points = attributes[attribute]
		new_points = points + current_points

		if new_points < 0:
			print("Hey can't use negative points below zero")
		else:
			attributes[attribute] = new_points
			pool -= points

			print("You successfully applied ", points, " points to attribute ", attribute)
			print("Here's the current attributes", attributes)
			print("Current pool", pool)

