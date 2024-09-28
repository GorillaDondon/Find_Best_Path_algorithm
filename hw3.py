import random
from collections import deque

# function to read and create a dictionary for a graph
def dictionary_maker(file_name):
    with open (file_name, 'r') as file:
        graph = {}
        counter = 0
        for line in file:
            if line.strip() and not line.strip().startswith('//'):
                parts = line.split()
                node1, node2 = int(parts[0]), int(parts[1])
                graph[counter] = (node1, node2)
                counter += 1

    return graph

# function to make a random path (creating an individual component) only once in the beginning
# based on the POPULATION_SIZE, loop this function to create population
def generate_path():
    len_path = random.randint(1, 30)
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

    print("queue", all_links)

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

# DFS search through the graph
def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

# Function to see how many nodes are connected
def are_connected(edges, nodes):

    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Check if any nodes to check exist in the graph
    if not any(node in graph for node in nodes):
        return 0
    
    visited = set()
    for node in nodes:
        if node in graph:
            dfs(node, graph, visited)
            break  # Start DFS from the first existing node

    # Count how many of the nodes_to_check are in visited
    connected_count = sum(node in visited for node in nodes)

    return connected_count

# Calculates the fitness of the offspring
def calc_fitness_score(offspring, graph, target_nodes):
    offspring = [graph[key] for key in offspring]

    nodes_connected = are_connected(offspring, target_nodes)

    num_edges = len(offspring)

    fitness = nodes_connected/(1+num_edges)

    return fitness

# function to generate a new generation. suppose that the parameter 'current_population' is 
#   already sorted based on fitness score
def make_new_generation(current_population, graph):
    # get the population size
    population_size = len(current_population)

    # store the paths for a new generation
    new_generation = []

    # store the new generated offspring paths
    offspring_paths = []

    # make offsprings first
    for i in range(population_size):
        # randomly select 2 parent paths out of the best 50% fitting paths
        parent_path1 = random.choice(current_population[0:(len(current_population)//2)])
        parent_path2 = random.choice(current_population[0:(len(current_population)//2)])

        offspring = make_offspring(parent_path1, parent_path2, graph)

        fittness = calc_fitness_score(offspring, graph, target_nodes=[3,6,9,12])

        offspring_paths.append((fittness, offspring))

    for path in current_population:
        if isinstance(path, tuple):
            paths_with_fitness = current_population  # If fitness is already paired with paths
        else:
            # Calculate fitness if it's not paired yet
            paths_with_fitness = [(calc_fitness_score(path, graph, target_nodes=[3, 6, 9, 12]), path)
                                  for path in current_population]

    # Merge offspring and current population (both with fitness scores)
    all_paths_with_fitness = paths_with_fitness + offspring_paths

    # Sort the combined list by fitness score in descending order (from highest to lowest)
    all_paths_with_fitness.sort(reverse=True, key=lambda x: x[0])  # Sort by fitness score (x[0])

    # Select the best paths (based on fitness) to form the new generation
    paths_queue = deque(all_paths_with_fitness)
    for i in range(population_size):
        new_generation.append(paths_queue.popleft())  # Take the best (highest fitness) paths
        
    # return the new population, here it is not sorted based on fitness score
    return new_generation
 

# show each generation with graph colored
# show the best path from each generation
"""
fun show_generation(best_chromosome):
    - show with the library
"""

# function for main 
def __main__():
    graph = dictionary_maker('C:\\Users\\William Hall\\Desktop\\CSCE480\\HW3\\hw3_cost239.txt')
    # 1: the first population creation 
    population_size = 100

    current_population = []
    for i in range(population_size):
        current_population.append(generate_path())
    

    # 2: check if the best path is found or not? if yes, show the result and the operation is done. 
    #       if not, proceed with the operations 
    #       - Here, we have to decide how to finish the operation. 
    #       - we can specify the number of operations, or we can end the operation 
    #           once a chromesome that seems to have the best fitting score is found in new generation

    # 3: conducting the mating process, and make new generation
    #   - once it is done, go back to the #2 and check if you have the path with the best fitting score. (while loop?)
    for _ in range(100):
        new_generation = make_new_generation(current_population, graph)

__main__()





           


           

