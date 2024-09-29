import random
from collections import deque

class Path:
    def __init__(self, path, fitness):
        self.path = path
        self.fitness = fitness
    
    def get_path(self):
        return self.path
    
    def get_fitness_score(self):
        return self.fitness


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

# Funtion that initialize the first population
def generate_path(graph):
    len_path = random.randint(1, len(graph))
    all_edge_numbers = list(range(0, 37))

    random.shuffle(all_edge_numbers)
    edge_num_queue = deque(all_edge_numbers)

    path = []
    for i in range(len_path):
        path.append(edge_num_queue.pop())

    return path

# function to make a offspring path out of the two parent paths
def make_offspring(path1, path2):

    # contain the links that comprises offspring
    offspring = []
    offspring_length = max(len(path1), len(path2))

    for _ in range(offspring_length):

        prob = random.random()

        if prob < 0.45:
            offspring.append(random.choice(path1))
        # make a offspring of the length of the path2
        elif prob <0.90:
            offspring.append(random.choice(path2))
        else:
           offspring.append(random.randint(0,36))
        
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

    max_score = len(target_nodes)*10

    edges = []
    for key in offspring:
        edges.append(graph[key])

    num_edges = len(edges)

    nodes_connected = are_connected(edges, target_nodes)

    fitness = 0

    if nodes_connected == len(target_nodes):
        fitness = max_score

    # Minimum edges required for a graph to be fully connected
    required_edges = len(target_nodes)-1

    if num_edges < required_edges:
        fitness -= (required_edges - num_edges) * 5  # Penalize for each missing edge

    unnecessary_edges = (num_edges - len(target_nodes)+1) * 5
    fitness -= unnecessary_edges

    return fitness


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

    generation = 1

    population = []

    target_nodes = [3, 5, 9, 15]

    #Create initial population
    for _ in range(population_size):
        path = generate_path(graph)

        fitness = calc_fitness_score(path, graph, target_nodes)
        path_obj = Path(path, fitness)

        population.append(path_obj)

    # Sort the population based on fitness
     
    for generation in range(100):
        population = sorted(population, key = lambda x:x.fitness, reverse=True) 

        print("Generation ", generation)

        if population[0].fitness == 1:
            break

        new_generation = []

        s = int((10*population_size)/100) 
        new_generation.extend(population[:s])
        print("The fittest offspring", new_generation[0].path)
        print("The fittest offspring", new_generation[0].fitness)

        s = int((50*population_size)/100) 
        for i in range(s):
            path1 = random.choice(population[:50])
            path2 = random.choice(population[:50])

            offspring = make_offspring(path1.path, path2.path)
            fitness = calc_fitness_score(offspring, graph, target_nodes)

            # Initialize new offspring path
            path = Path(offspring, fitness)
            new_generation.append(path)

        population = new_generation


__main__()





           


           

