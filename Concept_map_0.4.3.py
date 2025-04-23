from graphviz import Digraph

# Create a directed Graphviz diagram for section 0.4.3
dot = Digraph(comment='Detailed Concept Map for 0.4.3: Condition for Tangency')
dot.attr(rankdir='TB')

# Nodes for the detailed process.
dot.node('A', 'Start: Consider line\n y = m x + c')
dot.node('B', 'Substitute into ellipse:\n x²/a² + (m x + c)²/b² = 1')
dot.node('C', 'Form quadratic: A x² + B x + C = 0')
dot.node('D', 'Identify coefficients:\nA = 1/a² + m²/b²\nB = 2 m c/b²\nC = c²/b² - 1')
dot.node('E', 'Compute Discriminant:\nD = B² - 4 A C')
dot.node('F', 'Tangency Condition:\nSet D = 0')
dot.node('G', 'Solve for c:\n c² = a² m² + b²')
dot.node('H', 'Conclusion: Line is tangent to the ellipse')
dot.node('I', 'End')

# Connect the nodes.
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'I')

# Render the diagram as PNG.
dot.render('detailed_concept_04_3', format='png', view=True)