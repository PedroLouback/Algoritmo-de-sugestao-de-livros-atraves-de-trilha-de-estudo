import networkx as nx
import csv
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def verify_connectivity(v, G, themes):
    i = 0
    associates = []
    for u in G.nodes():
        if (G.has_edge(v, u) == True) and (verify_theme_impression(u, themes) == False):
            i = i + 1
            associates.append(u)
    if i > 0:
        print(f'\nOpções associadas a {theme}')
        for j in range(len(associates)):
            print(associates[j])
    return i

def verify_theme_impression(u, themes):
    for i in range(len(themes)):
        if u != themes[i]:
            continue
        else:
            return True 
    return False

def verify_correct_theme(theme, G):
    for v in G.nodes():
        if theme != v:
            continue           
        else:
            return True
    return False

def verify_correct_connectivity(themes, theme, G):
    for u in G.nodes():
        if (G.has_edge(theme, themes[-1]) == False):
            continue
        else:
            return True
    return False
    
def read_weight():
    group = {}
    with open('files/weights.txt','r') as file:
        f = csv.DictReader(file,delimiter=';')
        for i in f:
            group = i
    print(group)


G = nx.read_adjlist('files/adjacency_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)

arq = open("files/weights.txt", "a")

print('\nOpções de estudo: ')
print(G.nodes())

themes = []
i = 0

while i < 5:
    theme = input('\nEscolha, entre os temas acima, o que deseja estudar: ')
    if verify_correct_theme(theme, G) == False:
        print(f'\nO tema "{theme}" não está presente na lista acima!')
        continue
    else:
        if i > 0:
            if verify_correct_connectivity(themes, theme, G) == False:
                print(f'\nO tema "{theme}" não está presente na lista acima!')
                continue
            if verify_theme_impression(theme, themes) == True:
                print(f'\nO tema {theme} já foi escolhido anteriormente!')
            else: 
                themes.append(theme)
                if i > 0:
                    G[themes[i-1]][themes[i]]['peso'] = random.randrange(0,10)
                    arq.write('\n'+themes[i-1]+';'+themes[i]+';'+'%d' % G[themes[i-1]][themes[i]]['peso'])
                print(themes)
                for v in G.nodes():
                    if v == theme:
                        if i < 4:
                            if verify_connectivity(v, G, themes) == 0:
                                print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                                read_weight()
                                i = 5
                        else:
                            print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                i = i + 1
        else:
            themes.append(theme)
            if i > 0:
                G[themes[i-1]][themes[i]]['peso'] = random.randrange(0,10)
                arq.write('\n'+themes[i-1]+';'+themes[i]+';'+'%d' % G[themes[i-1]][themes[i]]['peso'])
                read_weight()
            for v in G.nodes():
                if v == theme:
                    if i < 4:
                        if verify_connectivity(v, G, themes) == 0:
                            print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                            read_weight()
                            i = 5
                    else:
                        print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                        read_weight()
            i = i + 1

arq.close()
nx.draw(G, with_labels=True, font_color='black', node_color='red', node_size=1200)
plt.show()
