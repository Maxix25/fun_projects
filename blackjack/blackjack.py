import random
# Initialize game functions
def verify():
	print(
		f"Your hand: {hand}\n",
		f"Bot's hand: {bot_hand}"
		)
	if hand > bot_hand:
		# If the player's hand is greater than the bot's hand, then player wins
		print("You win!")
	elif hand < bot_hand:
		# If the player's and is less than the bot's hand, then player loses
		print("You lose...")
	else:
		# If the player's hand is equal to the bot's hand, then it's a tie
		print("Tie!")
# Initialize game with random cards
print("Welcome to blackjack!")
hand = random.randrange(1,10) * 2
bot_hand = random.randrange(1,10) * 2
print("Current hand:", hand)
while True:
	if hand == 21:
		print("You have a blackjack!")
	if bot_hand == 21:
		print("The bot has a blackjack!")
	choice = input("Do you want to add another card? [y/n]")
	if choice.lower() == "y":
		hand += random.randrange(1,13)
		print("You add one card!")
		print("Current hand:", hand)
		bot_hand += random.randrange(1,13)
		if hand > 21:
			# Player lose
			print("You lose...")
			break
		if bot_hand > 21:
			# Bot lose
			print("You win!")
			break
		continue
	elif choice.lower() == "n":
		print("You don't add another card")
		verify()
		break
	else:
		print("You entered a non-valid response...")
		continue