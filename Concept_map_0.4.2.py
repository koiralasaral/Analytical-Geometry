from graphviz import Digraph

# Create a directed Graphviz diagram for section 0.4.2
dot = Digraph(comment='Detailed Concept Map for 0.4.2: Tangent and Normal at a Point on the Ellipse')
dot.attr(rankdir='TB')  # top-to-bottom direction

# Define the nodes for a detailed breakdown.
dot.node('A', 'Select a point P on the ellipse\nP = (a cosθ, b sinθ)')
dot.node('B', 'Tangent Equation (Standard Form)\n(x*x₁)/a² + (y*y₁)/b² = 1')
dot.node('C', 'Differentiate the ellipse implicitly\n→ dy/dx = - (b² x)/(a² y)')
dot.node('D', 'Compute the slope of the tangent at P\n(using either method)')
dot.node('E', 'Form the tangent line (point-slope form)')
dot.node('F', 'Compute the Normal Line\nNormal slope = -1/(tangent slope)')
dot.node('G', 'End')

# Define the flow.
dot.edge('A', 'B', label='Use parametric coords')
dot.edge('A', 'C', label='OR differentiate')
dot.edge('B', 'D', label='Compute tangent slope')
dot.edge('C', 'D', label='→ Slope of tangent')
dot.edge('D', 'E', label='Form equation for tangent')
dot.edge('E', 'F', label='Find perpendicular line')
dot.edge('F', 'G')

# Render the diagram as PNG.
dot.render('detailed_concept_04_2', format='png', view=True)