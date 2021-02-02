import random

def intro():
    print('''Welcome To BLACKJACK!!!

        Press "r" to view rules.
        Press "c" to continue to game.''')

def rules():
    print('''
    Rules: --> You have to make sure that the sum of your cards is closest to 21 without exceeding it.
           --> If the sum of your cards exceed 21. You lose. 
           --> You can ask for as many cards as you want.
           --> The value of numeric cards is the same as the number on it.
           --> The value of ace ("A") is 1.
           --> The value of King("K"),Queen("Q") and Jack("J") is 10.''')


clubs = ['A','2','3','4','5','6','7','8','9','K','Q','J']
diamonds = ['A','2','3','4','5','6','7','8','9','K','Q','J']
hearts = ['A','2','3','4','5','6','7','8','9','K','Q','J']
spades = ['A','2','3','4','5','6','7','8','9','K','Q','J']
card_list = [clubs,diamonds,hearts,spades]

  
def player_choose():
    card_sym = random.choice(card_list)
    sym_index = -1
    card_sym_st = ""
    if card_sym == clubs:
        card_sym_st = "Clubs"
        sym_index = 0
    elif card_sym == diamonds:
        card_sym_st = "Diamonds"
        sym_index = 1
    elif card_sym == hearts:
        card_sym_st = "Hearts"
        sym_index = 2
    elif card_sym == spades:
        card_sym_st = "Spades"
        sym_index = 3

    card_worth = 0
    card_num = random.choice(card_sym)
    card_index = -1
    if card_num == 'A':
        card_index = 0
        card_worth = card_worth + 1
    elif card_num == 'K':
        card_index = 9
        card_worth = card_worth + 10
    elif card_num == 'Q':
        card_index = 10
        card_worth = card_worth + 10
    elif card_num == 'J':
        card_index = 11
        card_worth = card_worth + 10
    else:
        card_index = int(card_num) - 1
        card_worth = card_worth + int(card_num)
    print(f"Your card is {card_num} of {card_sym_st}.")
    try:
        del card_list[sym_index][card_index]
    except:
        pass
    return card_worth

def player():
    palyer_value = 0
    palyer_value = palyer_value + player_choose()
    palyer_value = palyer_value + player_choose()
    
    hit_pass = int(input("Hit me (Press 1) or Pass(Press 2) : "))    
    while(hit_pass == 1):
        palyer_value = palyer_value + player_choose()
        if palyer_value > 21:
            #print("Your cards worth exceeds 21. You lose!!!")
            break
        hit_pass = int(input("Hit me (Press 1) or Pass(Press 2) : "))

    return palyer_value

comp_card_sym = []
comp_card_num = []

def comp_choose():
    card_sym = random.choice(card_list)
    sym_index = -1
    card_sym_st = ""
    if card_sym == clubs:
        card_sym_st = "Clubs"
        sym_index = 0
    elif card_sym == diamonds:
        card_sym_st = "Diamonds"
        sym_index = 1
    elif card_sym == hearts:
        card_sym_st = "Hearts"
        sym_index = 2
    elif card_sym == spades:
        card_sym_st = "Spades"
        sym_index = 3

    card_worth = 0
    card_num = random.choice(card_sym)
    card_index = -1
    if card_num == 'A':
        card_index = 0
        card_worth = card_worth + 1
    elif card_num == 'K':
        card_index = 9
        card_worth = card_worth + 10
    elif card_num == 'Q':
        card_index = 10
        card_worth = card_worth + 10
    elif card_num == 'J':
        card_index = 11
        card_worth = card_worth + 10
    else:
        card_index = int(card_num) - 1
        card_worth = card_worth + int(card_num)
    comp_card_num.append(card_num)
    comp_card_sym.append(card_sym_st)
    try: 
        del card_list[sym_index][card_index]
    except IndexError:
        pass
    return card_worth


def computer():
    comp_value = 0
    comp_value = comp_value + comp_choose()
    comp_value = comp_value + comp_choose()
    while(comp_value < 17):
        comp_value = comp_value + comp_choose()
    return comp_value
    
def game(pl,cmp):
    if pl>cmp and pl<=21:
        print("Congratulations!! You Win.")
    elif pl<cmp and cmp<=21:
        print("You lose.Better luck next time.")
    elif pl<=21 and cmp>21:
        print("Congratulations!! You Win.")
    elif pl>21 and cmp>21:
        print("You both lose!!")
    else:
        print("It's a tie!!")

def print_card():
    for i in range(len(comp_card_sym)):
        print(f"The computer has {comp_card_num[i]} of {comp_card_sym[i]}.")


intro()
rc = input("Enter your choice : ")
if rc.lower()=='r':
    rules()
    pl = player()
    cmp = computer()
    print_card()
    game(pl,cmp)
elif rc.lower()=='c':
    pl = player()
    cmp = computer()
    print_card()
    game(pl,cmp)
    
else:
    print("Enter a valid input.")

