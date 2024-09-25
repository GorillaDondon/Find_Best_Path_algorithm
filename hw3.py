import re
import random

#  function to read and create a dictionary for a graph
def dictionary_maker(file_name):
    with open (file_name, 'r') as file:
        graph = {}
        for line in file:
            if line.strip() and not line.strip().startswith('//'):
                parts = line.split()
                node1, node2 = int(parts[0]),int(parts[1])
                if not node1 in graph:
                    graph[node1] = []
                if not node2 in graph:
                    graph[node2] = []

                # use the regular expression to extract the number next to '#'
                match = re.search(r'#(\d+)', line)
                edge_num = int(match.group(1))

                graph[node1].append((node2, edge_num))
                graph[node2].append((node1, edge_num))

        # sort the keys        
        graph = {k: graph[k] for k in sorted(graph)}

    return graph

# function to make a dictionary representing a graph, where the number of links are used as keys


# function to create a random path
def generate_path(graph):
    len_path = random.randint(1, 37)


    

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


# create a dictionary representing a graph
graph = dictionary_maker('/Users/joejoezaki/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Documents/Semesters/Fall_2024/CSCE_480/hw/hw3/hw3/hw3_cost239.txt')
    
print(graph)

print()
print(graph[0])
print(graph[0][0])
print(graph[0][0][1])

# edge number is graph[node1][index in node1 key][1]





