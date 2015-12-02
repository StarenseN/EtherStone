# EtherStone
Game used to experiment Python coding || It has no intent to be a best practice example !

### How to use:

You can copy/paste Etherstone.py in www.codeskulptor.org and hit run.
Cards generated per deck is set to 2 (you can change it in class Fight, init)

### Game Logic:

When run is hit (on codeskulptor):
  - PLAYERS: "Player" and "Computer" are in play
  - CARDS and DECKS CREATION: 2 decks, 2 cards each (4 in total) are created. This number of cards per deck can be changed.
  - SHUFFLE: Both decks are shuffled.
  - FIGHT card by card initiated, they are drawn from the top of the deck.
  - HIT FIRST: Each card has 50% chance to hit first. 
  - BONUS: Here comes the bonus, the bonus are added to the 50% chance to hit first. 
  - ATTACK: Once a card is chosen to hit first, it lowers the body of the ennemy card by the value of the attack.
  - ROUNDS: Round repeats untill a card is dead (body <= 0)
  - END: Game end when each cards have played once.
  - SCORE: Score is calculated, Winner displayed

### Futher developement:

multi files game with purse.py which will implement a wallet logic (to buy cards)

### Dev is on hold 
