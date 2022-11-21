import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

def main():
    Graph1 = nx.read_adjlist('files/adjacency_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)
    Graph2 = nx.read_edgelist('files/historic_adj_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)

    arq = open("files/historic_adj_list.csv")
    lines_number = arq.readlines()

    print('\nOpções de estudo:', ', '.join(Graph1.nodes()).replace("'", ""))

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
                    Graph2.add_edge(themes[i-1], themes[i])
                    for v in Graph1.nodes():
                        if v == theme:
                            if i < 4:
                                store_value_function = verify_connectivity(v, Graph1, themes)
                                if store_value_function == 0:
                                    print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                                    print(', '.join(themes).replace("'", ""))
                                    i = 5
                                if store_value_function > 1 and len(lines_number) > 0:
                                    store_value_function2 = verify_relationship(theme, Graph2, themes)
                            else:
                                print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                                print(', '.join(themes).replace("'", ""))
                    i = i + 1
            else:
                themes.append(theme)
                for v in Graph1.nodes():
                    if v == theme:
                        store_value_function = verify_connectivity(v, Graph1, themes)
                        if store_value_function == 0:
                            print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                            print(', '.join(themes).replace("'", ""))
                            i = 5
                        if store_value_function > 1 and len(lines_number) > 0:
                            store_value_function2 = verify_relationship(theme, Graph2, themes)
                i = i + 1
    
    if store_value_function2 > 0:
        print('\nDe acordo com as escolhas do usuário e execuções anteriores foi observado que usuário realizou um estudo verticalizado, seguindo sugestões realizadas pelo programa!')
    elif store_value_function2 == 0:
        print('\nDe acordo com as escolhas do usuário e execuções anteriores foi observado que usuário não realizou um estudo verticalizado!')
    

    nx.write_edgelist(Graph2, 'files/historic_adj_list.csv', delimiter=";", data=False, encoding='utf-8')

    arq.close()

def verify_connectivity(theme, Graph1, themes):
    i = 0
    associates = []
    for u in Graph1.nodes():
        if (Graph1.has_edge(theme, u) == True) and (verify_theme_impression(u, themes) == False):
            i = i + 1
            associates.append(u)
    if i > 0:
        print(f'\nOpções associadas a {theme}:')
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
    
def verify_relationship(theme, Graph2, themes):
    count_associates = 0
    i = 0
    associates = []
    for u in Graph2.nodes():
        if (Graph2.has_edge(theme, u) == True) and (verify_theme_impression(u, themes) == False):
            i = i + 1
            associates.append(u)
    if i > 0:
        count_associates = count_associates + 2
        print(f'\nSUGESTÃO: De acordo com escolhas de usuários anteriores, o tema {theme} foi selecionado em conjunto com o(s) seguinte(s) tema(s): ')
        for j in range(len(associates)):
            print(associates[j])
    return count_associates

if __name__ == "__main__":
    main()