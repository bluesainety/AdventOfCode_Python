import math
import re

from helper import file_handler as fh, matcher


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.name)


lines = fh.readLinesFromFile("Inputs/Day8.txt", " = ", True)
node_strings = lines[1:]
instructions = lines[0][0]

nodes: [Node] = []

for node_string in node_strings:
    neighbors = re.findall(r"\w{3}", node_string[1])
    nodes.append(Node(node_string[0], neighbors[0], neighbors[1]))


def find(name) -> Node:
    return next(node for node in nodes if node.name == name)


def find_next(node: Node, instruction) -> Node:
    return matcher.find(node.left if instruction == 'L' else node.right,
                        nodes, lambda n: n.name)

def follow_path():
    counter, index = 0, 0
    next_node = matcher.find("AAA", nodes, lambda n: n.name)

    while index <= len(instructions):
        counter += 1
        next_node = find_next(next_node, instructions[index])

        if next_node.name == "ZZZ":
            break

        index = (index + 1) % len(instructions)

    print(counter)


def follow_ghost_path():
    counter, index = 0, 0
    multiples: [int] = []
    starting_nodes: [Node] = matcher.match_pattern_all(r"..A", nodes, lambda n: n.name)

    while len(multiples) < 6:
        counter += 1
        starting_nodes = [find_next(node, instructions[index]) for node in starting_nodes]

        if matcher.match_pattern_all(r"..Z", starting_nodes, lambda n: n.name):
            multiples.append(counter)

        index = (index + 1) % len(instructions)

    print(multiples)
    print(math.lcm(*multiples))


follow_path()
follow_ghost_path()
