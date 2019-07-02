# encoding=utf-8
import random

SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
SUITS_CODE = {'hearts': u'♡', 'diamonds': u'♢', 'clubs': u'♣', 'spades': u'♠'}


class Card(object):
    def __init__(self, number, suit):
        if number < 1 or number > 13:
            raise ValueError('Invalid Card number!!')
        if suit not in SUITS:
            raise ValueError('Invalid Suit for card!!')

        self.number = number
        self.suit = suit
        self.uuid = suit + str(number)

        self.card_str = self.str_rep()

    def has_same_number(self, card):
        return self.number == card.number

    def has_same_suit(self, card):
        return self.suit == card.suit

    def str_rep(self):
        card = self.number

        if self.number == 11:
            card = 'Jack'
        elif self.number == 12:
            card = 'Queen'
        elif self.number == 13:
            card = 'King'
        return '{} of {}'.format(card, self.suit)

    def __str__(self):
        return self.card_str

    def __unicode__(self):
        card = self.number

        if self.number == 1:
            card = 'A'
        if self.number == 11:
            card = 'J'
        elif self.number == 12:
            card = 'Q'
        elif self.number == 13:
            card = 'K'
        return str(card) + SUITS_CODE[self.suit]


def print_cards(cards):
    print '[',
    for card in cards:
        print unicode(card),
    print ']',


def get_shuffled_cards():
    card_bucket = []
    for number in xrange(1, 14):
        for suit in SUITS:
            card_bucket.append(Card(number, suit))
    return random.sample(card_bucket, len(card_bucket))


if __name__ == '__main__':
    print get_shuffled_cards()
    #print_cards(get_shuffled_cards()[:13])

