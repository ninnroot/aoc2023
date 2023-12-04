

def get_numbers(unparsed_str: str):
    return [int(i) for i in unparsed_str.split(" ") if i.strip().isdigit()]

def main():
    x = open("input.txt").readlines()
    total_point = 0
    for i in x:
        i = i.split(":")[1]
        winning_numbers = get_numbers(i.split("|")[0])
        your_numbers = get_numbers(i.split("|")[1])
        win_count = 0
        for num in your_numbers:
            if num in winning_numbers:
                win_count += 1
        if win_count > 0:
            total_point += 2 ** (win_count-1)
    return total_point


def main2():
    x = open("input.txt").readlines()
    cards=[]
    for i in x:
        i = i.split(":")[1]
        winning_numbers = get_numbers(i.split("|")[0])
        your_numbers = get_numbers(i.split("|")[1])
        win_count = 0
        for num in your_numbers:
            if num in winning_numbers:
                win_count += 1
        cards.append((winning_numbers, your_numbers, win_count))

    total_cards = len(cards)
    for index,i in enumerate(cards):
        total_cards+=(get_cards(i, index, cards))
    print(total_cards)


def get_win_count(card):
    win_count = 0
    for i in card[1]:
        if i in card[0]:
            win_count+=1
    return win_count


def get_cards(card, card_index: int, global_cards):
    total_cards = 0
    for index, i in enumerate(global_cards[card_index+1: card_index+card[2]+1]):
        total_cards+=1
        total_cards+= get_cards(i, card_index+index+1, global_cards)

    return total_cards






main2()