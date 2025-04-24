from graphviz import Digraph

# Create a concept map for Section 0.5 "Director Circle"
dot = Digraph(comment='Concept Map for 0.5 Director Circle')
dot.attr(rankdir='TB', size='8,5')

# Node: Ellipse Equation and Properties
dot.node('A', 'Ellipse Equation:\n x²/a² + y²/b² = 1', shape='rectangle', color='blue')
dot.node('B', 'Center & Axes:\n Center = (0,0)\n Semi-axes: a (major), b (minor)', shape='rectangle', color='green')
dot.node('C', 'Tangent Properties:\n Tangents can be perpendicular', shape='rectangle', color='orange')
dot.node('D', 'Director Circle:\n Locus of intersections\n of perpendicular tangents', shape='rectangle', color='purple')
dot.node('E', 'Director Circle Equation:\n x² + y² = a² + b²', shape='rectangle', color='red')
dot.node('F', 'Interpretation:\n Center = (0,0)\n Radius = √(a² + b²)', shape='rectangle', color='brown')

# Logical flow edges
dot.edge('A', 'B', label='defines')
dot.edge('B', 'C', label='grants geometric insight')
dot.edge('C', 'D', label='leads to')
dot.edge('D', 'E', label='via algebra')
dot.edge('E', 'F', label='implies')
dot.edge('B', 'F', label='Combine with center')

# Render the concept map into a PNG file and open it.
dot.render('concept_map_director_circle', view=True, format='png')