#GLOBAL VARIABLES
import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}


#Classes

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                card_object=Card(suit,rank)
                self.all_cards.append(card_object)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal(self): 
        return self.all_cards.pop()   

deckclass=Deck()

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    def add_cards(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
    
    def adjust_for_ace(self):
        if self.value>21:
            self.value-=10
            self.aces-=1
            
class Chips:
    def __init__(self):
        self.total=100
        self.bet=0
        
    def win_total(self):
        self.total+=self.bet
    
    def los_total(self):
        self.total-=self.bet




#Functions!

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('Please Enter Bet: '))
        except ValueError:
            print('Incorrect Bet entered! Try again!')
        else:
            if chips.bet > chips.total:
                print('Bet incorrect and more than chips.! ',chips.total )
            else:
                break

def hit(deck,hand):
    hand.add_cards(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing
    
    while playing:
        HitOrStand=input('Please enter if you want to Hit or Stand: ')
        
        if HitOrStand=='Hit':
            hit(deck,hand)
        
        elif HitOrStand=='Stand':
            print('Please stand. Dealer is playing!')
            playing=False
        
        else:
            print('Incorect Input enter again!')
            continue
        break
        
def show_some(player,dealer):
    print('Dealers cards!')
    print('Dealers card HIDDEN')
    print('Dealers second card ',dealer.cards[1])
    print('Players cards ',*player.cards,sep='\n')
    
def show_all(player,dealer):
    print('Dealers cards ',*dealer.cards,sep='\n')
    print('Dealers hand value ',dealer.value)
    print('Players card ',*player.cards,sep='\n')
    print('Players hand value ',player.value)
    

def players_bust(chips):
    print('Player busted!')
    chips.los_total()

def players_win(chips):
    print('Players win')
    chips.win_total()

def dealers_bust(chips):
    print('Dealer busted!')
    chips.los_total()

def dealers_win(chips):
    print('Dealer win')
    chips.win_total()

def push():
    print('Tie Match!!')
    
playing=True

while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
       
    deck=Deck()
    deck.shuffle()
       
    player_hand=Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
       
    dealer_hand=Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
       
    player_chips=Chips()
    take_bet(player_chips)
       
    show_some(player_hand,dealer_hand)
       
    playing=True
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
           
        if player_hand.value>21:
            players_bust(player_chips)
            break
           
    if player_hand.value<=21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        show_all(player_hand,dealer_hand)
            
        if dealer_hand.value > 21:
            dealers_bust(player_chips)
                
        elif dealer_hand.value > player_hand.value:
            dealers_win(player_chips)
            
        elif dealer_hand.value < player_hand.value:
            players_win(player_chips)
            
        else:
            push()
                
     # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break    