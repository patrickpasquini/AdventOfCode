from year_2023 import Day6


def test_day_6_pt2():
    document = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]
    result = Day6.solution_pt2(document)
    assert result == 71503
