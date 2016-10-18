"""Simulates the popular 'Twenty One' card trick.

1.	21 cards selected from the deck.
2.	Cards are dealt into 3 columns of 7.
3.	Participant selects a card.
4.	Participent points to the pile which contains their card.
5.	Cards are picked up with the selected pile sandwiched between the others.
6.	Steps 2-5 are repeated 2 times more.
7.	The chosen card is now the 11th card in the deck.
"""

# pylint: disable=C0103, C0325, W0621

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
    """Prints 3 card piles followed by a blank line.

    This function uses print_card_pile to print 3 card piles for the given
    parameter.

    Parameters
    ----------
    card_piles: A 2d list containing 3 piles to be printed.

    """
    print_card_pile(1, card_piles[0])
    print_card_pile(2, card_piles[1])
    print_card_pile(3, card_piles[2])
    print()


def ask_player_for_chosen_card_pile():
    """Asks player for chosen card pile, validates it and returns it as an int.

    Returns
    ----------
    chosen_card_pile: The pile number of the users card as an integer.
    """
    while True:
        chosen_card_pile = input("Which number pile is your card in? ")

        if chosen_card_pile.isdigit():
            chosen_card_pile = int(chosen_card_pile)

            if 1 <= chosen_card_pile <= 3:
                return int(chosen_card_pile)

            else:
                print("Pile number has to be between 1 and 3.")

        else:
            print("Only enter the number of the pile.")

        print()


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
print()

deck_fragment = deal_cards_into_3_columns(deck[0:21])

print_three_card_piles(deck_fragment)

pile_of_chosen_card = ask_player_for_chosen_card_pile()

deck_fragment = pick_up_card_piles(pile_of_chosen_card, deck_fragment)

# TURN 2
print()

deck_fragment = deal_cards_into_3_columns(deck_fragment)

print_three_card_piles(deck_fragment)

pile_of_chosen_card = ask_player_for_chosen_card_pile()

deck_fragment = pick_up_card_piles(pile_of_chosen_card, deck_fragment)

# TURN 3
print()

deck_fragment = deal_cards_into_3_columns(deck_fragment)

print_three_card_piles(deck_fragment)

pile_of_chosen_card = ask_player_for_chosen_card_pile()

print()

print_three_card_piles(deck_fragment)

deck_fragment = pick_up_card_piles(pile_of_chosen_card, deck_fragment)


# Extra Credit


def print_multiple_card_piles(card_piles):
    """Prints formatted card piles followed by a blank line"""
    for index, pile in enumerate(card_piles):
        print_card_pile(index+1, pile)
    print()


def ask_player_for_1_pile(number_of_piles):
    """Asks player for 1 card pile, validates the input and returns it """

    # Convert number of piles to index number
    number_of_piles = int(number_of_piles) - 1

    while True:
        chosen_card_pile = input("Please select a pile at random. ")

        # If input is a number
        if chosen_card_pile.isdigit():

            chosen_card_pile = int(chosen_card_pile) - 1

            # if input more than 0 but not more than number of piles.
            if 0 <= chosen_card_pile <= number_of_piles:

                return chosen_card_pile

            # If number's not valid
            else:
                print("Please check the card pile number you have entered.")

        # If input is not a number
        else:
            print("Only enter the number of the pile.")

        print()


def ask_player_for_2_piles(number_of_piles):
    """Asks player for 2 card piles, validates the input and returns it """

    # Convert number of piles to index number
    number_of_piles = int(number_of_piles) - 1

    while True:
        chosen_card_piles = input("Please select 2 piles at random. "
                                  "(Seperate pile numbers with a space) ")

        # If input is 3 chars long and follows pattern [int][space][int].
        if (len(chosen_card_piles) == 3 and
                chosen_card_piles[0].isdigit() and
                chosen_card_piles[1] == " " and
                chosen_card_piles[2].isdigit()):

            # Split user input into list of 2 numbers
            chosen_card_piles = chosen_card_piles.split()

            # Change user input from pile numbers to pile index's
            chosen_card_piles[0] = int(chosen_card_piles[0])-1
            chosen_card_piles[1] = int(chosen_card_piles[1])-1

            # if input more than 0 but not more than number of piles.
            if ((0 <= chosen_card_piles[0] <= number_of_piles) and
                    (0 <= chosen_card_piles[1] <= number_of_piles)):

                return chosen_card_piles

            # If numbers not valid
            else:
                print("Please check the card pile numbers you have entered.")

        # If input is not [int][space][int]
        else:
            print("Please format your input with your 2 chosen "
                  "pile numbers seperated by a space")

        print()


def find_users_card_pile(users_card, card_piles):
    """Finds the pile with the users card"""

    for index, pile in enumerate(card_piles):
        for card in pile:
            if card == users_card:
                return index


def remove_piles(users_card_pile, chosen_piles, card_piles):
    """Removes chosen piles or all other piles depedning on user input

    The piles chosen by the user are removed unless the user chooses a pile
    with their own card where all other piles are removed.

    Parameters
    ----------
    """

    print()

    new_card_piles = []

    if isinstance(chosen_piles, list):

        if users_card_pile in chosen_piles:
            print("The other piles will be removed.")

            for index, pile in enumerate(card_piles):
                if index in chosen_piles:
                    new_card_piles.append(pile)

        else:
            print("These piles will be removed")

            for index, pile in enumerate(card_piles):
                if index not in chosen_piles:
                    new_card_piles.append(pile)

    else:

        if chosen_piles == users_card_pile:
            print("The other pile will be removed.")
            if chosen_pile == 0:
                card_piles.remove(card_piles[1])
            else:
                card_piles.remove(card_piles[0])

        else:
            print("This pile will be removed.")
            card_piles.remove(card_piles[chosen_pile])

        new_card_piles = card_piles

    return new_card_piles


def print_multiple_cards(card_pile):
    """Prints formatted cards followed by a blank line"""
    for index, card in enumerate(card_pile):
        print("Card " + str(index+1) + ": " + card)
    print()


def find_users_card(users_card, card_pile):
    """Finds the index of the users card"""

    for index, card in enumerate(card_pile):
        if card == users_card:
            return index


def ask_player_for_1_card(number_of_cards):
    """Asks player for 1 card pile, validates the input and returns it """

    # Convert number of piles to index number
    number_of_cards = int(number_of_cards) - 1

    while True:
        chosen_card = input("Please select a card at random. ")

        # If input is a number
        if chosen_card.isdigit():

            chosen_card = int(chosen_card) - 1

            # if input more than 0 but not more than number of piles.
            if 0 <= chosen_card <= number_of_cards:

                return chosen_card

            # If number's not valid
            else:
                print("Please check the card number you have entered.")

        # If input is not a number
        else:
            print("Only enter the number of the card.")

        print()


def ask_player_for_2_cards(number_of_cards):
    """Asks player for 2 card piles, validates the input and returns it """

    # Convert number of piles to index number
    number_of_cards = int(number_of_cards) - 1

    while True:
        chosen_cards = input("Please select 2 cards at random. "
                             "(Seperate card numbers with a space) ")

        # If input is 3 chars long and follows pattern [int][space][int].
        if (len(chosen_cards) == 3 and
                chosen_cards[0].isdigit() and
                chosen_cards[1] == " " and
                chosen_cards[2].isdigit()):

            # Split user input into list of 2 numbers
            chosen_cards = chosen_cards.split()

            # Change user input from pile numbers to pile index's
            chosen_cards[0] = int(chosen_cards[0])-1
            chosen_cards[1] = int(chosen_cards[1])-1

            # if input more than 0 but not more than number of piles.
            if ((0 <= chosen_cards[0] <= number_of_cards) and
                    (0 <= chosen_cards[1] <= number_of_cards)):

                return chosen_cards

            # If numbers not valid
            else:
                print("Please check the card numbers you have entered.")

        # If input is not [int][space][int]
        else:
            print("Please format your input with your 2 chosen "
                  "card numbers seperated by a space")

        print()


def remove_cards(users_card, chosen_cards, card_pile):
    """Removes chosen piles or all other piles depedning on user input

    The piles chosen by the user are removed unless the user chooses a pile
    with their own card where all other piles are removed.

    Parameters
    ----------
    """

    print()

    new_card_pile = []

    if isinstance(chosen_cards, list):

        if users_card in chosen_cards:
            print("The other cards will be removed.")

            for index, card in enumerate(card_pile):
                if index in chosen_cards:
                    new_card_pile.append(card)

        else:
            print("These cards will be removed")

            for index, card in enumerate(card_pile):
                if index not in chosen_cards:
                    new_card_pile.append(card)

    else:

        if chosen_cards == users_card:
            print("The other card will be removed.")
            if chosen_cards == 0:
                card_pile.remove(card_pile[1])
            else:
                card_pile.remove(card_pile[0])

        else:
            print("This card will be removed.")
            card_pile.remove(card_pile[chosen_cards])

        new_card_pile = card_pile

    return new_card_pile

# Start of main code

users_card = deck_fragment[10]

card_piles = [deck_fragment[0:4], deck_fragment[4:8], deck_fragment[8:12],
              deck_fragment[12:16], deck_fragment[16:21]]

print_multiple_card_piles(card_piles)

chosen_piles = ask_player_for_2_piles(5)

card_piles = remove_piles(2, chosen_piles, card_piles)

# While there are more then 2 piles
while len(card_piles) > 2:

    print_multiple_card_piles(card_piles)

    users_card_index = find_users_card_pile(users_card, card_piles)

    chosen_piles = ask_player_for_2_piles(len(card_piles))

    card_piles = remove_piles(users_card_index, chosen_piles, card_piles)

# If there are 2 piles left
if len(card_piles) is not 1:

    print_multiple_card_piles(card_piles)

    users_card_index = find_users_card_pile(users_card, card_piles)

    chosen_pile = ask_player_for_1_pile(2)

    card_piles = remove_piles(users_card_index, chosen_pile, card_piles)

card_pile = card_piles[0]

print("Only one pile remaining. Now I will find your card. ")

while len(card_pile) > 2:

    print_multiple_cards(card_pile)

    users_card_index = find_users_card(users_card, card_pile)

    chosen_card = ask_player_for_2_cards(len(card_pile))

    card_pile = remove_cards(users_card_index, chosen_card, card_pile)

# If there are 2 piles left
if len(card_pile) is not 1:

    print_multiple_cards(card_pile)

    users_card_index = find_users_card(users_card, card_pile)

    chosen_card = ask_player_for_1_card(2)

    card_pile = remove_cards(users_card_index, chosen_card, card_pile)

print()
print("The final card left is", card_pile[0], "your card.")


# TODO Fix code to find card after sorted into 1 pile
