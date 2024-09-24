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
"""
"""

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
"""

# Kiko
# encode chromosome
"""
fun encode_chromosome(chromosome, size):
    - hexidecimal encoding
    - padding or dropping if needed to, based on the size
    (ex) one chromosome can be 8 and the other can be 12 but they have to be the same size to mate)

    return encoded_chromosome
"""

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






           


           

