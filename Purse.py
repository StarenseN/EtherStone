class Wallet:
    def __init__(self, owner):
        self.obj = {}
        self.obj['owner'] = owner
        self.obj['gold'] = 100 #somme initiale (=2 boosters)
        self.obj['dust'] = 0 
        self.obj['coffer'] = [] #feature | TODO

        #add the obj in the existings wallet

    def display(self):
        print("Gold: %d / Dust: %d" % (self.obj.get('gold'), self.obj.get('dust')))
        print("Coffer contains: %d item(s)" % len(self.obj.get('coffer')))
    
    def creditGold(self, amount):
        self.obj['gold'] = self.obj.get('gold') + amount
        
    def creditDust(self, amount):
        self.obj['dust'] = self.obj.get('dust') + amount
        
    def debitGold(self, amount):
        self.obj['gold'] = self.obj.get('gold') - amount
        
    def debitDust(self, amount):
        self.obj['dust'] = self.obj.get('dust') - amount
#TESTAREA

wallet = Wallet("Player")

print(wallet.obj)

wallet.display()
wallet.creditGold(50)
wallet.creditDust(15)
wallet.display()
wallet.debitGold(50)
wallet.debitDust(15)
wallet.display()