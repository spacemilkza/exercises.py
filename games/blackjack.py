############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
from random import randint

#declare deck
deck = [x for x in range(2, 11)]
deck.extend([10 for x in range(3)])
deck.append(11)

def deal_cards(deck, count=1):
  """func to output any number of cards"""
  return [deck[randint(0, len(deck) - 1)] for x in range(count)]

def sum_cards(deck):
  """function to add up all the card values"""
  sum = 0
  for x in deck:
    sum += x
  return sum

def display_player_cards(player, deck, hidden=False):
  """function to reveal a player's cards on the table"""
  if not hidden:
    print(f"{player}: {deck} = {sum_cards(deck)}")
  else:
    print(f"{player}: [{deck[0]}, X]")
    
#declare and assign players
computer = deal_cards(deck, 2)
player1 = deal_cards(deck, 2)

#display logo and user cards
print(logo)
display_player_cards("Computer", computer, True)
display_player_cards("You", player1)

while sum(player1) < 21:
  while 11 in player1 and sum(player1) > 21:
    #replace 11 with 1
    player1[player1.index(11)] = 1

  hit = input("\nHit or stand? hit=y, stand=n: ").lower().strip()
  if hit == "y":
    player1.extend(deal_cards(deck))
    display_player_cards("You", player1)
  else:
    while sum(computer) < 17:
    	computer.extend(deal_cards(deck))
    display_player_cards("You", player1)
    break

display_player_cards("Computer", computer)
print("\nResults: ", end= "")
if sum(player1) <= 21 and sum(player1) > sum(computer):
  print("You win!!!")
elif sum(player1) <= 21 and sum(computer) > 21:
  print("You win")
elif sum(player1) == sum(computer):
  print("Draw")
else:
 print("Computer wins")

