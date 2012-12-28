auto-cluedo
===========

I am too lazy to play Cluedo. This should be a useful thinking machine/notepad for when I'm forced to play.

Rules
-----

The most basic things we need to know for this, ignoring all of the other faffing about.

* There will be a number of categories of things we need to guess. Usually these will be place, person and item.
* We must know the full set of possible entries for each of these categories.
* One unknown entry from each category is removed from the pile at the beginning of the game and placed into a secret `murder envelope'.
* Cards will be shuffled and dealt to players one by one until there a no more left. Therefore we should know the number of cards each player has.
* A guess will involve publicly asking players in turn for one entry of each category until either someone produces one of the cards privately, or there are no players left other than the asker to ask.
* An accusation will involve publicly stating one entry of each category. All players will discovery whether these are the correct or incorrect items in the murder envelope.
* To allow for the DVD version, cards may move possession through the game so we should keep track of the point in the game that anything happens.
* To allow for people screwing up, the engine shouldn't assume a particular ordering of turns and should allow if possible for people making incorrect statements.

Design
------

### Facts

* All players start with no cards.
* Each time a card is taken we record an incrementation of the total card number for that player
* Each time a card is removed we record a decrementation of the total card number for that player
* For each guess we need to keep track of WHO guessed, WHAT they guessed and each person that answered, along with whether they showed a card or not.
* For an accusation we keep track of WHAT was guessed and by WHO, along with whether they were CORRECT - this is less important if they were in fact correct.
* If a card is shown to the player, then we record WHO showed it and WHAT it is.
* We show ourselves all each of our cards as we pick them up.

Each of these facts should be recorded with the logical time at which they occurred within the game.

### Deductions

A deduction is made from one or more other deductions and facts. These can be based on rules similar to the following.

* Only one player can hold a particular entry at any time.
* If a player has shown a card to you then we know they hold that card.
* If players hold all but one entry in a category, then the last entry must be in the murder envelope.
* If a deduction about card ownership is true at time B and the player has not picked up or dropped any cards between time A and B then it must have been true at A.
* If a player does not show cards for a guess then they do not have any of those cards.

Each deduction should record the facts and deductions used to make it. This way an invalidated fact can be traced to destroy its damage.

### Processing

* Should be able to tell engine about facts.
* Deductions should be trusted to tell you who has which card at which time.
* We can treat the murder envelop as just another player.
* Deductions should be made by applying all rules over and over until no new deductions are made.
* Should be able to ask engine if a player had a card at a certain time, or if they didn't. Returns YES, NO, UNKNOWN.
* Should keep track of all new deductions/facts. We can then do a light deductive phase that checks with rules whether the information is relevant rather than running on everything.

### Improvements

Work out who has seen what, so that we can show them the same or see what they know in order to guess first if need be.
