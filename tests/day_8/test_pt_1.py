from utils import ri
from year_2023 import Day8


def test_day_8_pt1():
    documents = ["LLR", "", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]
    result = Day8.solution_pt1(documents)
    assert result == 6
