#import random
import random


def deal_card():
    #create list which contain cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    #return random card from deck
    return random_card


#create lists which will contain draw of user and computer, to compare score
user_draw = []
dealer_draw = []

#add 2 random cards in user_draw and in dealer_draw
for i in range(2):
    user_draw.append(deal_card())
    dealer_draw.append(deal_card())

print(user_draw)
print(dealer_draw)

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this


#calculate score
def calculate_score(cards):
    global user_score, dealer_score

    #check for a blackjack
    if len(user_draw) == 2 and sum(user_draw) == 21:
        return 0
    elif len(dealer_draw) == 2 and sum(dealer_draw) == 21:
        return 0

    #add all items of the list
    return sum(user_draw)
    return sum(dealer_draw)
    #check if user got an ace
    for card in user_draw:
        #if he got one, remove it from the list and replace it by a 1
        if card == 11:
            ##debug changer valeur de 11 par 1 dans list recuperer index de la place ou valeur est 11
            index_draw = user_draw.index(11)
            user_draw.remove(index_draw)
            user_draw.append(1)


calculate_score(user_draw, dealer_draw)


def compare_score(total_user, total_dealer):
    global user_score, dealer_score
    if total_user > 21:
        for card in user_draw:
            if card == 11:
                ##debug changer valeur de 11 par 1 dans list recuperer index de la place ou valeur est 11
                index_draw = user_draw.index(11)
                user_draw[index_draw] = 1
                print(user_score)


compare_score(user_score, dealer_score)
""""
    if user_result == 21:
        print("You have a blackjack, bank has lose")
    elif dealer_result == 21:
        print("Bank have a blackjack, you has lose")
    else:
        compare_amount(user_result, dealer_result)

def compare_amont(total_user, total_dealer):
    if total_user > 21:
        print(f"Total of {user_result}, you bust, it's a loose :(")
    elif total_user < 21:
        redraw = input(
            "Do you want an another card ? Type 'y' for yes, 'n' for no: \n"
        ).lower()

        if redraw == 'y':
            user_card3 = random.choice(cards)
            user_draw.append(user_card3)
            card_calcul()
            compare_amont(total_user, total_dealer)

    elif total_user <= 21 and total_user > total_dealer:
        print("You win")
    elif total_user <= 21 and total_user < total_dealer:
        print("You lose")
    else:
        print("nnn")


compare_amont(user_result, dealer_result)
"""
