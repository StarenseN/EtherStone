#import Purse.py (used in multi-files game)
#import Purse

import random
from random import shuffle

maxAttack = 10
maxBody = 10
maxBonusFactor = 14 #Bonus cannot exceed 31 (otherwise card has 100% first hit)) 
                    #TODO find a better to modelize bonus

class Card:
    
    id_card = 0
        
    def __init__(self, owner):

        self.obj = {}
        self.obj['owner'] = owner
        self.obj['id'] = self.id_card
        #self.obj['name'] = self.nameGen()
        self.obj['attack'] = random.randint(1, maxAttack)
        self.obj['body'] = random.randint(1, maxBody)
        self.obj['bonus'] = ((random.randint(0, maxBonusFactor)**2)/10.0)
        self.obj['rarity'] = self.setRarity()
        Card.id_card += 1
    
    ##def nameGen(self):
        #used in __init__
        #test
        #todo: convert num by letters
        #return ''.join(str(random.randint(0,9)) for x in range(8))
    
    def setRarity(self):
        #rarity is dependent of the MAX possibles.
        total = maxAttack + maxBody + maxBonusFactor**2/10
        if self.obj['attack']+self.obj['body']+self.obj['bonus'] >= 0.8*total:
            return "!!**LENGENDARY**!!"
        elif 0.6*total <= self.obj['attack']+self.obj['body']+self.obj['bonus'] < 0.8*total:
            return "!*Rare*!"
        else:
            return "Common"
         
class Deck:
    
    def __init__(self, owner, n): #tell the owner, create a deck with n cards
        
        #TODO: Different Owner Logic (2 list ? or Classed by Owner?)
        
        self.decklist = self.create(owner, n) #decklist is a LIST "deck" wich each element is an OBJECT
    
    def create(self, owner, n): #create random cards

        self.owner = owner
        deck = []
        i  = 0 
        while i < n:
            x = Card(self.owner)  #***call class Card***
            deck = [x.obj] + deck
            i += 1
        return deck
    
    def displaydeck(self):
        
        print("Number of cards: "+ str(len(self.decklist)))
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        for x in self.decklist:
            print("Owner: " + str(x['owner']))
            print("ID: " + str(x['id']))
            #print "Name: " + str(x['name'])         
            print("Attack: " + str(x['attack']))
            print("Body: " + str(x['body']))
            print("Bonus: +" + str(x['bonus']) +"%")
            print("Rarity: " + str(x['rarity']))
            print("\n")

    def shuffleDeck(self):
        
        shuffle(self.decklist)
        return self.decklist
   
class Fight:
    
    def __init__(self, player, ordinateur): #player and ordinateur must be string"
        
        #generate 2 decks, one for Player, one for ordinateur | TODO: CHANGE
        self.owner1 = player
        self.owner2 = ordinateur
        
        #Arbitrary set cards to 2 | TODO: SUBJECT TO CHANGE
        self.deck1 = Deck(self.owner1, 2)
        self.deck2 = Deck(self.owner2, 2)

        #Shuffle the decks

        self.deck1.decklist = self.deck1.shuffleDeck()
        self.deck2.decklist = self.deck2.shuffleDeck()

    def fightCard(self):
        
        #Show the fighters: | SUBJECT TO CHANGE IF DECK TOO LARGE
        print(self.deck1.displaydeck())
        print(self.deck2.displaydeck())
        
        #Fight Logic now:

        #score
        score1 = 0 #Player
        score2 = 0 #Computer

        #Master Loop trough each card
        i=0
        while i < len(self.deck1.decklist):
            print("\n***CARD " + str(i+1) + " Fight***\n") 
            att1 = self.deck1.decklist[i]['attack']
            att2 = self.deck2.decklist[i]['attack']
            body1 = self.deck1.decklist[i]['body']
            body2 = self.deck2.decklist[i]['body']
            
            #fight till one card is dead          
            while body1 > 0 and body2 > 0:
                print("*new round*")
                #way to find which hit first (it's 50/50 chance + bonus)
                if random.random()+self.deck1.decklist[0]['bonus']/100 > random.random()+self.deck2.decklist[0]['bonus']/100:
                    print(self.owner1 +" hits first doing "+ str(att1) + " damages")
                    body2 -= att1
                    print(self.owner2 + "'s card body is now: "+str(body2) + "\n")
                else:
                    print(self.owner2 + " hits first doing "+ str(att2) + " damages")
                    body1 -= att2
                    print(self.owner1 + "'s card body is now: "+str(body1) + "\n")
        
            #One card is now dead, tell the winner
            if body1 <= 0:
                    print("battle lost")
                    score2 += 1
            elif body2 <= 0:
                    print("battle won")
                    score1 += 1
            i += 1
        if score1 > score2:
            print("---------" + self.owner1.upper() + " WINS--------- (" +str(score1) + "/" + str(score2) +")")
        elif score1 < score2:
            print("---------" + self.owner2.upper() + " WINS--------- ("+str(score2) + "/"+ str(score1) + ")")
        else:
            print("---------TIE GAME--------- ("+str(score2) + "/"+ str(score1) + ")")
    
class Hero:
    pass


#RUN

fight = Fight("Player", "Computer")
fight.fightCard()
