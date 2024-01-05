from year_2023 import Day7


def test_day_7_pt2():
    documents = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]
    day_7 = Day7()
    result = day_7.solution_pt2(documents)
    assert result == 5905
