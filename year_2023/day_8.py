class Day8:
    def loop_coord():
        pass

    def solution_pt1(documents: list[str]):
        directions = documents[0]
        values = []
        coord_tuples = []
        ZZZ = False
        for doc in documents[2:]:
            paranthesis_idx = doc.find("(")
            equal_idx = doc.find("=")
            values.append(doc[: equal_idx - 1])
            coord_tuples.append(tuple(doc[paranthesis_idx:].strip("()").split(", ")))
        coord_pos = 0 if directions[0] == "L" else 1
        next_value = coord_tuples[0][coord_pos]
        loops = 1
        while not ZZZ:
            for d in directions:
                coord_pos = 0 if d == "L" else 1
                value_idx = values.index(next_value)
                next_value = coord_tuples[value_idx][coord_pos]
                if next_value == "ZZZ":
                    loops += 1
                    ZZZ = True
                loops += 1
            loops += 1
        return loops

    def solution_pt2(self):
        pass
