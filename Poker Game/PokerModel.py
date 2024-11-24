import operator
import random


class Card:
    def __init__(self, rank, suit):
        self.rank = 0
        self.suit = ''
        self.image_path = ('img/' + str(rank) + str(suit) + '.png')
        self.selected = False

        if rank == 'A':
            self.rank = 14
        elif rank == 'K':
            self.rank = 13
        elif rank == 'Q':
            self.rank = 12
        elif rank == 'J':
            self.rank = 11
        elif rank == 'T':
            self.rank = 10
        else:
            self.rank = int(rank)

        self.suit = suit

    def __str__(self):
        out = ""

        if self.rank == 14:
            out += "Ace"
        elif self.rank == 13:
            out += "King"
        elif self.rank == 12:
            out += "Queen"
        elif self.rank == 11:
            out += "Jack"
        else:
            out += str(self.rank)

        out += ' of '

        if self.suit == 'H':
            out += 'Hearts'
        elif self.suit == 'S':
            out += 'Spades'
        elif self.suit == 'C':
            out += 'Clubs'
        else:
            out += 'Diamonds'

        return out


class Hand:
    def __init__(self, hand):
        self.hand = hand

    def __str__(self):
        out = ""
        for card in self.hand:
            out += str(card) + ", "
        return out

    def __getitem__(self, index):
        return self.hand[index]

    def __len__(self):
        return len(self.hand)


class Deck:
    def __init__(self):
        self.deck = []

        for suit in ['H', 'S', 'C', 'D']:
            for rank in range(2, 15):
                self.deck.append(Card(rank, suit))

    def __str__(self):
        out = ""
        for card in self.deck:
            out += str(card) + "\n"
        return out

    def __getitem__(self, index):
        return self.deck[index]

    def deal(self, amount):
        cards = []

        if amount > len(self.deck):
            print("There are not enough cards! I can only deal " + str(len(self.deck)) + " cards.")
            amount = len(self.deck)

        for i in range(amount):
            card = random.choice(self.deck)
            self.deck.remove(card)
            cards.append(card)
        return cards


class Poker:
    def __init__(self, scores=None):
        self.deck = Deck()
        self.scores = scores if scores else [0, 0, 0, 0]

        self.playerHand = Hand(self.deck.deal(5))
        self.comp1Hand = Hand(self.deck.deal(5))
        self.comp2Hand = Hand(self.deck.deal(5))
        self.comp3Hand = Hand(self.deck.deal(5))

    def computerReplace(self):
        self.AI_replace(self.comp1Hand)
        self.AI_replace(self.comp2Hand)
        self.AI_replace(self.comp3Hand)

    def AI_replace(self, hand):
        best_score = float('-inf')
        best_action = None
        deck_copy = Deck()
        deck_copy.deck = [card for card in self.deck.deck]

        for i in range(len(hand.hand)):
            simulated_hand = Hand(list(hand.hand))
            simulated_deck = Deck()
            simulated_deck.deck = deck_copy.deck[:]

            if len(simulated_deck.deck) > 0:
                simulated_hand.hand[i] = simulated_deck.deal(1)[0]
                score = self.expectiminimax(simulated_hand, 2, False, simulated_deck)
                if score > best_score:
                    best_score = score
                    best_action = simulated_hand

        if best_action:
            hand.hand = best_action.hand

    def expectiminimax(self, hand, depth, is_maximizing_player, deck):
        if depth == 0 or len(deck.deck) == 0:
            return self.get_score(hand)

        if is_maximizing_player:
            max_eval = float('-inf')
            for i in range(len(hand.hand)):
                simulated_hand = Hand(list(hand.hand))
                simulated_deck = Deck()
                simulated_deck.deck = deck.deck[:]

                if len(simulated_deck.deck) > 0:
                    simulated_hand.hand[i] = simulated_deck.deal(1)[0]
                    eval = self.expectiminimax(simulated_hand, depth - 1, False, simulated_deck)
                    max_eval = max(max_eval, eval)
            return max_eval

        else:
            min_eval = float('inf')
            for i in range(len(hand.hand)):
                simulated_hand = Hand(list(hand.hand))
                simulated_deck = Deck()
                simulated_deck.deck = deck.deck[:]

                if len(simulated_deck.deck) > 0:
                    simulated_hand.hand[i] = simulated_deck.deal(1)[0]
                    eval = self.expectiminimax(simulated_hand, depth - 1, True, simulated_deck)
                    min_eval = min(min_eval, eval)
            return min_eval

    def replace(self, hand):
        count = 0
        for card in hand:
            if card.selected:
                hand.hand.remove(card)
                count += 1
        hand.hand.extend(self.deck.deal(count))

    def play_round(self):
        score1 = self.get_score(self.playerHand)
        score2 = self.get_score(self.comp1Hand)
        score3 = self.get_score(self.comp2Hand)
        score4 = self.get_score(self.comp3Hand)

        winner = max(score1, max(score2, max(score3, score4)))

        if winner == score1:
            self.scores[0] += 1
        elif winner == score2:
            self.scores[1] += 1
        elif winner == score3:
            self.scores[2] += 1
        elif winner == score4:
            self.scores[3] += 1

        return [score1, score2, score3, score4]

    def convert(self, hand):
        return len(hand)

    def get_score(self, hand):
        cardCount = {rank: 0 for rank in range(2, 15)}
        for card in hand.hand:
            cardCount[card.rank] += 1

        uniqueCount = len([count for count in cardCount.values() if count > 0])
        straight = self.is_straight(hand)
        flush = self.is_flush(hand)
        points = 0

        if straight and flush:
            points = 9
        elif flush:
            points = 6
        elif straight:
            points = 5
        elif uniqueCount == 2:
            if max(cardCount.values()) == 4:
                points = 8
            elif max(cardCount.values()) == 3:
                points = 7
        elif uniqueCount == 3:
            if max(cardCount.values()) == 3:
                points = 4
            elif max(cardCount.values()) == 2:
                points = 3
        elif uniqueCount == 4:
            points = 2
        else:
            points = 1

        sorted_cardCount = sorted(cardCount.items(), key=operator.itemgetter(1, 0), reverse=True)
        for keyval in sorted_cardCount:
            if keyval[1] != 0:
                points = int(str(points) + (keyval[1] * str(keyval[0]).zfill(2)))

        return points

    def convert_score(self, score):
        if str(score)[0] == '1':
            return "High Card"
        elif str(score)[0] == '2':
            return "One Pair"
        elif str(score)[0] == '3':
            return "Two Pair"
        elif str(score)[0] == '4':
            return "Three of a Kind"
        elif str(score)[0] == '5':
            return "Straight"
        elif str(score)[0] == '6':
            return "Flush"
        elif str(score)[0] == '7':
            return "Full House"
        elif str(score)[0] == '8':
            return "Four of a Kind"
        elif str(score)[0] == '9':
            return "Straight Flush"

    def is_straight(self, hand):
        values = sorted(card.rank for card in hand.hand)
        for i in range(len(values) - 1):
            if values[i] + 1 != values[i + 1]:
                return False
        return True

    def is_flush(self, hand):
        suit = hand.hand[0].suit
        return all(card.suit == suit for card in hand.hand)

