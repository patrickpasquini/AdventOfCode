from collections import Counter


class Day7:
    mapping_pt1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    mapping_pt2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )
    total_points = 0
    i = 1

    def append_game(
        self,
        most_common_char: list[tuple],
        ordered_high_card: list,
        value: int,
    ):
        if most_common_char[0][1] == 1:
            self.high_card.append((ordered_high_card, value))
        elif most_common_char[0][1] == 2 and most_common_char[1][1] != 2:
            self.one_pair.append((ordered_high_card, value))
        elif most_common_char[0][1] == 2:
            self.two_pair.append((ordered_high_card, value))
        elif most_common_char[0][1] == 3 and most_common_char[1][1] != 2:
            self.three_kind.append((ordered_high_card, value))
        elif most_common_char[0][1] == 3:
            self.full_house.append((ordered_high_card, value))
        elif most_common_char[0][1] == 4:
            self.four_kind.append((ordered_high_card, value))
        else:
            self.five_kind.append((ordered_high_card, value))

    def order_hand(self, hand: list):
        return sorted(hand, key=lambda x: x[0], reverse=True)

    def solution_pt1(self, documents: list[str]):
        for doc in documents:
            g, value = doc[:5], int(doc[6:])
            ordered_high_card = []
            for char in g:
                idx = self.mapping_pt1.index(char)
                ordered_high_card.append(idx)
            counter = Counter(g)
            most_common_char = counter.most_common(2)
            self.append_game(most_common_char, ordered_high_card, value)
        high_card_ordered = self.order_hand(self.high_card)
        one_pair_ordered = self.order_hand(self.one_pair)
        two_pairs_ordered = self.order_hand(self.two_pair)
        three_kind_ordered = self.order_hand(self.three_kind)
        full_house_ordered = self.order_hand(self.full_house)
        four_kind_ordered = self.order_hand(self.four_kind)
        five_kind_ordered = self.order_hand(self.five_kind)
        for game_type in [
            high_card_ordered,
            one_pair_ordered,
            two_pairs_ordered,
            three_kind_ordered,
            full_house_ordered,
            four_kind_ordered,
            five_kind_ordered,
        ]:
            for g in game_type:
                self.total_points += g[1] * self.i
                self.i += 1
        return self.total_points

    def solution_pt2(self, documents: list[str]):
        for doc in documents:
            game, value = doc[:5], int(doc[6:])
            game_idx = [self.mapping_pt2.index(char) for char in game]
            counter = Counter(game)
            j_qtd = counter.get("J", 0)
            most_common = counter.most_common(2)
            key = most_common[0][0]
            most_common_dict = [{tpl[0]: tpl[1]} for tpl in most_common]
            list_pos = 0
            if len(most_common) > 1:
                second_counter_key = most_common[1][0]
                if key == "J":
                    list_pos = 1
                    key = second_counter_key
            most_common_dict[list_pos][key] = j_qtd + most_common_dict[list_pos][key]
            most_common = tuple(
                (key, value) for d in most_common_dict for key, value in d.items()
            )
            self.append_game(most_common, game_idx, value)
        high_card_ordered = self.order_hand(self.high_card)
        one_pair_ordered = self.order_hand(self.one_pair)
        two_pairs_ordered = self.order_hand(self.two_pair)
        three_kind_ordered = self.order_hand(self.three_kind)
        full_house_ordered = self.order_hand(self.full_house)
        four_kind_ordered = self.order_hand(self.four_kind)
        five_kind_ordered = self.order_hand(self.five_kind)
        for game_type in [
            high_card_ordered,
            one_pair_ordered,
            two_pairs_ordered,
            three_kind_ordered,
            full_house_ordered,
            four_kind_ordered,
            five_kind_ordered,
        ]:
            for g in game_type:
                self.total_points += g[1] * self.i
                self.i += 1
        return self.total_points
