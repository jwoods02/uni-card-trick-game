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


def print_three_card_piles(card_pile):
    """Prints 3 card piles for player to choose from"""
    print_card_pile(1, card_pile[0])
    print_card_pile(2, card_pile[1])
    print_card_pile(3, card_pile[2])


def ask_player_for_chosen_card_pile():
    """ Asks player for chosen card pile, validates it and returns it as an int"""
    chosen_card_pile = int(input("Which number pile is your card in?"))
    # ADD VALIDATION HERE
    return chosen_card_pile


def pick_up_card_piles(chosen_card_pile, card_piles):
    """Picks up cards based on which pile chosen card is in"""
    if chosen_card_pile == 1:
        card_piles[0], card_piles[1] = card_piles[1], card_piles[0]

    elif chosen_card_pile == 3:
        card_piles[2], card_piles[1] = card_piles[1], card_piles[2]

    concentrated_card_pile = card_piles[0] + card_piles[1] + card_piles[2]


    return concentrated_card_pile


# Start of the main game code.

deck = make_deck()

# TURN 1

deck_fragment = deal_cards_into_3_columns(deck[0:20])

print_three_card_piles(deck_fragment)

pile_of_chosen_card = ask_player_for_chosen_card_pile()

deck_fragment = pick_up_card_piles(pile_of_chosen_card, deck_fragment)

# TURN 2

deck_fragment = deal_cards_into_3_columns(deck_fragment)

print_three_card_piles(deck_fragment)

pile_of_chosen_card = ask_player_for_chosen_card_pile()

deck_fragment = pick_up_card_piles(pile_of_chosen_card, deck_fragment)

# TURN 3

deck_fragment = deal_cards_into_3_columns(deck_fragment)

print_three_card_piles(deck_fragment)

pile_of_chosen_card = ask_player_for_chosen_card_pile()

print_three_card_piles(deck_fragment)

deck_fragment = pick_up_card_piles(pile_of_chosen_card, deck_fragment)

# Tell user their card

print(deck_fragment[10])
