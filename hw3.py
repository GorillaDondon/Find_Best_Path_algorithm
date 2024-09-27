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

# function to make a random path (creating an individual component)
# based on the POPULATION_SIZE, loop this function to create population
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

    # all the links (edges) in the graph
    graph_links = list(graph)
    random.shuffle(graph_links)
    graph_links_queue = deque(graph_links)

    # all the links (edges) in the two paths
    all_links = []
    all_links.extend(path1)
    all_links.extend(path2)
    all_links = list(set(all_links)) # to prevent the duplication of the same link 
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
        # the idea is to first get an offspring of the same length as the longer parent path, and then, 
        #   add new links (the number of links is randomly decided less than the number of shorter path) to the offspring
        #   By randomly adding some links, it works as mutation
        if (len(path1) < len(path2)):
            # first, get links for the number of length of the longer path (in his case, path2)
            for i in range(len(path2)):
                offspring.append(all_links_queue.pop())
            
            # additionally, add new links for the number of length less than that of the shorter path (in this case, path1)
            for i in range(random.randint(1, len(path1))):
                if (not graph_links_queue):
                    break
                new_link = graph_links_queue.pop()
                while(new_link in offspring):
                    if (not graph_links_queue):
                        break
                    new_link = graph_links_queue.pop()
                offspring.append(new_link)

        else:
            # first, get links for the number of length of the longer path (in his case, path1)
            for i in range(len(path1)):
                offspring.append(all_links_queue.pop())

            # additionally, add new links for the number of length less than that of the shorter path (in this case, path1)
            for i in range(random.randint(1, len(path2))):
                if (not graph_links_queue):
                    break
                new_link = graph_links_queue.pop()
                while(new_link in offspring):
                    if (not graph_links_queue):
                        break
                    new_link = graph_links_queue.pop()
                offspring.append(new_link)
    
    return offspring

# function to generate a new generation. suppose that the parameter 'current_population' is 
#   already sorted based on fitness score
def make_new_generation(current_population, graph):
    # get the population size
    population_size = len(current_population)

    # store paths to be considered to be in new generation
    paths = current_population

    # store the paths for a new generation
    new_generation = []

    # store the new generated offspring paths
    offspring_paths = []

    # make offsprings first
    for i in range(population_size):
        # randomly select 2 parent paths out of the best 50% fitting paths
        parent_path1 = random.choice(current_population[0:(len(current_population)/2)])
        parent_path2 = random.choice(current_population[0:(len(current_population)/2)])
        offspring_paths.append(make_offspring(parent_path1, parent_path2, graph))

    # then, merge it with the current population
    paths.append(offspring_paths)
    
    # sort it based on the fitness score.
    # ---------- here i need to use the calc fit ness function ---------

    # select the best paths for the number of the length of the current population, and make a new generation
    paths_queue = deque(paths)
    for i in range(population_size):
        new_generation.append(paths_queue.pop())

    # return the new population, here it is not sorted based on fitness score
    return new_generation
 
# Willy: function to calculate the fitness score 
"""
fun calc_fitness_score(chromsome):
    - if any node from M is in a chromsome
        - if there are more than two nodes in chromsome
            - if there are connections between them
                - cost of links
    - cost of links
"""

# Kiko: sort population based on fitness score
"""
fun sort_population():
    based on fitness score for each of chromsome, sort from the best to the worst
"""

# show each generation with graph colored
# show the best path from each generation
"""
fun show_generation(best_chromosome):
    - show with the library
"""

# function for main 
def __main__():
    graph = dictionary_maker('/Users/joejoezaki/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Documents/Semesters/Fall_2024/CSCE_480/hw/hw3/hw3/hw3_cost239.txt')

    # 1: the first population creation 
    population_size = 100

    current_population = []
    for i in range(population_size):
        current_population.append(generate_path(graph))
    

    # 2: check if the best path is found or not? if yes, show the result and the operation is done. 
    #       if not, proceed with the operations 
    #       - Here, we have to decide how to finish the operation. 
    #       - we can specify the number of operations, or we can end the operation 
    #           once a chromesome that seems to have the best fitting score is found in new generation

    # 3: conducting the mating process, and make new generation
    #   - once it is done, go back to the #2 and check if you have the path with the best fitting score. (while loop?)
    new_generation = make_new_generation(current_population, graph)

__main__()






