"""
def test(a,*t):
   for n,h in zip(t,a):
      print n,h

a = [5,4,3,2,1]
test(a,2,2)

"""
class Time(object):
   def __init__(self,hour=0,minute=0,second=0):
      self.hour   = hour
      self.minute = minute
      self.second = second

   def __str__(self):
       return '%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second)

   def __cmp__(self,other):
      #t1 = self.time_to_int()  #start
      #t2 = other.time_to_int() #end
      #return cmp(t2,t1)
      
      """"""
      if other.time_to_int() - self.time_to_int() > 0:
         return 1
      else:
         return -1
      """"""
   def time_to_int(self):
      seconds = self.hour * 3600 + self.minute * 60 + self.second
      return seconds

start = Time(1,4,3)
print (start.__str__())
end   = Time(1,3,4)
print (end)

print (start.__cmp__(end))
print ('+++next process+++')

"""
"""
import random
class Card(object):
   #""""""Represents a standard playing card. """"""

   def __init__(self, suit=0, rank=2):
       self.suit = suit
       self.rank = rank

   suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
   rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']
   
   def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                           Card.suit_names[self.suit])
   def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
       
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
       

class Deck(object):
   def __init__(self):
       self.cards = []
       for suit in range(4):
          for rank in range(1, 14):
             card = Card(suit, rank)
             #print 'card = ',card
             self.cards.append(card)
       
             
   def __str__(self):
       res = []
      
       for card in self.cards:
          
          res.append(str(card))
       
       return '\n'.join(res)

   def pop_card(self):
       return self.cards.pop()

   def add_card(self, card):
       self.cards.append(card)

   def shuffle(self):
       random.shuffle(self.cards)
       
   def sort(self):
      #res = []
      for i in range(len(self.cards)):
         for j in range(len(self.cards)-1-i):
            if self.cards[j].__cmp__(self.cards[j+1]) == 1:
               temp = self.cards[j]
               self.cards[j] = self.cards[j + 1]
               self.cards[j + 1] = temp
               
      return self.cards

   def move_cards(self, hand, num):
       for i in range(num):
         hand.add_card(self.pop_card())

   def deal_hands(self,hand_num,num):
      
      hand_list = []
      for i in range(hand_num):
         
         for j in range(num):
            
            hand.add_card(self.pop_card())
            hand_list.append(str(self.pop_card()))
      
      return hand_list
      
class Hand(Deck):
   def __init__(self, label=''):
       self.cards = []
       self.label = label

 
deck = Deck()
hand = Hand('new hand')

deck.shuffle()

#deck.pop_card()
#deck.move_cards(hand,6)

hand_lists = deck.deal_hands(2,5)
print ('Tanaka =', hand_lists[:5])
print ('Suzuki =', hand_lists[5:])



