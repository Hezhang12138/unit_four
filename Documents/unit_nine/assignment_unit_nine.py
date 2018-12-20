import card
import deck


def deal_cards():
    deck1 = deck.Deck()
    deck.shuffle()
    list1 = []
    list2 = []
    for x in range(5):
        card1 = deck1.draw_a_card()
        card2 = deck1.draw_a_card()
        list1.append(card1)
        list2.append(card2)
    return list1, list2


def compare_cards():
    result1 = 0
    result2 = 0


def main():
    player1, player2 = deal_cards()
    compared_to(list1, list2)

