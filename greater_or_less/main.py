import random
import time
from functions import printf
from getpass import getpass
printf("Welcome to the greater or less game!")
time.sleep(.5)
printf("Rules: I'll show you a number and you'll have to guess if the next number is less or greater than the current number")
getpass("Press enter to continue...")
# Generate a number from 1 to 13
while True:
	number = random.randint(1,13)
	next_number = random.randint(1,13)
	choice = input(f"Is the next number greater than {number}? [y/n]")
	if choice.lower() == "y" and number > next_number:
		printf("You did it!")
		print(number)
		print(next_number)
		time.sleep(1)
		continue
	elif choice.lower() == "n" and number < next_number:
		printf("You did it!")
		print(number)
		print(next_number)
		time.sleep(1)
		continue
	else:
		printf("Bad luck...")
		print(number)
		print(next_number)
		break