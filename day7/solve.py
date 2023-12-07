from dataclasses import dataclass


@dataclass
class Hand:
    contents: list[str]
    card_counts: dict[str, int]
    """
    7: Five of a kind
    6: Four of a kind
    5: Full house
    4: Three of a kind
    3: Two pairs
    2: One pair
    1: High card
    """
    classification: int

card_map = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
}


def classify(card_counts):
    try:
        if card_map["J"] != "11" and 0 < card_counts["J"] < 5:
            # Replace Jokers with most common cards
            most_common = sorted(card_counts.items(), key=lambda x: x[1], reverse=True)[0][0]
            card_counts[most_common] += card_counts["J"]
            del card_counts["J"]
    except KeyError:
        pass
    if max(card_counts.values()) == 5:
        return 7
    elif max(card_counts.values()) == 4:
        return 6
    elif set(card_counts.values()) == {3, 2}:
        return 5
    elif max(card_counts.values()) == 3:
        return 4
    elif list(card_counts.values()).count(2) == 2:
        return 3
    elif list(card_counts.values()).count(2) == 1:
        return 2
    else:
        return 1


def parse(lines):
    split = [line.split(" ") for line in lines]
    hands = [x[0] for x in split]
    bids = [int(x[1]) for x in split]
    list_of_hands = []
    for hand, bid in zip(hands, bids):
        cards = [card_map[card] for card in hand]
        card_counts = {
            hand[0]: hand.count(hand[0]),
            hand[1]: hand.count(hand[1]),
            hand[2]: hand.count(hand[2]),
            hand[3]: hand.count(hand[3]),
            hand[4]: hand.count(hand[4])
        }
        hand_obj = Hand(cards, card_counts, classify(card_counts))
        # if card_map["J"] != "11":
        #     print(hand_obj)

        list_of_hands.append(hand_obj)
    return list_of_hands, bids


def split_hands_by_classification(parsed_hands, bids, top_rank):
    # print(parsed_hands, bids, top_rank)
    split_hands = [[] for _ in range(1, 7+1)]
    # print(split_hands)
    for hand, bid in zip(parsed_hands, bids):
        # print(hand, bid)
        for i in range(1, 7+1):
            # print(i, hand.classification)
            if hand.classification == i:
                split_hands[i-1].append((hand, bid))
    return split_hands


def solve_part1(parsed_hands, bids):
    top_rank = len(parsed_hands)
    hands_by_classification = split_hands_by_classification(parsed_hands, bids, top_rank)
    # print(hands_by_classification)

    current_rank = 1
    running_total = 0

    for classification in hands_by_classification:
        sorted_in_classification = sorted(classification, key=lambda x: x[0].contents)
        for hand, bid in sorted_in_classification:
            # print(hand.contents, bid, current_rank)
            running_total += bid * current_rank
            current_rank += 1
    return running_total


def solve_part2(parsed_hands, bids):
    top_rank = len(parsed_hands)
    hands_by_classification = split_hands_by_classification(parsed_hands, bids, top_rank)
    # print(hands_by_classification)

    current_rank = 1
    running_total = 0

    for classification in hands_by_classification:
        sorted_in_classification = sorted(classification, key=lambda x: x[0].contents)
        for hand, bid in sorted_in_classification:
            # print(hand.contents, bid, current_rank)
            running_total += bid * current_rank
            current_rank += 1
    return running_total


if __name__ == "__main__":
    with open("input") as f:
        parsed_hands, bids = parse([line.strip() for line in f.readlines()])
        print(solve_part1(parsed_hands, bids))

    with open("input") as f:
        card_map["J"] = "01"
        parsed_hands, bids = parse([line.strip() for line in f.readlines()])
        print(solve_part2(parsed_hands, bids))
