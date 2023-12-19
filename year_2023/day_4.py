def solution_pt1(winning_numbers: list[int], matching_numbers: list[int]):
    result = 0
    for num in matching_numbers:
        if num in winning_numbers:
            result = 1 if result == 0 else result * 2
    return result


def solution_pt2(
    winning_numbers: list[int],
    matching_numbers: list[int],
    scratchcards: dict,
    game: int,
):
    points = sum(num in winning_numbers for num in matching_numbers)
    for j in range(game, game + points):
        scratchcards[j + 1] += scratchcards[game]


def scratchcards(document: list[str]):
    scratchcards = {i: 1 for i in range(1, len(document) + 1)}
    for idx, line in enumerate(document, start=1):
        _, line = line.split(":")
        winning_numbers, matching_numbers = line.split("|")
        winning_numbers = [int(num) for num in winning_numbers.split()]
        matching_numbers = [int(num) for num in matching_numbers.split()]
        solution_pt2(winning_numbers, matching_numbers, scratchcards, idx)
    return sum(scratchcards.values())
