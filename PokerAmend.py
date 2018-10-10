"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import random


class Card(object):
    """Represents a standard playing card.
    
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        """Compares this card to other, first by suit, then rank.

        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(object):
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    card = Card(0,1)
    deck.add_card(card)
    #print ('pass1 = ',deck)
    #print deck.pop_card(2)
    """
    deck.shuffle()
    
    
    hand = Hand()
    print find_defining_class(hand, 'shuffle')

    deck.move_cards(hand, 5)
    hand.sort()
    print hand
    """
#-------------------------------------------------------------------    

class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
        
    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        cnt = 0
        for val in self.ranks.values():
            if val == 2:
                cnt += 1
        if cnt == 1: 
            return True
        else:
            return False
        

    def has_twopair(self):
        self.rank_hist()
        cnt = 0
        for val in self.ranks.values():
            if val == 2:
                cnt += 1
        if cnt == 2: 
            return True
        else:
            return False
        
    def has_threecards(self):
        self.rank_hist()
        cnt = 0
        for val in self.ranks.values():
            if val == 3:
                cnt += 1
        if cnt == 1: 
            return True
        else:
            return False

    def classify(self):
        card_list = []
        spc_straight =[1,10,11,12,13]
        
        for card in self.cards:
            card_list.append(card.rank)

        card_list.sort()
        cnt = 0
        for i in range(1,3):
            if card_list[0] == card_list[i]:
                cnt += 1
                if cnt == 2:
                    if card_list[3] == card_list[4]:
                        #count('hse')
                        return 'full house'
            else:
                cnt = 0
                break
      
        if card_list[0] == card_list[1]:
            for i in range(3,5):
                if card_list[2] == card_list[i]:
                    cnt += 1
                    if cnt == 2:
                        #count('hse')
                        return 'full house'
                else:
                    cnt = 0
                    break
            
        for i in range(1,5):
            if card_list[0] == card_list[i]:
                cnt += 1
                if cnt == 3:
                    #count('fou')
                    return 'four of a kind'
            else:
                cnt = 0
                break
            
        for i in range(2,5):
            if card_list[1] == card_list[i]:
                cnt += 1
                if cnt == 3:
                    #count('fou')
                    return 'four of a kind'
            
        if card_list[4] < 5:
            return self.others()
        
        if card_list[0] == 1:
            if card_list[0:5] == spc_straight :
                if self.has_flush() == True:
                    #count('stf')
                    return 'straight flush'
                else:
                    #count('st')
                    return 'straight'
        
        if card_list[len(card_list)-2] != card_list[len(card_list)-1]-1:
            return self.others()
        if card_list[len(card_list)-3] != card_list[len(card_list)-1]-2:
            return self.others()
        if card_list[len(card_list)-4] != card_list[len(card_list)-1]-3:
            return self.others()
        if card_list[len(card_list)-5] != card_list[len(card_list)-1]-4:
            return self.others()
        else:
            if self.has_flush() == True:
                #count('stf')
                return 'straight flush'
            else:
                #count('st')
                return 'straight'

    def others(self):

        if self.has_flush() == True:
            #count('fl')
            return 'flush'

        if self.has_threecards() == True:
            #count('th')
            return 'three of a kind'

        if self.has_twopair() == True:
            #count('t')
            return 'two pair'

        if self.has_pair() == True:
            #count('p')
            return 'pair'

global p_cnt ,t_cnt ,th_cnt ,st_cnt ,fl_cnt ,hse_cnt ,fou_cnt ,stf_cnt ,\
none_cnt

(p_cnt ,t_cnt ,th_cnt ,st_cnt ,fl_cnt ,\
 hse_cnt ,fou_cnt ,stf_cnt ,none_cnt) = (0,0,0,0,0,0,0,0,0)

def count(check):
    global p_cnt ,t_cnt ,th_cnt ,st_cnt ,fl_cnt ,hse_cnt ,fou_cnt ,stf_cnt ,\
           none_cnt
           
    if check == 'pair':
        p_cnt += 1
    if check == 'two pair':
        t_cnt += 1
    if check == 'three of a kind':
        th_cnt += 1
    if check == 'straight':
        st_cnt += 1
    if check == 'flush':
        fl_cnt += 1
    if check == 'full house':
        hse_cnt += 1
    if check == 'four of a kind':
        fou_cnt += 1
    if check == 'straight flush':
        stf_cnt += 1
    if check == None:
        none_cnt += 1
    
        

if __name__ == '__main__':
    # make a deck
    for i in range(3000):
        deck = Deck()
        deck.shuffle()

    # deal the cards and classify the hands
    
        for j in range(10):
            hand = PokerHand()
            deck.move_cards(hand, 5)
            """
            card_1 = Card(0,9)
            card_2 = Card(0,10)
            card_3 = Card(0,11)
            card_4 = Card(0,12)
            card_5 = Card(0,13)
            
            
            hand.add_card(card_1)
            hand.add_card(card_2)
            hand.add_card(card_3)
            hand.add_card(card_4)
            hand.add_card(card_5)
            print 'before sort'
            print hand
            print ''
            """
            hand.sort()
            #print hand
            #print 'flush = ',hand.has_flush()
            #print ''
            
            #print 'classify =',hand.classify()
            chk = hand.classify()
            count(chk)
            #print ''
    
        
    print ('p_cnt = ',p_cnt)
    print ('t_cnt = ',t_cnt)
    print ('th_cnt = ',th_cnt)
    print ('st_cnt = ',st_cnt)
    print ('fl_cnt = ',fl_cnt)
    print ('hse_cnt = ',hse_cnt)
    print ('fou_cnt = ',fou_cnt)
    print ('stf_cnt = ',stf_cnt)
    print ('none_cnt = ',none_cnt)
    print ('')
            