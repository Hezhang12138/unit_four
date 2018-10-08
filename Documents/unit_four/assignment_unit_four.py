# assignment_unit_four.py
# by Frank Zhang
# Last Modified 10/8/2018
#
# "I finally finished ..."
import random


def draw_a_card(random):
    number = random.randint(1, 10)
    return number


def main():
    card1 = draw_a_card(random)
    card2 = draw_a_card(random)
    card3 = draw_a_card(random)
    card4 = draw_a_card(random)
    card5 = draw_a_card(random)
    total1 = card1 + card2
    total3 = card4 + card5
    print("You drew a", card1, "and a", card2)
    print("Your total is", total1)
    print("Would you like another card?")
    your_answer = input()
    if your_answer == "y":
        total2 = total1 + card3
        print("you drew a", card3, ", and your total is", total2)
        if total2 > 21:
            print("you lose")
        else:
            print("dealer drew two card, and the total is", total3)
            if total3 > total2:
                print("dealer wins")
            elif total3 == total2:
                print("dealer wins")
            else:
                print("you win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("dealer drew two card", card4, "and", card5, "and the total is", total3)
        if total3 > total1:
            print("dealer wins")
        elif total3 == total1:
            print("dealer wins")
        else:
            print("you win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


main()