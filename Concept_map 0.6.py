from graphviz import Digraph

# Create a concept map for 0.6 Geometrical Properties of an Ellipse (Part 1)
dot = Digraph(comment='Concept Map for 0.6 Geometrical Properties (Part 1)')
dot.attr(rankdir='TB', size='8,6')

# Node: Ellipse Geometry
dot.node('A', 'Ellipse & Its Geometry\nEquation: x²/a² + y²/b² = 1\nCenter: C, Semi–axes: a (major), b (minor)', shape='rectangle', color='blue')

# Node: Point on Ellipse
dot.node('B', 'Choose a Point P\non the Ellipse', shape='rectangle', color='green')

# Node: Tangent at P
dot.node('C', 'Tangent at P\n• Meets major axis at T\n• Meets minor axis at t', shape='rectangle', color='orange')

# Node: Perpendiculars from P
dot.node('D', 'Perpendiculars from P\nto the Axes\n• Foot on major axis: N\n• Foot on minor axis: M', shape='rectangle', color='purple')

# Node: Geometrical Properties
dot.node('E', 'Geometrical Properties:\n• CN · CT = a²\n• CM · Ct = b²\n[Sub-tangent relation]', shape='rectangle', color='red')

# Node: Interpretation & Insight
dot.node('F', 'Interpretation:\nTangent & perpendicular lengths\nreflect ellipse dimensions', shape='rectangle', color='brown')

# Logical flow edges
dot.edge('A', 'B', label='defines')
dot.edge('B', 'C', label='draw tangent')
dot.edge('B', 'D', label='drop perpendiculars')
dot.edge('C', 'E', label='Intersection\nyields lengths')
dot.edge('D', 'E', label='Provide measures')
dot.edge('E', 'F', label='→ Insight')
dot.edge('A', 'F', label='Based on ellipse geometry')

# Render the concept map to a PNG file and open it (this creates a file "concept_map_geometrical_properties1.png")
dot.render('concept_map_geometrical_properties1', view=True, format='png')