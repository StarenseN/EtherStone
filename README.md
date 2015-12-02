# EtherStone
Game used to experiment Python coding || It has no intent to be a best practice example !

### How to use:

You can copy/paste Etherstone.py in www.codeskulptor.org and hit run.
Cards generated per deck is set to 2 (you can change it in class Fight, init)

### Game Logic:

When run is hit (on codeskulptor):
  - **cards** and **decks**: 2 decks, 2 cards each (4 in total) are created. NB: number of cards per deck can be changed. They are assigned to owner: "Player" and "Computer".
  - **rarity**: cards are randomly generated, rarity rank depends of the values sum the card has.
  - **shuffle**: Both decks are shuffled.
  - **fight**: card by card, they are drawn from the top of the deck.
  - **hit first**: Each card has 50% chance to hit first. 
  - **bonus**: Here comes the bonus, the bonus are added to the 50% chance to hit first. 
  - **attack**: Once a card is luckily chosen to hit first, it lowers the body of the ennemy card by the value of the attack.
  - **rounds**: Round repeats untill a card is dead (body <= 0)
  - **end**: Game end when each cards have played once.
  - **score**: Score is calculated, Winner displayed

### Futher developement:

multi files game with purse.py which will implement a wallet logic (to buy cards)

### Dev is on hold 
