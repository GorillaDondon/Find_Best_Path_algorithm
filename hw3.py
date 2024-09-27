from collections import deque

#  function to read and create a dictionary for a graph
def dictionary_maker(file_name):
    with open (file_name, 'r') as file:
        edges = []
        for line in file:
            if line.strip() and not line.strip().startswith('//'):
                parts = line.split()
                node1, node2 = int(parts[0]), int(parts[1])
                edges.append((node1, node2))

    return edges


# JO
# function to make a random path (creating an individual component)
"""
# based on the POPULATION_SIZE, loop this function to create population
# the size is randomly decided and passed to function (1-37)
fun create_chromosome(size):
    - size create one chromosome
"""

# Kiko
# Function to do Dijkstra search algorithm for fitness
# to check if a path is connected, and get the shortest path from one node
def create_sub_graph(chromosome):
    sub_graph = {}

    for c in chromosome:
        if not (graph[c][0] in sub_graph):
            sub_graph[graph[c][0]] = []
        sub_graph[graph[c][0]].append(graph[c][1])

        if not (graph[c][1] in sub_graph):
            sub_graph[graph[c][1]] = []
        sub_graph[graph[c][1]].append(graph[c][0])

    return sub_graph

def find_shortest_path(graph, start, goal):
    # Keep track of visited nodes
    visited = set()
    # Queue to store paths
    queue = deque([[start]])
    
    # BFS loop
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return len(path) - 1  # Number of edges = number of nodes in path - 1
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None  # Return None if no path exists

def calc_distance(sub_graph, visited_nodes):
    total_distance = 0
    connection_count = 1
    for i in range(len(visited_nodes)-1):
        distance = find_shortest_path(sub_graph, visited_nodes[i], visited_nodes[i+1])
        if distance != None:
            total_distance += distance
            connection_count += 1
    return total_distance, connection_count

# William
# function to calculate the fitness score 
"""
fun calc_fitness_score(chromsome):
    - if any node from M is in a chromsome
        - if there are more than two nodes in chromsome
            - if there are connections between them
                - cost of links
    - cost of links
"""

# William
# sort population based on fitness score
"""
fun sort_population():
    based on fitness score for each of chromsome, sort from the best to the worst
"""

# Kiko
# selection of population to use for mating
"""
??? extract specifi % of population based on a parameter ex) 10%
-> selection?
""" # SELECTION_SIZE must be 0-1
def selection(SELECTION_SIZE, population_with_fitness): # population_with_fitness should be sorted already
    # slice top SELECTION_SIZE % of population and return
    size = len(population_with_fitness) * SELECTION_SIZE
    
    return population_with_fitness[:size]



# JO
# take two chromosomes, and create offspring
# function to create a new generation
"""
fun create_offsprint(chromosome1, chromosome2)
    - both chromosomes are encoded
    - CROSSOVER
    - MUTATION
"""

# JO
# crossover
"""
fun crossover()
"""

#JO
# mutation
"""
fun mutation
"""

# William
# show each generation with graph colored
# show the best path from each generation
"""
fun show_generation(best_chromosome):
    - show with the library
"""


# create a dictionary representing a graph
graph = dictionary_maker('C:\\Users\\William Hall\\Desktop\\CSCE480\\HW3\\hw3_cost239.txt')
    
print(graph)






           


           

