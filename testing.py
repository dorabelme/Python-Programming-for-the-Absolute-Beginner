#Useless Trivia
#
# Gets personal information from the user and then
# prints true but useless information about him or her

name = input("Hi. What's your name? ")
age = input("How old are you? ")
age = int(age)

weight = int(input("Okay, one last question. How many pounds do you weight? "))

print("\nIf poet ee cummings were to email you, he'd address you as",
	name.lower())
print("But if ee were mad, he'd call you", name.upper())

called = name * 5
print("\nIf a small child were trying to get your attention",)
print("your name would become:")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nYou're over", seconds, "seconds old.")

moon_weight = weight / 6
print("\nDid you know that on the moon you would weigh only",
	mmon_weight, "pounds?")

sun_weight = weight * 27.1
print("On the sun, you'd weight", sun_weight, "(but, ah... not for long).")
