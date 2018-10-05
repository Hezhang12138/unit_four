# assignment_unit_four.py
# by Frank Zhang
# Last Modified
#
#
import random


def draw_a_card(random):
    number = random.randint(1, 10)
    return number


def main():
    card1 = draw_a_card(random)
    card2 = draw_a_card(random)
    total1 = card1 + card2
    print("You drew a", card1, "and a", card2)
    print("Your total is", total1)
    print("Would you like another card")


main()