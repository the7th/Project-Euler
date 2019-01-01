# This is for problem 2 of ProjectEuler https://projecteuler.net/problem=2
# already checked the solution with others. seems good!
firstNumber = 0
secondNumber = 1
thirdNumber = 1

addedNumber = 0

i = 1

while thirdNumber < 4000000 :
	thirdNumber = firstNumber + secondNumber
	firstNumber = secondNumber
	secondNumber = thirdNumber

	i += 1

	if (thirdNumber%2==0):
		addedNumber = addedNumber + thirdNumber 

print (addedNumber)
