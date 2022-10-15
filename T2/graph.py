class Graph:
    def __init__(self):
        # self.nodes = {}
        self.edges = {}
        self.node_count = 0
        self.edge_count = 0

    def add_node(self, node):
        if node not in self.edges:
            self.edges[node] = []
            self.node_count += 1

    def add_edge(self, node1, node2):
        if self.edges.get(node1, 0) == 0:
            self.node_count += 1
            self.edges[node1] = []
        
        if self.edges.get(node2, 0) == 0:
            self.node_count += 1
            self.edges[node2] = []
        
        # Edges list size is max size 4
        if node2 not in self.edges[node1]:
            self.edges[node1].append(node2)
            self.edges[node2].append(node1)
            self.edge_count += 1

    def get_node(self, node):
        if node in self.nodes:
            return self.nodes[node]
        else:
            return None

    def get_edge(self, node1, node2):
        if node1 in self.edges:
            if node2 in self.edges[node1]:
                return self.edges[node1][node2]
        return None

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_node_count(self):
        return self.node_count

    def get_edge_count(self):
        return self.edge_count

    def __str__(self):
        return "Nodes: " + str(self.nodes) + "\nEdges: " + str(self.edges)
