# Five, four, fh, three, two_pair, pair, one

# n_cards =
# c_list = [n_c1, n_c2, n_c3....]
c_values = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "J": 3,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12,
}
h_values = {"five": 6, "four": 5, "fh": 4, "three": 3, "dp": 2, "pair": 1, "high": 0}


def check_cards(cards: list):
    card_dict = {}
    for card in cards:
        if card in card_dict.keys():
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    max_n = max(card_dict.values())
    min_n = min(card_dict.values())
    if max_n == 5:
        return "five"
    if max_n == 4:
        return "four"
    if max_n == 3:
        if min_n == 1:
            return "three"
        return "fh"
    if max_n == 2:
        if len(card_dict.keys()) == 4:
            return "pair"
        return "dp"
    return "high"

    # can be  2p, three


with open("test.txt", "r") as f:
    lines = f.read()
hv_dict = {}
for i, line in enumerate(lines.split("\n")):
    cards = line.split(" ")[0]
    cards = [card for card in cards]
    print(cards)
    print(check_cards(cards))
    processed_cards = check_cards(cards)
    hv_dict[i] = h_values[processed_cards]

hv_dict = dict(sorted(hv_dict.items(), key=lambda item: item[1], reverse=True))

print(hv_dict)
