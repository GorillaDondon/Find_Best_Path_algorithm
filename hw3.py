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

# function to make a dictionary representing a graph, where the number of links are used as keys


# function to create a random path
def generate_path(graph):
    len_path = random.randint(1, 37)
    all_edge_numbers = list(range(0, 37))

    random.shuffle(all_edge_numbers)
    edge_num_queue = deque(all_edge_numbers)

    path = []
    for i in range(len_path):
        path.append(edge_num_queue.pop())

    return path




        



    

# function to make a random path (creating an individual component)
"""
# based on the POPULATION_SIZE, loop this function to create population
# the size is randomly decided and passed to function (1-37)
fun create_chromosome(size):
    - size create one chromosome
"""

# function to calculate the fitness score 
"""
fun calc_fitness_score(chromsome):
    - if any node from M is in a chromsome
        - if there are more than two nodes in chromsome
            - if there are connections between them
                - cost of links
    - cost of links
"""

# sort population based on fitness score
"""
fun sort_population():
    based on fitness score for each of chromsome, sort from the best to the worst
"""

# selection of population to use for mating
"""
??? extract specifi % of population based on a parameter ex) 10%
-> selection?
"""

# encode chromosome
"""
fun encode_chromosome(chromosome, size):
    - hexidecimal encoding
    - padding or dropping if needed to, based on the size
    (ex) one chromosome can be 8 and the other can be 12 but they have to be the same size to mate)

    return encoded_chromosome
"""

# take two chromosomes, and create offspring
# function to create a new generation
"""
fun create_offsprint(chromosome1, chromosome2)
    - both chromosomes are encoded
    - CROSSOVER
    - MUTATION
"""

# crossover
"""
fun crossover()
"""

# mutation
"""
fun mutation
"""

# show each generation with graph colored
# show the best path from each generation
"""
fun show_generation(best_chromosome):
    - show with the library
"""


# function for main 
def __main__():
    # create a dictionary representing a graph
    graph = dictionary_maker('/Users/joejoezaki/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Documents/Semesters/Fall_2024/CSCE_480/hw/hw3/hw3/hw3_cost239.txt')
    
    # 1: the first population creation 
    population_size = 5

    generation_1 = []
    for i in range(population_size):
        generation_1.append(generate_path(graph))

    print(f"The first generation is:\n{generation_1}")

    # 2: check if the best path is found or not? if yes, show the result and the operation is done. 
    #       if not, proceed with the operations 
    #       - Here, we have to decide how to finish the operation. 
    #       - we can specify the number of operations, or we can end the operation 
    #           once a chromesome that seems to have the best fitting score is found in new generation


    # 3: conducting the mating process, and make new generation
    #   - once it is done, go back to the #2 and check if you have the path with the best fitting score. 

__main__()




# edge number is graph[node1][index in node1 key][1]


"""

{0: (0, 1), 
 1: (0, 2), 
 2: (2, 8), 
 3: (8, 18), 
 4: (17, 18), 
 5: (16, 17), 
 6: (15, 16), 
 7: (7, 15), 
 8: (5, 7), 
 9: (5, 6), 
 10: (6, 11), 
 11: (10, 11), 
 12: (9, 10), 
 13: (9, 12), 
 14: (12, 14), 
 15: (13, 14), 
 16: (1, 13), 
 17: (1, 3), 
 18: (3, 4), 
 19: (2, 4), 
 20: (1, 2), 
 21: (1, 5), 
 22: (2, 5), 
 23: (1, 11), 
 24: (5, 11), 
 25: (2, 7), 
 26: (7, 8), 
 27: (8, 13), 
 28: (8, 15), 
 29: (8, 17), 
 30: (11, 15), 
 31: (11, 13), 
 32: (13, 15), 
 33: (13, 16), 
 34: (1, 9), 
 35: (10, 12), 
 36: (12, 13)}

"""


