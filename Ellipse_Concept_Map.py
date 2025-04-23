import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph for the concept map.
G = nx.DiGraph()

# Define key concepts (nodes)
nodes = [
    "Conic Section",
    "Focus",
    "Directrix",
    "Eccentricity (e)",
    "Parabola (e = 1)",
    "Ellipse (e < 1)",
    "Hyperbola (e > 1)",
    "Center",
    "Axes (major/minor)",
    "Vertices",
    "Latus Rectum",
    "Chord",
    "Auxiliary Circle"
]

# Add nodes
for node in nodes:
    G.add_node(node)

# Define relationships (edges)
edges = [
    ("Conic Section", "Focus"),
    ("Conic Section", "Directrix"),
    ("Conic Section", "Eccentricity (e)"),
    ("Eccentricity (e)", "Parabola (e = 1)"),
    ("Eccentricity (e)", "Ellipse (e < 1)"),
    ("Eccentricity (e)", "Hyperbola (e > 1)"),
    ("Ellipse (e < 1)", "Center"),
    ("Ellipse (e < 1)", "Axes (major/minor)"),
    ("Axes (major/minor)", "Vertices"),
    ("Ellipse (e < 1)", "Focus"),
    ("Ellipse (e < 1)", "Latus Rectum"),
    ("Ellipse (e < 1)", "Chord"),
    ("Ellipse (e < 1)", "Auxiliary Circle"),
    ("Axes (major/minor)", "Auxiliary Circle")
]

# Add edges
G.add_edges_from(edges)

# Choose a layout for the concept map
pos = nx.spring_layout(G, k=1.0, seed=42)  # using spring layout for better spacing

# Draw nodes and edges
plt.figure(figsize=(10,10))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1500)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

plt.title("Concept Map: Conic Sections and the Ellipse")
plt.axis('off')
plt.show()