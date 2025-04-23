from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Flowchart for Sections 0.4.1, 0.4.2, 0.4.3')

# Optionally, set the layout direction (LR: left-to-right)
dot.attr(rankdir='LR')

# Define nodes with descriptive labels
dot.node('A', '0.4.1: Intersection of a Line\nwith an Ellipse\n(Substitute line Eq into ellipse Eq and solve quadratic)')
dot.node('B', '0.4.2: Tangent and Normal\nat a Point on the Ellipse\n(Compute derivative for tangent; normal is perpendicular)')
dot.node('C', '0.4.3: Condition for Tangency\n(Discriminant = 0, so c² = a²·m² + b²)')

# Connect the nodes (flow order)
dot.edge('A', 'B', label='Next: Find tangent & normal')
dot.edge('B', 'C', label='Then enforce tangency')

# Render the graph to a PNG file and open it
# This creates 'flowchart_04.png' in your working directory.
dot.render('flowchart_04', format='png', view=True)
