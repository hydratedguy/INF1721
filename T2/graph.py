import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        # self.nodes = {}
        self.edges = {}
        self.node_count = 0
        self.edge_count = 0
        self.visual = []

    def add_node(self, node):
        if self.edges.get(node, 0) == 0:
            self.node_count += 1
            self.edges[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
       
        # Edges list size is max size 4
        if node2 not in self.edges[node1]:
            self.edges[node1].append(node2)
            self.edges[node2].append(node1)
            self.visual.append([node1,node2])
            self.edge_count += 1


    def get_node(self, node):
        if self.edges.get(node, 0) != 0:
            return self.edges[node]
        else :
            return -1

    def get_edge(self, node1, node2):
        if node1 in self.edges:
            if node2 in self.edges[node1]:
                return self.edges[node1][node2]
        return None

    def get_nodes(self):
        nodes = []
        for k in self.edges.items():
            nodes.append(k)
        return nodes

    def get_edges(self):
        return self.edges

    def get_node_count(self):
        return self.node_count

    def get_edge_count(self):
        return self.edge_count
    
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

    def __str__(self):
        return "Nodes: " + str(self.node_count) + "\nEdges: " + str(self.edge_count)
