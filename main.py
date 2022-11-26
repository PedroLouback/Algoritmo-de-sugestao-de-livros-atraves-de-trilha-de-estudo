import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import nltk
import csv
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import wordcloud
import string
nltk.download('punkt')
cont=0



def main():
    Graph1 = nx.read_adjlist('files/adjacency_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)
    Graph2 = nx.read_edgelist('files/historic_adj_list.csv', delimiter=";", create_using=nx.Graph(), nodetype=str)

    arq = open("files/historic_adj_list.csv")
    lines_number = arq.readlines()
    j=0
    print('\nOpções de estudo:', ', '.join(Graph1.nodes()).replace("'", ""))
    Books=[]
    themes = []
    i = 0
    check_associates = []
    associates = []

    while i < 5:
        theme = input('\nEscolha, entre os temas acima, o que deseja estudar:')
        if len(associates) > 0:
            check_associates.append(verify_vertical_study(theme, associates))
        associates.clear()
        if verify_correct_theme(theme, Graph1) == False:
            print(f'\nO tema "{theme}" não está presente na lista acima!')
            continue
        else:
            verify_book(theme,cont,Books)
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
                                    if len(check_associates) > 0:
                                        if verify_impression_vertical_study(check_associates) == True:
                                            print('\nDe acordo com as escolhas do usuário e execuções anteriores foi observado que usuário realizou um estudo verticalizado, seguindo sugestões realizadas pelo programa!')
                                        else:
                                            print('\nDe acordo com as escolhas do usuário e execuções anteriores foi observado que usuário realizou um estudo horizontal, não seguindo as sugestões realizadas pelo programa!')
                                    print('\nCom base nas suas escolhas foram encontrados os seguintes livros:')
                                    verify_book(theme,cont,Books)
                                    print(Books)
                                    print(', '.join(themes).replace("'", ""))
                                    i = 5
                                if store_value_function > 1 and len(lines_number) > 0:
                                    associates = verify_relationship(theme, Graph2, themes)
                            else:
                                if len(check_associates) > 0:
                                    if verify_impression_vertical_study(check_associates) == True:
                                        print('\nDe acordo com as escolhas do usuário e execuções anteriores foi observado que usuário realizou um estudo verticalizado, seguindo sugestões realizadas pelo programa!')
                                    else:
                                        print('\nDe acordo com as escolhas do usuário e execuções anteriores foi observado que usuário realizou um estudo horizontal, não seguindo as sugestões realizadas pelo programa!')
                                print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                                print(', '.join(themes).replace("'", ""))
                    i = i + 1
            else:
                themes.append(theme)
                for v in Graph1.nodes():
                    if v == theme:
                        store_value_function = verify_connectivity(v, Graph1, themes)
                        if store_value_function == 0:
                            if len(check_associates) > 0:
                                if verify_impression_vertical_study(check_associates) == True:
                                    print('\nDe acordo com as escolhas do usuário e execuções anteriores foi observado que usuário realizou um estudo verticalizado, seguindo sugestões realizadas pelo programa!')
                                else:
                                    print('\nDe acordo com as escolhas do usuário e execuções anteriores foi observado que usuário realizou um estudo horizontal, não seguindo as sugestões realizadas pelo programa!')
                            print('\nCom base nas suas escolhas foram encontrados os seguintes livros: ')
                            print(', '.join(themes).replace("'", ""))
                            i = 5
                        if store_value_function > 1 and len(lines_number) > 0:
                            associates = verify_relationship(theme, Graph2, themes)
                i = i + 1
    # print('Os livros selecionados foram:\n')
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
    i = 0
    associates = []
    for u in Graph2.nodes():
        if (Graph2.has_edge(theme, u) == True) and (verify_theme_impression(u, themes) == False):
            i = i + 1
            associates.append(u)
    if i > 0:
        print(f'\nSUGESTÃO: De acordo com escolhas de usuários anteriores, o tema {theme} foi selecionado em conjunto com o(s) seguinte(s) tema(s): ')
        for j in range(len(associates)):
            print(associates[j])
    return associates

def verify_vertical_study(theme, associates):
    for i in range(len(associates)):
        if theme != associates[i]:
            check_value = 1
        else:
            check_value = 2
            return check_value
    return check_value

def verify_impression_vertical_study(check_associates):
    for i in range(len(check_associates)):
        if check_associates[i] == 1:
            continue
        else:
            return True
    return False

def verify_book(theme,cont,Books):
    Narq = 1
    linha = 0
    linha_max = 3274
    new_arq = 'final_data.csv'
    data = pd.read_csv(new_arq)
    newdata_s = data['FinalStar']
    newdata_t = data['RatingDistTotal']
    newdata_n = data['Name']
    livro_1 = 0
    livro_2 = 0
    livro_3 = 0
    livro_4 = 0
    livro_5 = 0
    text_4 = ''
    text_1 = ''
    text_2 = ''
    text_3 = ''
    text_5 = ''
    Userstudy = theme
    Nstudy = Userstudy.lower()
    if Nstudy == 'javascrip':
        book_name = 'javascript'
        second_name = 'javascript'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 'rust':
        book_name = 'rust'
        second_name = 'rust'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 'python':
        book_name = 'python'
        second_name = 'python'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 'c#':
        book_name = 'c#'
        second_name = 'c#'
        define_1 = 'programming'
        define_3 = 'developer'
    if Nstudy == 'c++':
        book_name = 'c++'
        second_name = 'c++'
        define_1 = 'c++'
    if Nstudy == 'java':
        book_name = 'java'
        second_name = 'java'
        define_1 = 'programming'
        define_3 = 'developer'
    if Nstudy == 'react':
        book_name = 'react'
        second_name = 'react'
        define_1 = 'programming'
        define_3 = 'developer'
    if Nstudy == 'react':
        book_name = 'react'
        second_name = 'native'
        define_1 = 'programming'
        define_3 = 'developer'
    if Nstudy == 8:
        book_name = 'arduino'
        second_name = 'arduino'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 's.embarcados':
        book_name = 'embedded'
        second_name = 'systems'
    if Nstudy == 'i.a':
        book_name = 'artificial'
        second_name = 'intelligence'
        define_1='artificial'
    if Nstudy == 'analise de dados':
        book_name = 'data'
        second_name = 'analysis'
        define_1 = 'data'
    if Nstudy == 'raspberry':
        book_name = 'raspberry'
        second_name = 'raspberry'
        define_1='hardware'
        define_2='embedded'
    if Nstudy == 'mineração de dados':
        book_name = 'data'
        second_name = 'mining'
        define_1='data'
    if Nstudy == 'programming':
        book_name = 'programming'
        second_name = 'logic'
        define_1='programming'
    if Nstudy == 'html/css':
        book_name = 'html'
        second_name = 'html'
        define_1='html'
    if Nstudy == 'mobile':
        book_name = 'mobile'
        second_name = 'mobile'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 'ios':
        book_name = 'ios'
        second_name = 'ios'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 'android':
        book_name = 'android'
        second_name = 'android'
        define_1 = 'programming'
        define_3 = 'developer'
    if Nstudy == 'estrututra de dados':
        book_name = 'data'
        second_name = 'structure'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 'redes':
        book_name = 'nets'
        second_name = 'nets'
        define_1 = 'programming'
        define_3 = 'developer'
    if Nstudy == 'banco de dados':
        book_name = 'database'
        second_name = 'database'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 'sql':
        book_name = 'sql'
        second_name = 'sql'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 'poo':
        book_name = 'object-oriented'
        second_name = 'programming'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    if Nstudy == 's.o':
        book_name = 'operating'
        second_name = 'system'
        define_1 = 'programming'
        define_2 = 'data'
        define_3 = 'developer'
        define_4 = 'Development'
    while linha <= linha_max:
        new_arq = newdata_n.iloc[linha].lower()
        # text_sp = ''.join([p for p in new_arq if p not in string.punctuation])
        text_tokenize = nltk.word_tokenize(new_arq)
        conteis = text_tokenize.__contains__(book_name)
        conteis_1 = text_tokenize.__contains__(second_name)
        define = text_tokenize.__contains__(define_1 or define_2 or define_3 or define_4)
        if conteis & conteis_1 & define:
            print(new_arq)
            text_alt = newdata_t.iloc[linha]
            hating_t = int(text_alt)
            text_alt = newdata_s.iloc[linha]
            hating_s = int(text_alt)
            hating_s = hating_s*hating_s
            pointfinal = hating_s*hating_t
            livro = pointfinal
            if livro > livro_5:
                livro_5 = livro
                text_5 = '"'+newdata_n.iloc[linha]+'"'+ '\n'
                if livro > livro_4:
                    livro_5 = livro_4
                    livro_4 = livro
                    text_5 = text_4
                    text_4 = '"'+newdata_n.iloc[linha]+'"' +'\n'
                    if livro > livro_3: 
                        livro_4 = livro_3
                        livro_3 = livro
                        text_4 = text_3
                        text_3 = '"'+newdata_n.iloc[linha]+'"'+ '\n'
                        if livro > livro_2: 
                            livro_3 = livro_2
                            livro_2 = livro
                            text_3 = text_2
                            text_2 = '"'+newdata_n.iloc[linha]+'"'+'\n'
                            if livro > livro_1:
                                livro_2 = livro_1
                                livro_1 = livro
                                text_2 = text_1
                                text_1 = '"'+newdata_n.iloc[linha]+'"'+'\n'
        linha += 1

    print("Os 5 melhores livros para sua linha de estudo são:\n")
    print('Selecione um dos livros abaixo:\n')
    print('Digite 1 para:', text_1,'\n')
    print('Digite 2 para:', text_2,'\n')
    print('Digite 3 para:', text_3,'\n')
    print('Digite 4 para:', text_4,'\n')
    print('Digite 5 para:', text_5,'\n')
    book = input('\nDigite o livro desejado.')
    if book == 1:
        Books.append(text_1) 
    if book == 2:
        Books.append(text_2)
    if book == 3:
        Books.append(text_3)
    if book == 4:
        Books.append(text_4)
    if book == 5:
        Books.append(text_5)
    if cont == 4:
        print(Books)
    cont+=1


if __name__ == "__main__":
    main()