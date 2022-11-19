import networkx as nx
import csv
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def verify_connectivity(v, G, themes, weights):
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
    if len(weights) > 0:
        verify_relationship(theme, weights, themes)
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
    with open('files/weights.txt','r') as f: 
        for line in f:
            (v1, v2) = line.split(';')
            group[v1] = v2.replace('\n', '')
    return group

def verify_relationship(theme, weights, themes):
    count1 = 0
    count2 = 0
    for i in weights:
        if theme == i:
            relationship1 = weights.get(i)
            count1 = count1 + 1
    for key, value in weights.items():
        if theme == value:
            relationship2 = key
            count2 = count2 + 1
    if count1 > 0 and (verify_theme_impression(relationship1, themes) == False):
        print(f'\nSugestão: De acordo com escolhas de usuários anteriores, o tema {theme} já foi relacionado com {relationship1}')
    elif count2 > 0 and (verify_theme_impression(relationship2, themes) == False):
        print(f'\nSugestão: De acordo com escolhas de usuários anteriores, o tema {theme} já foi relacionado com {relationship2}')
    elif count1 > 0 and count2 > 0 and (verify_theme_impression(relationship1, themes) == False) and (verify_theme_impression(relationship2, themes) == False):
        print(f'\nSugestão: De acordo com escolhas de usuários anteriores, o tema {theme} já foi relacionado com {relationship1} e {relationship2}')


G = nx.read_adjlist('files/adjacency_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)

arq = open("files/weights.txt", "a")
print('\nOpções de estudo: ')
print(G.nodes())

themes = []
i = 0

weights = read_weight()

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
                    arq.write(themes[i-1]+';'+themes[i])
                    arq.write('\n')
                for v in G.nodes():
                    if v == theme:
                        if i < 4:
                            if verify_connectivity(v, G, themes, weights) == 0:
                                print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                                print(themes)
                                i = 5
                        else:
                            print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                            print(themes)
                i = i + 1
        else:
            themes.append(theme)
            if i > 0:
                G[themes[i-1]][themes[i]]['peso'] = random.randrange(0,10)
                arq.write(themes[i-1]+';'+themes[i] )
                arq.write('\n')
            for v in G.nodes():
                if v == theme:
                    if i < 4:
                        if verify_connectivity(v, G, themes, weights) == 0:
                            print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                            print(themes)
                            i = 5
                    else:
                        print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                        print(themes)
            i = i + 1

arq.close()
# nx.draw(G, with_labels=True, font_color='black', node_color='red', node_size=1200)
# plt.show()
