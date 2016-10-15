"""Simulates the popular 'Twenty One' card trick.

1.	21 cards selected from the deck.
2.	Cards are dealt into 3 columns of 7.
3.	Participant selects a card.
4.	Participent points to the pile which contains their card.
5.	Cards are picked up with the selected pile sandwiched between the others.
6.	Steps 2-5 are repeated 2 times more.
7.	The chosen card is now the 11th card in the deck.
"""

# pylint: disable=C0103, C0325

from random import shuffle

def make_deck():
    """Create and shuffles a deck of cards.

    Returns
    ----------
    new_deck: A list containing a randomly shuffled deck of 52 cards.
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
    """Deals cards row by row into 3 columns of 7 cards.

    Parameters
    ----------
    card_pile: A list containing 21 cards.

    Returns
    ----------
    [column_1, column_2, column_3]: A 2d list containing the 3 columns of
                                    7 cards.
    """
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
    """Prints a formatted card pile.

    The card pile is formatted with the pile number, followed by each card
    seperated with ', '.

    Parameters
    ----------
    pile_number: An int literal containing the pile number to print.
    card_pile: A list containing the cards to format and print.
    """
    print("Pile " + str(pile_number) + ": " + ", ".join(card_pile))


def print_three_card_piles(card_piles):
    """Prints 3 card piles.

    This function uses print_card_pile to print 3 card piles for the given
    parameter.

    Parameters
    ----------
    card_piles: A 2d list containing 3 piles to be printed.

    """
    print_card_pile(1, card_piles[0])
    print_card_pile(2, card_piles[1])
    print_card_pile(3, card_piles[2])


def ask_player_for_chosen_card_pile():
    """ Asks player for chosen card pile, validates it and returns it as an int.

    Returns
    ----------
    chosen_card_pile: The pile number of the users card as an integer.
    """
    chosen_card_pile = int(input("Which number pile is your card in?"))
    # ADD VALIDATION HERE
    return chosen_card_pile


def pick_up_card_piles(chosen_card_pile, card_piles):
    """Picks up cards based on which pile chosen card is in.

    Parameters
    ----------
    chosen_card_pile: The card pile which contains the users card
    card_piles: The list of all 3 card piles.

    Returns
    ----------
    concentrated_card_pile: A list that joins the 3 card piles, with the pile
                            that contains the users card in the middle.
    """
    if chosen_card_pile == 1:
        card_piles[0], card_piles[1] = card_piles[1], card_piles[0]

    elif chosen_card_pile == 3:
        card_piles[2], card_piles[1] = card_piles[1], card_piles[2]

    concentrated_card_pile = card_piles[0] + card_piles[1] + card_piles[2]

    return concentrated_card_pile


# Start of the main game code.

deck = make_deck()

# TURN 1

deck_fragment = deal_cards_into_3_columns(deck[0:21])

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

# Extra Credit
print()
print(deck_fragment[10])
print()

users_card = deck_fragment[10]

card_piles = [deck_fragment[0:4], deck_fragment[4:8], deck_fragment[8:12], deck_fragment[12:16], deck_fragment[16:21]]

for index, pile in enumerate(card_piles):
    print_card_pile(index+1, pile)

chosen_piles = input("Please select 2 piles at random. (Seperate pile numbers with a space) ")

chosen_piles = chosen_piles.split()

chosen_piles[0], chosen_piles[1] = int(chosen_piles[0])-1, int(chosen_piles[1])-1

new_card_piles = []

if 2 in chosen_piles:
    print("All other piles will be removed.")

    for index, pile in enumerate(card_piles):
        if index in chosen_piles:
            new_card_piles.append(pile)

else:
    print("These piles will be removed")

    for index, pile in enumerate(card_piles):
        if index not in chosen_piles:
            new_card_piles.append(pile)

card_piles = new_card_piles

for index, pile in enumerate(card_piles):
    print_card_pile(index+1, pile)

users_card_pile = None

for index, pile in enumerate(card_piles):
    for card in pile:
        if card == users_card:
            users_card_pile = index
            break

if len(card_piles) > 2:
    chosen_piles = input("Please select 2 more piles. (Seperate pile numbers with a space) ")

    chosen_piles = chosen_piles.split()

    chosen_piles[0], chosen_piles[1] = int(chosen_piles[0])-1, int(chosen_piles[1])-1

    new_card_piles = []

    if users_card_pile in chosen_piles:
        print("All other piles will be removed.")

        for index, pile in enumerate(card_piles):
            if index in chosen_piles:
                new_card_piles.append(pile)

    else:
        print("These piles will be removed")

        for index, pile in enumerate(card_piles):
            if index not in chosen_piles:
                new_card_piles.append(pile)

    card_piles = new_card_piles

print()
print(card_piles)
