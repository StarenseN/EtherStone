import random

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
        self.owner = owner
    
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

        for x in self.decklist:
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Owner: " + str(x['owner']))
            print("ID: " + str(x['id']))
            #print "Name: " + str(x['name'])         
            print("Attack: " + str(x['attack']))
            print("Body: " + str(x['body']))
            print("Bonus: " + str(x['bonus']) +"%")
            print("Rarity: " + str(x['rarity']))
            print("\n")

   
class Fight:
    
    def __init__(self, player, ordinateur): #player and ordinateur must be string"
        
        #generate 2 decks, one for Player, one for ordinateur | TODO: CHANGE
        self.owner1 = player
        self.owner2 = ordinateur
        
        #Arbitrary set cards to 1 | TODO: SUBJECT TO CHANGE
        self.deck1 = Deck(self.owner1, 1)
        self.deck2 = Deck(self.owner2, 1)

    def fightCard(self):
        
        #Show the fighters: | SUBJECT TO CHANGE IF DECK TOO LARGE
        print(self.deck1.displaydeck(), self.deck2.displaydeck())
        
        #Fight Logic now:
        att1 = self.deck1.decklist[0]['attack']
        att2 = self.deck2.decklist[0]['attack']
        body1 = self.deck1.decklist[0]['body']
        body2 = self.deck2.decklist[0]['body']
        
        while body1 > 0 and body2 > 0:
            print("NEW ROUND")
            #fight till one card is dead
            #way to find which hit first (it's 50/50 chance + bonus)
            if random.random()+self.deck1.decklist[0]['bonus']/100 > random.random()+self.deck2.decklist[0]['bonus']/100:
                print("Player hit first")
                body2 -= att1
                print("Computers card body is now: "+str(body2))
            else:
                print("Ordinateur hit first")
                body1 -= att2
                print("Players card body is now: "+str(body1))
        
        #One card is now dead, tell the winner
        if body1 <= 0:
                print("Player lose")
        elif body2 <= 0:
                print("Player win")
                
    
#TEST AREA    

#Fight("Player", "Ordinateur")

fight1 = Fight("Player", "Ordinateur")

fight1.fightCard()

