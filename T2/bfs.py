# Create a BFS function that finds all of the connected components in a graph based on
# the graph structure implemented on graph.py

def bfs(G, s):
    visited = set()
    queue = [s]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(G[node] - visited)
    return visited


def connected_components(G):
    components = []
    visited = set()
    for node in G:
        if node not in visited:
            component = bfs(G, node)
            components.append(component)
            visited.update(component)
    return components
    