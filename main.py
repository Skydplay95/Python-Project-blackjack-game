import random
from art import logo
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(cards):
    """
    Calcul the value of the hands for user and dealer, take list as parameter
    """
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_hand, computer_hand):
    """
    Compare user score and dealer score to determien who wins 
    """
    if user_hand == computer_hand:
        print(
            f"Your hands {user_hand} and dealer have {computer_score} It's a draw"
        )
    elif computer_hand == 0:
        print(
            f"Dealer hands {computer_cards}: {computer_score} Black Jack, You Lose"
        )
    elif user_hand == 0:
        print(
            f"Your hands {user_cards}: {user_hand}, You have a Black Jack, You Win"
        )
    elif user_hand > 21:
        print(f"Your hands {user_cards}: {user_hand}, You bust, It's a lose")

    elif computer_hand > 21:
        print(
            f"Dealer hands {computer_cards}: {computer_hand}, Dealer bust, It's a win for you"
        )
    elif user_hand > computer_hand:
        print(f"You have {user_hand}, Dealer have {computer_hand}, You win")
    else:
        print(f"You have {user_hand}, Dealer have {computer_hand}, You lose")


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_end = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    #while loop to continue the game while wants to draw card or havent bust, or dealer hasn't lose yet
    while not game_end:
        #put the addition of card in a variable
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your card: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        #if user or dealer have a BlackJack end or if user bust
        if user_score == 21 or computer_score == 21 or user_score > 21:
            game_end = True
        else:
            #ask user if he wants to draw new card
            draw_new_card = input(
                "Do you want to draw an another card ? Types 'y' for yes or 'n' for no: \n"
            ).lower()
            #draw a new card
            if draw_new_card == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_end = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(user_score, computer_score)


while input("Do you want to play a new game ? Type 'y' for yes or 'n' for no: "
            ).lower() == 'y':
    clear()
    play_game()
