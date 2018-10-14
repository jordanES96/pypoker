import random


class Card:  # Create a card object that stores suit and rank for each object
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        elif self.rank == 10:
            rank = 'T'
        else:
            rank = self.rank
        return str(rank) + self.suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __sub__(self, other):
        return self.rank - other.rank

    def __add__(self, other):
        return self.rank + other.rank

    def show(self):
        print str(self.rank + self.suit)


class Deck:  # Create a deck object that stores our card objects
    def __init__(self):
        self.cards = []
        self.d = {}
        self.build()
        self.burnpile = []

    def build(self):  # Builds a deck of card objects
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        suits = ['h', 'c', 'd', 's']
        for s in range(4):
            for r in range(13):
                self.cards.append(Card(ranks[r], suits[s]))
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    def test(self):
        for i in self.cards:
            print i

    def shuffle(self):  # Shuffles our deck list
        random.shuffle(self.cards)

    def draw(self):  # Draws a card from the top of the deck
        return self.cards.pop()

    def burn_card(self):  # Poker mechanic in which a card is discarded before flop turn and river
        self.burnpile.append(self.cards.pop())

    def construct_flop(self):
        self.burn_card()
        self.flop = [self.draw(), self.draw(), self.draw()]
        return self.flop

    def construct_turn(self):
        self.burn_card()
        self.turn = [self.draw()]
        return self.turn

    def construct_river(self):
        self.burn_card()
        self.river = [self.draw()]
        return self.river

    def construct_dict(self):
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.d = dict(zip(self.ranks, self.values))
        return self.d


class Player:  # Create a player object that with both of its attributes being a card object this represents their hand
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.players = []

    def create_player_list(self, deck):  # Prompts for amount of players, then fills the player list with constructed player objs
        #self.count = int(input("Enter amount of players 2-10"))
        self.count = 1
        for i in range(self.count):
            self.players.append(Player(deck.draw(), deck.draw()))
        return self.players

    def is_pair(self, players):
        pass


class Board:  # Community cards
    pass
    def __init__(self, burn1, card1, card2, card3, burn2, card4, burn3, card5):
        self.burn1 = burn1
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.burn2 = burn2
        self.card4 = card4
        self.burn3 = burn3
        self.card5 = card5

    def print_flop(self):
        print self.card1, self.card2, self.card3

    def print_turn(self):
        print self.card1, self.card2, self.card3, self.card4

    def print_river(self):
        print self.card1, self.card2, self.card3, self.card4, self.card5


class Poker: # Checks players hands as well as creating a deck, shuffling it, and creating players and giving them hands
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player('null', 'null')
        self.playerlist = self.player.create_player_list(self.deck)
        self.flop = self.deck.construct_flop()
        self.turn = self.deck.construct_turn()
        self.river = self.deck.construct_river()
        self.board = Board(self.deck.burnpile[0], self.flop[0], self.flop[1], self.flop[2],
                           self.deck.burnpile[1], self.turn[0], self.deck.burnpile[2], self.river[0])
        self.sortedlist = []
        self.sorted_suit = []

        for i in range(len(self.playerlist)):
            sortedhand = self.sort_player_hands_by_rank(self.playerlist[i], self.board)
            self.sortedlist.append(sortedhand)

        for i in range(len(self.playerlist)):
            rank = self.sort_player_hands_by_suit(self.playerlist[i], self.board)
            self.sorted_suit.append(rank)

        for player in self.playerlist:
            print
            print player.card1
            print player.card2

        for i in self.sortedlist:
            print
            for ii in i:
                print ii



        # for i in test[1]:
        #     print i
    def sort_player_hands_by_suit(self, player, board):
        unsortedlist = [
                        player.card1,
                        player.card2,
                        board.card1,
                        board.card2,
                        board.card3,
                        board.card4,
                        board.card5
                        ]
        unsortedlist.sort(key=lambda y: y.suit, reverse=False)
        return unsortedlist

    def sort_player_hands_by_rank(self, player, board,):
        unsortedlist = [
                        player.card1,
                        player.card2,
                        board.card1,
                        board.card2,
                        board.card3,
                        board.card4,
                        board.card5
                        ]
        unsortedlist.sort(key=lambda x: x.rank, reverse=False)

        return unsortedlist
    def evalHand(self, sortedlist, sortedsuit):
        return self.isQuads(sortedlist, sortedsuit)

    def isRoyalFlush(self, unsortedhand):
        pass

    def isStraightFlush(self, unsortedhand, ):
        pass

    def isQuads(self, sortedlist, sortedsuit):
        hand = []
        for i in range(len(sortedlist)):
            for ii in range(4):
                if ii == 3:
                    print 'player', i + 1 ,'doesnt have quads'
                    return self.isFlush(sortedlist, sortedsuit)
                elif sortedlist[i][ii] == sortedlist[i][ii+1] and sortedlist[i][ii] == sortedlist[i][ii+2]\
                    and sortedlist[i][ii] == sortedlist[i][ii+3]:
                    hand.append(sortedlist[i][ii])
                    hand.append(sortedlist[i][ii+1])
                    hand.append(sortedlist[i][ii+2])
                    hand.append(sortedlist[i][ii+3])
                    for k in reversed(sortedlist[i]):
                        if k == hand[0]:
                            pass
                        else:
                            hand.append(k)
                            if len(hand) == 5:
                                print 'player', i + 1, 'does have quads!'
                                score = 1
                                return score, hand

    def isFullHouse(self, sortedlist):
        pass

    def isFlush(self, sortedlist, sortedsuit):
        hand = []
        for i in range(len(sortedsuit)):
            for ii in range(3):
                print sortedsuit[i][ii].suit == sortedsuit[i][ii+1].suit
                if ii == 2:
                    print 'player', i + 1, 'doesnt have a flush'
                    return self.isStraight(sortedlist)
                elif sortedsuit[i][ii].suit == sortedsuit[i][ii+4].suit:
                    hand.append(sortedsuit[i][ii])
                    hand.append(sortedsuit[i][ii+1])
                    hand.append(sortedsuit[i][ii+2])
                    hand.append(sortedsuit[i][ii+3])
                    hand.append(sortedsuit[i][ii+4])
                    print 'player', i + 1, 'does have a flush'
                    return True, hand

    def isStraight(self, sortedlist):
        hand = []
        for i in range(len(sortedlist)):
            for ii in range(3):
                if ii == 2:
                    print 'player', i + 1, 'doesnt have a straight'
                    return self.isTrips(sortedlist)
                elif sortedlist[i][ii+4] - sortedlist[i][ii] == 4 and sortedlist[i][ii+3] - sortedlist[i][ii] == 3 \
                       and sortedlist[i][ii+2] - sortedlist[i][ii] == 2 and sortedlist[i][ii+1] - sortedlist[i][ii] == 1:
                    hand.append(sortedlist[i][ii])
                    hand.append(sortedlist[i][ii+1])
                    hand.append(sortedlist[i][ii+2])
                    hand.append(sortedlist[i][ii+3])
                    hand.append(sortedlist[i][ii+4])
                    print 'player', i + 1, 'does have a straight!'
                    return True, hand


    def isTrips(self, sortedlist):
        #handcopy = sortedhand
        #count = 0
        hand = []
        for i in range(len(sortedlist)):
            for ii in range(6):
                if ii == 5:
                    print 'player', i + 1 ,'doesnt have trips'
                    return self.isTwopair(sortedlist)
                elif sortedlist[i][ii] == sortedlist[i][ii+1] and sortedlist[i][ii] == sortedlist[i][ii+2]:
                    hand.append(sortedlist[i][ii])
                    hand.append(sortedlist[i][ii+1])
                    hand.append(sortedlist[i][ii+2])
                    for k in reversed(sortedlist[i]):
                        if k == hand[0]:
                            pass
                        else:
                            hand.append(k)
                            if len(hand) == 5:
                                print 'player', i + 1, 'does have trips!'
                                return True, hand

    def isTwopair(self, sortedlist):
        #handcopy = sortedhand
        #count = 0
        hand = []
        pair_count = 0
        for i in range(len(sortedlist)):
            for ii in range(7):
                if ii == 6:
                    print 'player', i + 1 ,'doesnt have two pair'
                    return self.isPair(sortedlist)
                elif sortedlist[i][ii] == sortedlist[i][ii+1]:
                    hand.append(sortedlist[i][ii])
                    hand.append(sortedlist[i][ii+1])
                    pair_count += 1

                    if pair_count == 2:
                        for k in reversed(sortedlist[i]):
                            if k == hand[0] or k == hand[2]:
                                pass
                            else:
                                hand.append(k)
                                if len(hand) == 5:
                                    print 'player', i + 1, 'does have two pair!'
                                    return True, hand

    def isPair(self, sortedlist):
        #handcopy = sortedhand
        #count = 0
        hand = []
        pair_count = 0
        for i in range(len(sortedlist)):
            for ii in range(7):
                if ii == 6:
                    print 'player', i + 1 ,'doesnt have a pair'
                    return self.isHighCard(sortedlist)
                elif sortedlist[i][ii] == sortedlist[i][ii+1]:
                    hand.append(sortedlist[i][ii])
                    hand.append(sortedlist[i][ii+1])
                    for k in reversed(sortedlist[i]):
                        if k == hand[0]:
                            pass
                        else:
                            hand.append(k)
                            if len(hand) == 5:
                                print 'player', i + 1, 'does have a pair!'
                                return True, hand
    def isHighCard(self, sortedlist):
        hand = []
        k = 0
        for i in reversed(sortedlist[k]):
            hand.append(i)
            if len(hand) == 5:
                print 'player 1 has high card:', hand[0]
                return True, hand

def main():
    poker = Poker()
    hand = poker.sortedlist
    suit_hand = poker.sorted_suit
    run_count = 0
    while run_count < 1000:
        poker = Poker()
        hand = poker.sortedlist
        test = poker.evalHand(hand, suit_hand)
        print "suits:"
        for i in poker.sorted_suit:
            for ii in i:
                print ii,
        run_count += 1
        print
        print
        for i in test[1]:
            print i,


    #poker.board.print_river()


main()


# FOR TESTING :

#
#
#     count = 0
#     hand = []
#     for card in sortedhand:
#         if sortedhand[0] == card or sortedhand[1] == card:
#             count += 1
#             hand.append(card)
#     if count == 3:
#         return True

# for card in handcopy:
#     j = 0
#     for card2 in handcopy:
#         if card2 == card:
#             if j != i:
#                 print 'hi1'
#                 count += 1
#                 hand.append(card2)
#                 if j == 6 or card == handcopy[i]:
#                     hand.append(card)
#         if count == 3:
#             for k in reversed(sortedhand):
#                 if k == hand[0]:
#                     pass
#                 else:
#                     hand.append(k)
#                     if len(hand) == 5:
#                         return True, hand
#         if count < 3 and j == 6:
#
#             return False, hand
#
#         j += 1
#
#     #del(handcopy[i])
#     i += 1
#
