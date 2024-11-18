import networkx as nx

# Create a graph for the traffic network
G = nx.Graph()

# Add edges (roads) between nodes (intersections)
# Format: (node1, node2, traffic_volume)
edges = [
    ("A", "B", 50),
    ("A", "C", 70),
    ("B", "D", 60),
    ("C", "D", 80),
    ("C", "E", 90),
    ("D", "E", 40)
]

# Add edges to the graph with weights
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)

# Print the degree centrality values
print("Degree Centrality of each intersection:")
for node, centrality in degree_centrality.items():
    print(f"{node}: {centrality:.4f}")
