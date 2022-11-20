import networkx as nx
import csv
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def verify_connectivity(v, Graph1, themes, Graph2, lines_number):
    i = 0
    associates = []
    for u in Graph1.nodes():
        if (Graph1.has_edge(v, u) == True) and (verify_theme_impression(u, themes) == False):
            i = i + 1
            associates.append(u)
    if i > 0:
        print(f'\nOpções associadas a {theme}')
        for j in range(len(associates)):
            print(associates[j])
    if len(lines_number) > 0:
        verify_relationship(theme, Graph2, themes)
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

def verify_relationship(theme, Graph2, themes):
    i = 0
    associates = []
    for u in Graph2.nodes():
        if (Graph2.has_edge(v, u) == True) and (verify_theme_impression(u, themes) == False):
            i = i + 1
            associates.append(u)
    if i > 0:
        print(f'\nSugestão: De acordo com escolhas de usuários anteriores, o tema {theme} foi selecionado em conjunto com os seguintes temas:')
        for j in range(len(associates)):
            print(associates[j])

Graph1 = nx.read_adjlist('files/adjacency_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)
Graph2 = nx.read_adjlist('files/historic_adj_list.txt', delimiter=";", create_using=nx.Graph(), nodetype=str)

arq = open("files/historic_adj_list.txt")
lines_number = arq.readlines()

print('\nOpções de estudo: ')
print(Graph1.nodes())

themes = []
i = 0

while i < 5:
    theme = input('\nEscolha, entre os temas acima, o que deseja estudar: ')
    if verify_correct_theme(theme, Graph1) == False:
        print(f'\nO tema "{theme}" não está presente na lista acima!')
        continue
    else:
        if i > 0:
            if verify_correct_connectivity(themes, theme, Graph1) == False:
                print(f'\nO tema "{theme}" não está presente na lista acima!')
                continue
            if verify_theme_impression(theme, themes) == True:
                print(f'\nO tema {theme} já foi escolhido anteriormente!')
            else: 
                themes.append(theme)
                if i > 0:
                    Graph2.add_edge(themes[i-1], themes[i])
                for v in Graph1.nodes():
                    if v == theme:
                        if i < 4:
                            if verify_connectivity(v, Graph1, themes, Graph2, lines_number) == 0:
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
                Graph2.add_edge(themes[i-1], themes[i])
            for v in Graph1.nodes():
                if v == theme:
                    if i < 4:
                        if verify_connectivity(v, Graph1, themes, Graph2, lines_number) == 0:
                            print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                            print(themes)
                            i = 5
                    else:
                        print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                        print(themes)
            i = i + 1

nx.write_adjlist(Graph2, 'files/historic_adj_list.txt', delimiter=";")

arq.close()
