import re

# Given adjacency list
def parse_adjacency_list(file_contents):
    adj = {}

    for line in file_contents:
        line = line.strip().split(":")
        key = tuple(map(int, line[0][1:-1].split(',')))

        if len(line) > 1:
            split = re.findall("\[.*?\]", line[1])
#             print(split)
            values = []
            for sub in split:
                sub = sub.replace("[", "").replace("]", "").split(",")
                values.append(tuple([int(x.strip()) for x in sub]))
            adj[key] = values
        else:
            adj[key] = []

    return adj

def find_longest_loop(adj_list, start, visited):
    stack = [(start, [start])]

    longest_loop = []

    while stack:
        current, path = stack.pop()

        visited[current] = True

        for neighbor in adj_list.get(current, []):
            if neighbor in path:
                # Loop found
                current_loop = path[path.index(neighbor):]
                if len(current_loop) > len(longest_loop):
                    longest_loop = current_loop

            if not visited.get(neighbor, False):
                stack.append((neighbor, path + [neighbor]))

    return longest_loop



def find_largest_distance(adj_list, start, visited, distance):
    stack = [(start, 0)]

    while stack:
        current, current_distance = stack.pop()

        visited[current] = True

        for neighbor in adj_list.get(current, []):
            if not visited.get(neighbor, False):
                new_distance = current_distance + 1
                distance[neighbor] = max(distance[neighbor], new_distance)
                stack.append((neighbor, new_distance))


# Initializations

with open("py_input") as f:
    adj = parse_adjacency_list(f.readlines())
# print(adj)
start_point = (111, 14)
visited_nodes = {node: False for node in adj}
distances = {node: 0 for node in adj}

# Find the largest distance
find_largest_distance(adj, start_point, visited_nodes, distances)

# Find the node with the largest distance
node_with_largest_distance = max(distances, key=distances.get)

# Find the longest loop
longest_loop = find_longest_loop(adj, start_point, visited_nodes)

# Adjusting the longest loop to include the starting point
longest_loop.append(start_point)

print(f"Longest loop: {longest_loop}")
print(f"Length of longest loop: {len(longest_loop)}")
print(f"Largest distance from {start_point} is {distances[node_with_largest_distance]} at node {node_with_largest_distance}")
