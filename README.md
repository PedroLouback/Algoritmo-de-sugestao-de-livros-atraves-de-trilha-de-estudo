# Algoritmo de sugestão de livros de estudos baseado em escolhas de temas relacionados a tecnologia
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## Conteúdos

<p align="center">
    <a href="#apresentação">Apresentação</a> •
    <a href="#introdução">Introdução</a> • 
    <a href="#estrutura-e-sua-implementação">Estrutura e sua implementação</a> •
    <a href="#conclusão">Conclusão</a> •
    <a href="#bibliotecas">Bibliotecas</a> •
    <a href="#execução-do-projeto">Execução do projeto</a> •
    <a href="#referências">Referências</a> •
    <a href="#autor">Autor</a>

</p>

---

## Apresentação

Foi proposto pelo professor [Michel Pires da Silva](http://lattes.cnpq.br/1449902596670082) da matéria de `Arquitetura e Estruturas de Dados 2 do 4º Período do curso de Engenharia de Computação` um trabalho relacionado ao conteúdo passado em suas aulas teóricas que são `Estruturas de dados Grafos`, onde tinha o propósito de implementar alguma apicação que envolvia estruturas de representação e caminhamento em grafos, a partir disso foi designado a seguinte proposta para desenvolvimento em dupla de alunos:

*Neste trabalho o objetivo é aplicar as estruturas em grafos para solucionar um problema real qualquer. Cada dupla de alunos deve escolher em literatura uma das áreas de aplicação do tema e propor uma solução baseada nos conceitos apresentados. Essa solução pode ser realizada utilizando C, C++ e/ou Python. O objetivo e mostrar a atuação de algoritmos clássicos em grafos na resolução de problemas emergentes. Alguns temas para inspiração são: Análise de rede social, rotas de entregas, análise de trafego (i.e., carros, pacotes na internet, etc), mínima quantidade de saltos em redes, teoria dos jogos, elaboração de horário vs rodízio de salas, envoltória convexa (do inglês, convex hull), etc.*

*LAB AEDS: Espera-se que os trabalhos estejam muito bem organizados em termos de estruturação de código. O código deve estar devidamente documentado. Para tanto, é obrigatório a utilização de diretrizes de comentários que possibilitem a geração automática de documentação.*

*AEDS: O problema abordado deve ser explicado em detalhes, considerando todo referencial teórico sobre o tema abordado. Por exemplo, se o tema for caminho mínimo, é esperado que os autores explorem a área relatando os algoritmos clássicos existentes para tal problema, bem como, todo embasamento teórico matemático que detalha o contexto de atuação / solução. Esse documento deve ser entregue em formato README ou Wiki, ambos como parte do git do projeto.*

*Observação:  Como o tema grafos é imenso, cada dupla deve escolher um tema exclusivo, o qual não poderá ser abordado por outra equipe através da mesma solução. Por exemplo, se a dupla optar por calcular o caminho mínimo de cada vértice para todos os outros utilizando o algoritmo de floyd-warshall para um problema real qualquer, outras equipes não poderão adotar o mesmo algoritmo no mesmo problema. Contudo, o problema pode ser abordado por outras equipes adotando-se para isso outros algoritmos. Além disso, fica liberado para todas as equipes a utilização de conceitos de heurística, meta-heurística, computação evolutiva, etc. Por fim, caso haja mais de uma equipe atuando sob o mesmo problema, porém com soluções distintas, se essas elaborarem um git a parte com todas as soluções e um comparativo entre elas, discutindo profundamente ganhos, perdas e motivos pelos quais os ganhos no algoritmo X são obtidos, essas equipes ficam liberadas de realizar a metade da prova final. Lembrem-se, para esse ponto final de comparação, caso a linguagem utilizada não seja exatamente a mesma, a discussão de ganho vs performance deve considerar as peculiaridades da linguagem, para assim, tornar a comparação justa. Logo, é sugerido que para fins de justiça todos os algoritmos sejam executados na mesma plataforma computacional. Para agilizar o trabalho sem precisar centralizar o trabalho em um mesmo computador, considerem utilizar o Google Colab durante o desenvolvimento ou outra ferramenta que execute on-line. Assim, teremos o tempo justo extraído ao final.*

Dada a proposta, foi pensado no desenvolvimento de um algoritmo que buscava sugerir livros para auxiliar no estudo de usuários, sendo essa sugestão baseada em escolhas feitas durante a execução do programa com os temas relacionados a partir de um grafo, obtendo êxito no desenvolvimento baseado nos detalhes presentes nos tópicos abaixo:

---

## Introdução

Para introduzir o problema proposto primeiramente foi necessário a criação dos cinco diferentes arquivos sendo quatro deles contendo os diferentes tamanhos de entrada do tipo _float_ e um contendo 10.000 entradas do tipo _float_ utilizado para consultas, sendo possível encontra-los na pasta *__src/files__* para verificação. A criação dos arquivos foi necessária apenas uma vez para manter o padrão de testes, após isso foi removido as funções de criações.

Após a criação dos arquivos foi necessário a implementação dos diferentes tipos de `Estrutura de Dados Árvore` onde foram utilizadas através de repositórios feitos pelo professor [Michel Pires da Silva](http://lattes.cnpq.br/1449902596670082), sendo eles, [Árvore Binária de Pesquisa](https://github.com/mpiress/basic_tree), [Árvore AVL](https://github.com/mpiress/avl_tree) e [Árvore RedBlack](https://github.com/mpiress/RedBlack) onde na última estrutura foi necessária a implementação do método de _remoção_ onde foi encontrado o mesmo no livro do [1]Cormem em forma de pseudocódigo, sendo feita apenas algumas alterações no código principal para que fosse possível ser feita a implementação da _remoção_ sem nenhum problema. Sendo feita essas implementações foi necessário implementar a utilização de __*vectors*__ e estruturas do tipo __*MAPs*__ encontrando informações em [2] para uma implementação sem erros;

## Estrutura e sua implementação

### • Grafo

__*<u>O que é uma Árvore Binária de Pesquisa?</u>*__

Uma Árvore Binária de Pesquisa é organizada, como o nome sugere, em uma árvore binária como mostra a _Figura 1_. Sendo uma estrutura baseada em nós, onde todos os nós da subárvore esquerda possuem um valor númerico interior ao nó raiz e todos os nós da subárvore direita possuem um valor superior ao nó raiz, sendo essa a forma padrão. Essa estrutura possue o objetivo de estruturar os dados de forma a permitir <a href="#busca-binária">Busca Binária</a>.
Esse tipo de estrutura suporta muitas operações de conjuntos dinâmicos, incluindo _<a href="#operação-de-busca">busca</a>, mínimo, máximo, antecessor, sucessor, <a href="#operação-de-inserção">inserção</a> e <a href="#operação-de-remoção">remoção</a>_, possibilitando seu uso como um dicionário e também como uma fila de prioridades. 

<p align="center">
<img src="imgs/abp.png" width="600px"/>
</p>
<p align="center">
<i>Figura 1: Árvores Binárias de Pesquisa. (<b>a</b>)Uma árvore binária de pesquisa com seis nós e altura 2. (<b>b</b>)Uma árvore de busca binária menos eficiente, com altura 4, contendo as mesmas chaves de (<b>a</b>).</i>
</p>

__*<u>Custos de uma Árvore Binária de Pesquisa?</u>*__

As operações básicas em um árvore binária de pesquisa demoram um tempo proporcional á altura da árvore. No caso de uma árvore binária completa com _n_ nós, tais operações são executados no tempo $O(log{}{n})$ do pior caso. Porém, se a árvore é uma cadeia linear de _n_ nós, as mesmas operações demoram o tempo $O(n)$ do pior caso. Segue uma tabela composta pela complexidade de tempo em __Notação big O__ dos algoritmos básicos que compõem a `Árvore Binária de Pesquisa`:

| Algoritmo         |  Caso Médio        | Pior Caso       |         
| ------------------| ------------------ | --------------- |
|  `Espaço`         | $O(n)$             | $O(n)$          |
|  `Busca`          | $O(log{n})$        | $O(n)$          |
|  `Inserção`       | $O(log{n})$        | $O(n)$          |
|  `Remoção`        | $O(log{n})$        | $O(n)$            

<i>Tabela 1: Complexidade de uma Árvore Binária de Pesquisa em notação big O.</i>

* Logo a árvore binária de busca é de pouca utilidade para ser aplicada em problemas de busca em geral, surgindo então o interesse em árvores balanceadas, cuja altura seja $O(log{}{n})$ no pior caso.

__*<u>Operação de Busca</u>*__

A operação de busca por um valor específico implementada no algoritmo através de uma função recursiva como é possível visualizar no pseudocódigo abaixo que foi usado como base para implementação:

```c
TreeSearch(x,k)
1 if x == NULL ou k == x.chave
2   return x
3 if k < x.chave
4   return TreeSearch(x.esquerda, k)
5 else return TreeSearch(x.direita, k)
```
<i>Explicação:</i> A busca começa examinando o nó raiz. Se a árvore está vazia, o valor procurado não pode existir na árvore. Caso contrário, se o valor é igual a raiz a busca foi bem sucedida. Se o valor é menor do que a raiz, a busca segue pela subárvore esquerda. Igualmente caso o valor é maior do que a raiz, a busca segue pela subárvore direita. Se tornando um processo recursivo até encontrar o valor requerido. Se o valor na for encontrado até a busca chegar na subárvore nula é concluido que o valor não está presente na árvore

__*<u>Operação de Inserção</u>*__

A operação de inserção é utilizado o procedimento presente na função ___insertTree()__ onde o mesmo toma um nó _z_ para o qual _z.chave = v_, _z.esquerda=NULL_ e _z.direita=NULL_, e modifica _T_ e alguns dos atributos de _z_ de modo tal que insere _z_ em uma posição adequada na árvore, sendo possível visualizar no pseudocódigo abaixo:

```c
insertTree(T,z)
1 y = NULL
2 x = T.raiz
3 while x != NULL
4   y = x
5   if z.chave < x.chave
6       x = x.esquerda
7   else x = x.direita
8 z.p = y
9 if y = NULL
10  T.raiz = z    //a árvore T era vazia
11 else if z.chave < y.chave
12  y.esquerda = z
13 else y.direita = z
```
<i>Explicação:</i> A fim de introduzir um nó novo na árvore, seu valor é primeiro comparado com o valor da raiz. Se seu valor for menor que a raiz, é comparado então com o valor do filho da esquerda da raiz. Se seu valor for maior, está comparado com o filho da direita da raiz. Este processo continua até que o nó novo esteja comparado com um nó da folha, e então adiciona-se o filho da direita ou esquerda, dependendo de seu valor. Segue abaixo na <i>Figura 2</i> um exemplo de inserção na Árvore Binária de Pesquisa:

<p align="center">
<img src="imgs/insertionTreeABP.png" width="400px"/>
</p>
<p align="center">
<i>Figura 2: Exemplo de uma inserção do valor 13 em uma árvore binária de pesquisa. Os nós sombreados emtommais claro indicamo
caminho simples da raiz até a posição emque o item é inserido. A linha tracejada indica a ligação que é acrescentada à árvore para inserir o item.</i>
</p>

__*<u>Operação de Remoção</u>*__

A exclusão de um nó na árvore binária de pesquisa é um processo mais complexo. Para excluir um nó de uma árvore binária de pesquisa, levando em consideração três casos distintos para a exclusão, sendo eles:

**Caso 1 - Remoção na folha:** A exclusão na folha é a mais simples, batando apenas removê-lo da árvore como no exemplo da figura abaixo:
<p align="left">
<img src="imgs/remove1.jpg" width="350px"/>
</p>
<i>Figura 3: Remoção do valor 40 presente em uma folha.</i>
<br><br>

**Caso 2 - Remoção de nó com um filho:** Ao excluir um nó que possui um filho, o filho vai subir para a posição do pai.
<p align="left">
<img src="imgs/remove2.jpg" width="500px"/>
</p>
<i>Figura 4: Remoção do valor 90 presente em um nó com um filho.</i>
<br><br>

**Caso 3 - Remoção de nó com dois filhos:** Neste caso, há duas opções para ser operado. A primeira é a possibilidade de substituir o valor do nó a ser retirado pelo valor sucessor (o nó mais á esquerda da subárvore direita) ou pelo valor antecessor (o nó mais á direita da subárvore esquerda), sendo feita então a remoção do nó sucessor ou antecessor.
<p align="left">
<img src="imgs/remove3.jpg" width="450px"/>
</p>
<i>Figura 5: Remoção do valor 30 presente em um nó com dois filho.</i>

A função __antecessor__ foi utilizada para que houvesse uma implementação sem erros onde a mesma é composta por:

```c
antecessor(T,x)
1 if x.direita != NULL
2 return antecessor(x.direita)
3 x = T
4 T = T.esquerda
5 free x
```

```c
RemoveTree(T,x)
1 y = T.raiz
2 if y == NULL
3   return
4 if x.chave < y.chave
5     RemoveTree(y.esquerda, x)
6 if x.chave > y.chave
7     RemoveTree(y.direita, x)
8 if y.direita == NULL{
9     aux = y
10     y = y.esquerda
11     free aux
12 }
13 if y.esquerda == NULL
14     antecessor(y.esquerda, y)
15 aux = y
16 y = y.direita
17 free aux
```

* *T* representa uma estrutura de árvore e *x* um nó

__*<u>Testes utilizando Árvore Binária de Pesquisa</u>*__

Após ser feita a implementação de todos os algoritmos básicos presentes em uma `Árvore Binária de Pesquisa` foi possível realizar os testes propostos em  <a href="#apresentação">Apresentação</a> obtendo então os seguintes resultados informados na tabela a seguir:

<p align="left">
<img src="imgs/tabelaABP.png" width="1170" height="125"/>
</p>
<i>Tabela 2: Tempos médios de comparações para pesquisa, remoção e motagem da estrutura de Árvore Binária de Pesquisa.</i>
<br><br>

Onde os mesmos são fornecidos pelo programa desenvolvido da seguinte forma após a sua compilação:

<p align="left">
<img src="imgs/saidaABP.png" width="300"/>
</p>
<i>Figura 6: Tempos encontrados após execução para diferentes processos implementados na Árvore Binária de Pesquisa.</i>
<br><br>

---

## Conclusão

_

---

## Bibliotecas

<p>Para o funcionamento do programa, é necessário incluir as seguintes bibliotecas onde suas instalações estão situadas em <a href="#instalação-dos-módulos-necessários">Instalação dos módulos necessários</a>: 
<ul>
    <li><code>import networkx as nx</code></li>
    <li><code>import matplotlib</code></li>
    <li><code>import matplotlib.pyplot as plt</code></li>

</ul>

---

## Execução do projeto

Algumas observações e comentários necessários antes que seja executado o projeto: 

• Este código foi desenvolvido com Python 3.10.7 em conjunto com os seguintes módulos: NetworkX (v. 2.8.8) e Matplotlib (v. 3.6.2). A instalação dos módulos mencionados se encontra em <a href="#instalação-dos-módulos-necessários">Instalação dos módulos necessários</a>
<br>• O comando nas seções abaixo assume que seu seu executável python utilize <code>python3</code> e o instalador do pacote Python (pip), sendo seu comando <code>pip</code>
<br>• Além disso, pressupõe que o módulo <code>venv</code> esteja instalado, pois será utilizado para construir o Ambiente Virtual Python para que executar o projeto

### Instalação dos módulos necessários

1. Para a instalação do sistema de gerenciamento de pacotes <b>pip</b> é necessário, em seu terminal, digitar o seguinte comando <code>sudo apt update</code> (necessário para atualizar a lista de pacotes), após isso digite o seguinte comando para instalar, <code>sudo apt install python3-pip</code> ou <code>apt-get install python3-pip</code>, lembrando de certificar se o Python 3 está instalado.<br>
2. Para a criação e ativação da <b>Python Virtual Environmente (venv)</b> é necessário clonar ou baixar este repositório em sua máquina e em seguida dentro do diretório raiz do projeto crie um <b>Python Virtual Environmente (venv)</b> com o seguinte comando: <code>python -m venv ./venv</code>. Após isso, é necessário ativar o ambiente virtual (venv) para executar o módulo. Em máquinas Linux, geralmente para ativar basta digitar o seguinte comando: <code>source venv/bin/activate</code>. No Windows <code>.\venv\Scripts\activate</code>. Caso queira sair do ambiente virtual basta executar <code>deactivate</code><br>
3. Após a instalação do ambiente virtual (venv) já feita, é necessário instalar as dependências necessárias para este projeto: <br>3.1. Para a instalação do método <b>NetworkX</b> basta digitar o comando <code>pip3 install networkx[default]</code> em seu terminal.<br>3.2. Para a instalação do método <b>matplotlib</b> é necessário digitar o seguinte comando em seu terminal; <code>pip3 install matplotlib</code>

<br>• Após a realização desses procedimentos você estará pronto para a execução do projeto, precisando apenas digitar o seguinte comando em seu terminal, <b><code>python3 main.py</code></b>, necessário apenas estar presente no *ambiente virtual (venv)* como mencionado acima.

---

## Referências

[1] Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008

[2] J. D. Hunter, "Matplotlib: A 2D Graphics Environment", *Computing in Science & Engineering*, vol. 9, no. 3, pp. 90-95, 2007.

[3] MARIANO, Diego. **Networkx**: Analisando grafos com Python e a biblioteca Networkx. [S. l.], 20 nov. 2020. Disponível em: https://diegomariano.com/networkx/. Acesso em: 19 nov. 2022.

---

## Autor

Desenvolvido por [João Marcelo Gonçalves Lisboa](https://github.com/joaojmgl) e [Pedro Henrique Louback Campos](https://github.com/PedroLouback)

Ambos alunos do 4° periodo do curso de `Engenharia de Computação` no [CEFET-MG](https://www.cefetmg.br)
