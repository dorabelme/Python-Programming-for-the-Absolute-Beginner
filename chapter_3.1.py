# Fortune Cookie Challange


import random

print("What does the fortune cookie tell you today?")
print("Read further if you wanna know...\n\n")

cookie = random.randint(1, 5)

if cookie == 1:
  print("A conclusion is simply the place where you got tired of thinking.")

elif cookie == 2:
  print("A cynic is only a frustrated optimist.")
    
elif cookie == 3:
  print("All your dreams are gonna come true...")
    
elif cookie == 4:
  print("If you look back, you’ll soon be going that way.")

elif cookie == 5:
  print("Hard work pays off in the future. Laziness pays off now.")

else:
    print("Illegal value! You didn't get a cookie today.")


input("\n\nPress the enter key to exit.")


