from blackjack_helper import *

# User's turn to play
user_hand = draw_starting_hand("YOUR")
should_hit = "y"
while user_hand < 21:
  should_hit = input(f"You have {user_hand}. Hit (y/n)? ").lower()
  if should_hit == "n":
    break
  elif should_hit != "y":
    print("Sorry I didn't get that.")
  else:
    user_hand = user_hand + draw_card()
print_end_turn_status(user_hand)

# Now, the dealer is to play
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
  print(f"Dealer has {dealer_hand}.")
  dealer_hand = dealer_hand + draw_card()

print_end_turn_status(dealer_hand)


# Finally, the game results
print_end_game_status(user_hand, dealer_hand)
