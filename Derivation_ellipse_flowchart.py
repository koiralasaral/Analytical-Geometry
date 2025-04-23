import networkx as nx
import matplotlib.pyplot as plt

# Create a new directed graph for the flow chart.
F = nx.DiGraph()

# Define steps in the derivation process (nodes)
steps = {
    "Start": "Locus definition:\nDistance ratio = e (constant)",
    "Focus & Directrix": "Identify fixed focus (S) and directrix (L)",
    "Perpendicular": "Drop perpendicular from point P to directrix",
    "Distance Ratio": "Set SP = e * PM",
    "Algebra": "Square distances and manipulate equations",
    "Center & Axes": "Define center (C) and set axes along CA and perpendicular",
    "Standard Form": r"Obtain $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$",
    "Properties": "Determine vertices, foci, and latus rectum"
}

# Add nodes to the flow chart
for key, label in steps.items():
    F.add_node(key, label=label)

# Define the flow (edges)
flow_edges = [
    ("Start", "Focus & Directrix"),
    ("Focus & Directrix", "Perpendicular"),
    ("Perpendicular", "Distance Ratio"),
    ("Distance Ratio", "Algebra"),
    ("Algebra", "Center & Axes"),
    ("Center & Axes", "Standard Form"),
    ("Standard Form", "Properties")
]

F.add_edges_from(flow_edges)

# Use a shell layout so that nodes appear in order.
pos = nx.shell_layout(F)

# Draw the flow chart nodes & edges with labels.
plt.figure(figsize=(12,8))
node_labels = nx.get_node_attributes(F, 'label')
nx.draw_networkx_nodes(F, pos, node_color='lightgreen', node_size=2500)
nx.draw_networkx_edges(F, pos, arrows=True, arrowstyle='->', arrowsize=20, edge_color='black')
nx.draw_networkx_labels(F, pos, labels=node_labels, font_size=9, font_family='sans-serif')

plt.title("Flow Chart: Derivation of the Standard Ellipse Equation")
plt.axis('off')
plt.show()