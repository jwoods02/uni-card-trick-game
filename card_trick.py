"""Simulates the popular 'Twenty One' card trick"""

# pylint: disable=C0103, C0325

from random import shuffle


def make_deck():
    """Create and shuffle deck of cards.

    Creates a deck of cards with the notation [Value, Suit]
    E.g. 7S for seven of spades, then shufles and returns the deck.
    """
    new_deck = []

    # Creates full deck of cards with nested for loop.
    for suit in "Spades", "Diamonds", "Hearts", "Clubs":
        for value in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "Jack", "Queen", "King"]:
            new_deck.append(value + " of " + suit)

    shuffle(new_deck)

    return new_deck

def deal_cards_into_3_columns(card_pile):
    """Deals cards into 3 columns"""
    column_1, column_2, column_3 = [], [], []
    column_count = 1

    for card in card_pile:
        if column_count == 1:
            column_1.append(card)
            column_count += 1

        elif column_count == 2:
            column_2.append(card)
            column_count += 1

        else:
            column_3.append(card)
            column_count = 1


    return [column_1, column_2, column_3]


def print_card_pile(pile_number, card_pile):
    """Prints card pile"""

    print("Pile " + str(pile_number) + ": " + ", ".join(card_pile))


# Start of the main game code.

deck = make_deck()

#Get first 21 cards in the shuffled deck.
deck_fragment = deck[0:20]


card_columns = deal_cards_into_3_columns(deck_fragment)

print_card_pile(1, card_columns[0])

print_card_pile(2, card_columns[1])

print_card_pile(3, card_columns[2])
