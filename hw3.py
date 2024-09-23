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
                graph[node1].append(node2)
                graph[node2].append(node1)

        # sort the keys        
        graph = {k: graph[k] for k in sorted(graph)}

    return graph

# function to make a random path (creating an individual component)

# function to calculate the fitness score 

# function to create a new generation




# create a dictionary representing a graph
graph = dictionary_maker('/Users/joejoezaki/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Documents/Semesters/Fall_2024/CSCE_480/hw/hw3/hw3/hw3_cost239.txt')
    
print(graph)






           

