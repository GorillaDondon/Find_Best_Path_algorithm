from collections import deque

path = [4,17,32,18,19,10,5,9,0]

path = sorted(path)
print(path)
path_queue = deque(path)

while path_queue:
    print(path_queue.pop())