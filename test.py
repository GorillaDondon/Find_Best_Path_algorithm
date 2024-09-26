import re
import random
from collections import deque

#  function to read and create a dictionary for a graph
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

# function to make a offspring path out of the two parent paths
# def make_offspring(path1, path2, graph):
#     offspring = []

#     # all the links conteined in the two paths
#     all_links = []
#     all_links.extend(path1)
#     all_links.extend(path2)
#     all_links = list(set(all_links))

#     random.shuffle(all_links)
#     all_links_queue = deque(all_links)

#     prob = random.random()

#     if prob < 0.33:
#         for i in range(len(path1)):
#             offspring.append(all_links_queue.pop())
#     elif prob <0.67:
#         for i in range(len(path2)):
#             offspring.append(all_links_queue.pop())
#     else:
#         if (len(path1) < len(path2)):
#             for i in range(len(path2)+3):
#                 offspring.append(all_links_queue.pop())
#         else:
#             for i in range(len(path1)+3):
#                 offspring.append(all_links_queue.pop())
    


path1 = [14, 2, 24, 16, 19, 34]
path2 = [36, 2, 17, 19, 20, 9, 16, 28, 30, 18]

graph = dictionary_maker('/Users/joejoezaki/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Documents/Semesters/Fall_2024/CSCE_480/hw/hw3/hw3/hw3_cost239.txt')

# print(graph)
# contain the links that comprises offspring
offspring = []

graph_links = list(graph)
random.shuffle(graph_links)
graph_links_queue = deque(graph_links)

# all the links in the two paths
all_links = []
all_links.extend(path1)
all_links.extend(path2)
all_links = list(set(all_links))
random.shuffle(all_links)
all_links_queue = deque(all_links)

prob = random.random()

# make a offspring of the length of the path1
if prob < 0.33:
    for i in range(len(path1)):
        offspring.append(all_links_queue.pop())
# make a offspring of the length of the path2
elif prob <0.67:
    for i in range(len(path2)):
        offspring.append(all_links_queue.pop())
# make a offspring longer than the two paths
else:
    if (len(path1) < len(path2)):
        # for i in range(len(path2)+random.randint(1, len(path1))):
        #     offspring.append(all_links_queue.pop())
        for i in range(len(path2)):
            offspring.append(all_links_queue.pop())
        for i in range(random.randint(1, len(path1))):
            new_link = graph_links_queue.pop()
            while(new_link in offspring):
                new_link = graph_links_queue.pop()
            offspring.append(new_link)

    else:
        # for i in range(len(path1)+random.randint(1, len(path2))):
        #     offspring.append(all_links_queue.pop())
        for i in range(len(path1)):
            offspring.append(all_links_queue.pop())
        for i in range(random.randint(1, len(path2))):
            new_link = graph_links_queue.pop()
            while(new_link in offspring):
                new_link = graph_links_queue.pop()
            offspring.append(new_link)

print(f"the off spring is: {offspring} length: {len(offspring)}")

