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

"""
1) Deal 11 cards face down into piles
2) ask player to choose 2 piles
3) delete or keep these piles
4) continue until 2 piles left then ask for 1 pile Only
5) With last pile ask player to choose a card
6) Show them their card

"""


def print_card_pile_face_down(card_piles):
    for index, pile in enumerate(card_piles):
        if pile == [""]:
            face_down_cards = ""
        else:
            face_down_cards = (" ? of ?, " * (len(pile) - 1)) + " ? of ?"
        print("Pile " + str(index+1) + ": " + face_down_cards)


def ask_player_for_2_piles(card_piles):
    """Asks player for 2 card piles, validates the input and returns it """

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
            chosen_pile_1 = int(chosen_card_piles[0])-1
            chosen_pile_2 = int(chosen_card_piles[1])-1

            # if input more than 0 but not more than number of piles.
            if ((0 <= chosen_pile_1 <= 4) and
                    (0 <= chosen_pile_2 <= 4)):

                # If pile not empty (already removed)
                if ((card_piles[chosen_pile_1] != [""]) and
                    (card_piles[chosen_pile_2] != [""])):
                    return [chosen_pile_1, chosen_pile_2]

                else:
                    print("The pile number you have entered has already been entered")

            # If numbers not valid
            else:
                print("Please check the card pile numbers you have entered.")

        # If input is not [int][space][int]
        else:
            print("Please format your input with your 2 chosen "
                  "pile numbers seperated by a space")

        print()


def remove_piles(piles_to_remove, all_card_piles):

    # If more than 1 pile to remove
    if isinstance(piles_to_remove, list):

        if 4 in piles_to_remove:
            print("All other piles will be removed. ")

            for i in range(len(all_card_piles) - 1):
                if i not in piles_to_remove:
                    all_card_piles[i] = [""]

        else:
            print("These piles will be removed. ")

            for i in range(len(all_card_piles) - 1):
                if i in piles_to_remove:
                    all_card_piles[i] = [""]

    else:
        if 4 == piles_to_remove:
            print("The other pile will be removed. ")

            for i in range(len(all_card_piles) - 1):
                if i != piles_to_remove:
                    all_card_piles[i] = [""]

        else:
            print("This pile will be removed. ")

            all_card_piles[piles_to_remove] = [""]

    print()
    return all_card_piles


def number_of_piles_remaining(all_card_piles):

    count = 0

    for pile in all_card_piles:
        if pile != [""]:
            count += 1

    return count


def ask_player_for_1_pile(card_piles):
    """Asks player for 1 card pile, validates the input and returns it """

    while True:
        chosen_card_pile = input("Please select a pile at random. ")

        # If input is a number
        if chosen_card_pile.isdigit():

            chosen_card_pile = int(chosen_card_pile) - 1

            # if input more than 0 but not more than number of piles.
            if 0 <= chosen_card_pile <= 4:

                # If card pile not empty
                if card_piles[chosen_card_pile] != [""]:

                    return chosen_card_pile

                else:
                    print("The pile number you have entered has already been entered")

            # If number's not valid
            else:
                print("Please check the card pile number you have entered.")

        # If input is not a number
        else:
            print("Only enter the number of the pile.")

        print()


def print_2_cards(card_pile):
    print("Card 1: ? of ?")
    print("Card 2: ? of ?")
    print()


def ask_player_for_1_card(all_cards):

    while True:
        chosen_card = input("Please select a card number. ")

        # If input is a number
        if chosen_card.isdigit():

            chosen_card = int(chosen_card) - 1

            # if input 0 or 1.
            if chosen_card == 0 or 1:

                return chosen_card

            # If number's not valid
            else:
                print("Please check the card number you have entered.")

        # If input is not a number
        else:
            print("Only enter the number of the card.")

        print()


def print_last_card_removal(card_to_remove):
    if card_to_remove == 0:
        print("This card will be removed. ")
    else:
        print("The other card will be removed. ")


    print()
    print("Card 1: ")
    print("Card 2: ? of ?")
    print()

    return

print()
print(deck_fragment[10])
print()

card_piles = [deck_fragment[0:3], deck_fragment[3:5], deck_fragment[5:7],
                 deck_fragment[7:9], deck_fragment[9:11]]

print_card_pile_face_down(card_piles)
chosen_piles = ask_player_for_2_piles(card_piles)
card_piles = remove_piles(chosen_piles, card_piles)

while number_of_piles_remaining(card_piles) > 2:

    print_card_pile_face_down(card_piles)
    chosen_piles = ask_player_for_2_piles(card_piles)
    card_piles = remove_piles(chosen_piles, card_piles)

if number_of_piles_remaining(card_piles) != 1:

    print_card_pile_face_down(card_piles)
    chosen_piles = ask_player_for_1_pile(card_piles)
    card_piles = remove_piles(chosen_piles, card_piles)

the_card_pile = card_piles[4]

print_card_pile_face_down(card_piles)

print("Only one pile remaining. Now I will find your card. ")
print()

print_2_cards(the_card_pile)
chosen_card = ask_player_for_1_card(the_card_pile)
print_last_card_removal(chosen_card)

print("There is only one card left...")
print("Your card is", the_card_pile[1])
