import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

G = nx.read_adjlist('files/adjacency_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)

nx.draw(G, with_labels=True, font_color='black', edgecolors='red', node_color='lightgray', node_size=1000)
plt.show()