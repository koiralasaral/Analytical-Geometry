from graphviz import Digraph

# Create a directed Graphviz diagram for section 0.4.1
dot = Digraph(comment='Detailed Concept Map for 0.4.1: Intersection of a Line with an Ellipse')
dot.attr(rankdir='TB')  # Layout: top-to-bottom

# Define the nodes with detailed labels.
dot.node('A', 'Ellipse Equation\nx²/a² + y²/b² = 1')
dot.node('B', 'Line Equation\n y = m x + c')
dot.node('C', 'Substitute the line into the ellipse\n→ Obtain: x²/a² + (m x + c)²/b² = 1')
dot.node('D', 'Rearrange to form quadratic:\nA x² + B x + C = 0')
dot.node('E', 'Identify coefficients:\nA = 1/a² + m²/b²\nB = 2 m c / b²\nC = c²/b² – 1')
dot.node('F', 'Compute Discriminant:\nD = B² – 4 A C')
dot.node('G', 'Decision:\nIf D > 0 → Secant (two intersections)\nIf D = 0 → Tangent (one intersection)\nIf D < 0 → No intersection')
dot.node('H', 'End')

# Connect the nodes to represent the flow.
dot.edge('A', 'C')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')

# Render and export the diagram as PNG.
dot.render('detailed_concept_04_1', format='png', view=True)