import re
import random
from collections import deque


# function to make a dictionary representing a graph, where the number of links are used as keys
def dictionary_maker(file_name):
    with open (file_name, 'r') as file:
        graph = {}
        for line in file:
            if line.strip() and not line.strip().startswith('//'):
                match = re.search(r'(\d+)\s+(\d+)\s+//.*#(\d+)', line)

                if match:
                    node1 = int(match.group(1))
                    node2 = int(match.group(2))
                    edge_num = int(match.group(3))

                graph[edge_num] = (node1, node2)

    graph = {k:graph[k] for k in sorted (graph)}

    return graph

graph = dictionary_maker('/Users/joejoezaki/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Documents/Semesters/Fall_2024/CSCE_480/hw/hw3/hw3/hw3_cost239.txt')
path = [12, 34, 22, 31, 36, 8, 3, 0]

def create_sub_graph(chromosome, graph):
    sub_graph = {}

    for c in chromosome:
        if not (graph[c][0] in sub_graph):
            sub_graph[graph[c][0]] = []
        sub_graph[graph[c][0]].append(graph[c][1])

        if not (graph[c][1] in sub_graph):
            sub_graph[graph[c][1]] = []
        sub_graph[graph[c][1]].append(graph[c][0])

    return sub_graph

print(create_sub_graph(path, graph))