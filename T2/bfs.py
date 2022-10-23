# Create a BFS function that finds all of the connected components in a graph based on
# the graph structure implemented on graph.py

def bfs(G, s):
    visited = {}
    queue = [s]
    while queue:
        node = queue.pop(0)
        if visited.get(node, 0) == 0:
            visited[node] = 1
            queue.extend(G.edges[node])
    return visited


def connected_components(G):
    components = []
    visited = {}
    for node in G.edges:
        if visited.get(node, 0) == 0:
            component = bfs(G, node)
            components.append(component)
            visited.update(component)

    return components