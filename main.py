import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

G = nx.read_adjlist('files/adjacency_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)

print('Opções de estudo: ')
print(G.nodes())
input()

option = 'Sim'

while option == 'Sim' or option == 'sim':
    theme = input('Informe o tema que deseja introduzir seu estudo: ')
    for v in G.nodes():
        if v == theme:
            print(v)

nx.draw(G, with_labels=True, font_color='black', node_color='red', node_size=1200)
plt.show()