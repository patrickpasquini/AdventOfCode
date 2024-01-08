class Day8:
    def solution_pt1(documents: list[str]):
        directions = documents[0]
        nodes = {}
        for doc in documents[2:]:
            node_name, node_values = doc.split(" = ")
            nodes[node_name] = tuple(node_values.strip("()").split(", "))
        actual_node = "AAA"
        direction_index = 0
        steps = 0
        while actual_node != "ZZZ":
            direction = directions[direction_index % len(directions)]
            actual_node = nodes[actual_node][0 if direction == "L" else 1]
            direction_index += 1
            steps += 1

        return steps

    def solution_pt2(self):
        pass
