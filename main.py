import networkx as nx
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def verify_connectivity(v, G):
    for u in G.nodes():
        if G.has_edge(v, u) == True:
            print(u)


G = nx.read_adjlist('files/adjacency_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)

print('\nOpções de estudo: ')
print(G.nodes())

themes = []
i = 0

for i in range(0,4):
    
    theme = input('\nEscolha, entre os temas acima, o que deseja estudar: ')
    #rodar a lista themes verificar se o nome inserido acima tem lá, se já tiver já foi inserido 
    themes.append(theme)
    if i > 0:
        G[themes[i-1]][themes[i]]['peso'] = 1 #criar uma struct que se tiver os dois nomes da arestas o valor que tem lá dentro vai ser incremetado
        print(G['IOT']['Arduino']['peso'])
    print(themes)
    print(f'\nOpções associadas a {theme}')
    for v in G.nodes():
        if v == theme:
            verify_connectivity(v, G)

nx.draw(G, with_labels=True, font_color='black', node_color='red', node_size=1200)
plt.show()