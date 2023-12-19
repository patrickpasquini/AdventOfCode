import re


class Race:
    def __init__(self, time: int, record_distance: int):
        self.time = time
        self.record_distance = record_distance

    def find_winners_possibilites(self):
        winners_possibilites = 0
        for t in range(1, self.time + 1):
            distance = (self.time - t) * t
            if distance > self.record_distance:
                winners_possibilites += 1
        return winners_possibilites


class Day6:
    def solution_pt1(documents: list[str]):
        numbers = [
            num for doc in documents for num in re.findall(r"\d+", doc.split(":")[1])
        ]
        times = numbers[: len(numbers) // 2]
        record_distances = numbers[len(numbers) // 2 :]

        result = 1
        for i in range(len(record_distances)):
            race = Race(time=int(times[i]), record_distance=int(record_distances[i]))
            result *= race.find_winners_possibilites()
        return result

    def solution_pt2(documents: list[str]):
        numbers = [
            num for doc in documents for num in re.findall(r"\d+", doc.split(":")[1])
        ]
        times = numbers[: len(numbers) // 2]
        record_distances = numbers[len(numbers) // 2 :]
        time = int("".join(times))
        record_distance = int("".join(record_distances))
        race = Race(time=time, record_distance=record_distance)
        return race.find_winners_possibilites()
