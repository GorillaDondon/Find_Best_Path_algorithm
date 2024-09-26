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
# function to make a random path (creating an individual component)
"""
# based on the POPULATION_SIZE, loop this function to create population
# the size is randomly decided and passed to function (1-37)
fun create_chromosome(size):
    - size create one chromosome
"""

def generate_path(graph):
    len_path = random.randint(1, 37)
    all_edge_numbers = list(range(0, 37))

    random.shuffle(all_edge_numbers)
    edge_num_queue = deque(all_edge_numbers)

    path = []
    for i in range(len_path):
        path.append(edge_num_queue.pop())

    return path




# function to make a offspring path out of the two parent paths
def make_offspring(path1, path2, graph):
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
    
    return offspring

    

        
        
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
    ## create a dictionary representing a graph
    graph = dictionary_maker('/Users/joejoezaki/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Documents/Semesters/Fall_2024/CSCE_480/hw/hw3/hw3/hw3_cost239.txt')

    #print(graph)

    path1 = [14, 2, 24, 16, 19, 34]
    path2 = [36, 2, 17, 19, 20, 9, 16, 28, 30, 18]
    print(make_offspring(path1, path2, graph))


    """
    # 1: the first population creation 
    population_size = 5

    generation_1 = []
    for i in range(population_size):
        generation_1.append(generate_path(graph))



    print(f"The first generation is:\n{generation_1}")
    """

# 2: check if the best path is found or not? if yes, show the result and the operation is done. 
#       if not, proceed with the operations 
#       - Here, we have to decide how to finish the operation. 
#       - we can specify the number of operations, or we can end the operation 
#           once a chromesome that seems to have the best fitting score is found in new generation


# 3: conducting the mating process, and make new generation
#   - once it is done, go back to the #2 and check if you have the path with the best fitting score. 

__main__()






