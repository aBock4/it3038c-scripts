import time
start_time = time.time()
print('What is your name?')
myName = input()
while myName != 'Wes':
	if myName == 'your name':
		print('This is not "your name". Please type "your name"?')
		myName = input()
	else:
		print('That is not your name. Please, tell me your real name.')
		name = input()

print('Hello, ' + myName + '. That is a good name. How old are you?')
<<<<<<< Updated upstream
myAge = int(input())
if myAge < 13:
	print("Learning young, that's good")
elif myAge==13:
	print("You're a teenager now... that's cool, I guess")
elif myAge>13 and myAge<30:
	print("Still young, still learning…")
elif myAge>=30 and myAge<65:
	print("Now you're adulting.")
else:
	print("... you've lived a long time?")

=======
myAge = input()
if myName < 13:
    print("Learining young, that's good")
elif myAge == 13:
    print("You're a teenager now...that's cool, I guess")
elif myAge > 13 and myAge < 30:
    print("Still young, still learning...")
elif myAge >= 30 and myAge <65:
    pring("Now you're adulting.")
else:
    print("...you've lived a long time?")
>>>>>>> Stashed changes
programAge = int(time.time() - start_time)
print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))
time.sleep(3)
print('I\'m tired. I go sleep sleep now.')