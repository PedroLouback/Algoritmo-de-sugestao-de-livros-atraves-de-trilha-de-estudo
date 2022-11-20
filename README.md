# Algoritmo de sugestão de livros de estudos baseado em escolhas de temas relacionados a tecnologia
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## Conteúdos

<p align="center">
    <a href="#apresentação">Apresentação</a> •
    <a href="#introdução">Introdução</a> • 
    <a href="#estrutura-e-sua-implementação">Estrutura e sua implementação</a> •
    <a href="#resultados-e-análises">Resultados e Análises</a> •
    <a href="#conclusão">Conclusão</a> •
    <a href="#bibliotecas">Bibliotecas</a> •
    <a href="#compilação-e-execução">Compilação e Execução</a> •
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
 
## Resultados e Análises
 
• Após todo o código ser implementado com suas respectivas estruturas funcionando, foi possível realizar testes para obtenção do resultados de tempo de cada tipo de estrutura mencionado na proposta, onde foi possível obter os valores que estão presentes na **tabela 2**, **tabela 4**, **tabela 6**, **tabela 8**, **tabela 9** e **tabela 10**, mostrando seus tempos médios para os diferentes tamanhos de entradas e processos, possibilitando a criação dos seguintes gráficos a seguir:

<p align="center">
<img src="imgs/Graph500entries.png" width="400"/>
<img src="imgs/Graph5000entries.png" width="405"/>
</p>
<i>Figura 19: Gráficos de tempo (s) em relação aos tipos diferentes de árvores ao serem utilizadas nos processos de pesquisa e remoção com 500 e 5.000 entradas.</i>
<br><br>

<p align="center">
<img src="imgs/Graph50000entries.png" width="400"/>
<img src="imgs/Graph500000entries.png" width="400"/>
</p>
<i>Figura 20: Gráficos de tempo (s) em relação aos tipos diferentes de árvores ao serem utilizadas nos processos de pesquisa e remoção com 50.000 e 500.000 entradas.</i>

<p align="center">
<img src="imgs/GraphMontagemEstrutura.png" width="400"/>
</p>
<i>Figura 21: Gráfico contendo a média de tempo (eixo y) dos diferentes tamanhos de entrada utilizado para a montagem da estrutura de cada árvore (eixo x) </i>
<br><br>

<p align="center">
<img src="imgs/GraphEstruturas.png" width="400"/>
</p>
<i>Figura 22: Gráfico contendo a média de tempo (eixo y) dos diferentes tamanhos de entrada utilizado para a pesquisa de cada estruturas citada (eixo x) </i>
<br><br>
 
Observando que foi utilizado um total de 10.000 números do tipo flutuante para realizar as pesquisas nas respectivas estruturas, considerando que:

* Há um total de **3** números iguais no conjunto de 10.000 números em relação a entrada de 500 números, sendo **_0.6%_** do total de entradas mencionada;
* Há um total de **10** números iguais no conjunto de 10.000 números em relação a entrada de 5.000 números, sendo **_0.2%_** do total de entradas mencionada;
* Há um total de **66** números iguais no conjunto de 10.000 números em relação a entrada de 50.000 números, sendo **_1.32%%_** do total de entradas mencionada;
* Há um total de **601** números iguais no conjunto de 10.000 números em relação a entrada de 500.000 números, sendo **_12.02%%_** do total de entradas mencionada.
 
•Todos os teste foram realizados em uma máquina com as seguintes especificações, sendo elementos ocasionais de incertezas nas medições de tempo:

**Processador:** AMD Ryzen 5 1600;<br><br>
**Mémoria :** 16 GB - 1600 Mhz;<br><br>
**Sistema Operacional:** Linux - Ubuntu 20.04 LTS

---

## Conclusão

__*<u>Montagem em estrutura</u>*__
- Levando em consideração esses valores apresentados em relação aos resultados obtidos de tempo foi possível analisar através de comparações que para *montagem em estrutura* a <a href="#•-árvore-binária-de-pesquisa">Árvore Binária de Pesquisa</a> se destaca por não possuir nenhuma limitação em sua inserção como as outras árvores possuem para garantir o balanceamento, ou seja, pela `Árvore Binária de Pesquisa` não ser uma estrutura balanceada sem condições de construção, se torna uma estrutura mais eficiente na montagem. Ao contrário disso, foi possível visualizar que a <a href="#•-árvore-redblack">Árvore RedBlack</a> obteve uma  menor eficiência em sua *montagem em estrutura* por se tratar de uma árvore que, entre as árvores balanceadas envolvidas nos testes, possui um maior número de casos para serem tratadas na inserção em mémoria, tornando o processo de montagem um pouco mais lento, havendo uma diferença de **<u>0,060821334 segundos</u>** na *montagem em estrutura* entre a `Árvore Binária de Pesquisa` e `Árvore RedBlack`.

__*<u>Pesquisa</u>*__
- Utilizando de base os resultados obtidos e estruturados, foi possível notar pela comparação das médias uma diferença positiva para a <a href="#•-árvore-redblack">Árvore RedBlack</a>, sendo seguida da <a href="#•-árvore-avl">Árvore AVL</a> e por último a <a href="#•-árvore-binária-de-pesquisa">Árvore Binária de Pesquisa</a> em ranking de velocidade de execução durante as pesquisas para até 50.000 entradas, sendo explicado pela falta de balanceamento da `Árvore Binária de Pesquisa`, tornando-a mais lenta.
 Após ser realizado o último testes com um total de 500.000 entradas foi possível observar que obteve uma diferença em relação ao ranking de tempos onde a `Árvore Binária de Pesquisa` tomou a liderança de mais rápida, seguinda pela `Árvore AVL` ficando em ultimo lugar a `Árvore RedBlack` sendo a estrutura que demorou mais tempo para realizar pesquisas, podendo ocasionar essa diferença na maior quantidade de entradas por possuir cerca de **12%** de seus elementos presentes nos 10.000 números utilizados para consulta e por ser uma árvore um pouco menos estritamente equilibrida que a `Árvore AVL` como mencionado nas explicações das estruturas acima. Apesar da estrutura `Árvore AVL` apresentar resultado mediano em todos os teste é levado em consideração a massa de dados iguais contidas na árvore em relação as 10.000 entradas de consulta pois é vísivel em literatura [1] que a `Árvore AVL` se destaca na eficiência de pesquisa em relação a `Árvore RedBlack`.

__*<u>Remoção</u>*__
- Com esses mesmos dados foi concluido que no processo de remoção de elementos das estruturas estudadas, entre elas se destacou novamente a `Árvore RedBlack`, agora em sincronia com conteúdos encontrados na literatura [1] é possível concordar com os resultados forncedios pelo teste, em sequência no ranking está situado a `Árvore AVL` e por fim a `Árvore Binária de Pesquisa`. A `Árvore RedBlack` se destaca nesse processo em relação a outros tipos de árvores mencionados pois menos rotações são realizadas devido ao balancemaneto relativamente relaxado.

__*<u>Comparações com vetores</u>*__
- Utilizando os testes citados anteriormente em comparação com teste realizados é possível visualizar utilizando como referência o gráfico apresentado na **Figura 22** que estruturas do tipo *Árvore* apresentam maior eficiência em pesquisa de elementos quando comparadas com utilização da `Busca Binária` em vetores ordenados, havendo um diferença de tempo de **<u>0,00040225 segundos</u>** entre a `Árvore Binária de Pesquisa` (estrutura menos eficiente para pesquisa) e a pesquisa em vetores ordenados, onde para a implementação da `Pesquisa Binária` foi necessária a utilização da função sort() como mencionada anteriormente na explicação das estruturas, podendo visualizar os tempos de ordenação para os diferentes tamanhos de entradas no gráfico abaixo:

<p align="center">
<img src="imgs/GraphVector.png" width="450"/>
</p>
<i>Figura 23: Gráfico contendo a média de tempo (eixo y) dos diferentes tamanhos de entrada utilizado para a ordenação de vetores (eixo x) </i>
<br><br>

__*<u>Utilização de estruturas MAPs</u>*__
- Ao adotar as estruturas MAPs mencionadas em <a href="#•-estruturas-maps">MAPs</a> foi realizado testes, possibilitando as seguintes conclusões.<br><br>
 **Para a utilização da função std::map()** em comparação com as demais estruturas analisadas com testes de pesquisa foi possível observar que obteve um eficiência maior tendo uma diferença **<u>0,000828749 segundos</u>** entre a `Árvore RedBlack` (segunda estrutura mais eficiente para pesquisa) e a utilização da estrutura **map()** para pesquisa, essa eficiência deve se a sua maneira de armazenar elementos internamente como `Árvore Binária de Pesquisa` balanceada, tendo uma complexidade $O(log{n})$ mesmo no pior caso. É possível observar esse ganho de eficiência em comparação com as outras estruturas no gráfico plotado abaixo:

<p align="center">
<img src="imgs/Graphmap.png" width="450"/>
</p>
<i>Figura 24: Gráfico contendo a média de tempo (eixo y) dos diferentes tamanhos de entrada utilizado para a ordenação de diferentes estruturas (eixo x) </i>
<br><br>

 **Para a utilização da função std::unordered_map()** foi feita também testes de pesquisas, possibilitando a sua comparação com os testes de pesquisas feitos com as estruturas presentes no código, onde foi possível observar um ganho de eficiência ainda maior comparado com a ultima estrutura implementada *std::map* reduzindo o tempo de pesquisa em  **<u>0,002289 segundos</u>** (quase um terço do seu tempo) entre ela, possuindo uma diferença de  **<u>0,00311775 segundos</u>** da `Árvore RedBlack` (estrutura em árvore mais eficiente em pesquisa). Essa estrutura apresenta esse ganho de tempo no processo de pesquisa por armazenar elementos usando `Tabela Hash`, buscando uma chave específica torna sua complexidade para a operação de $O(1)$. É possível observar esse ganho de eficiência em relação as outras estruturas no gráfico plotado abaixo:

<p align="center">
<img src="imgs/Graphunordered_map.png" width="450"/>
</p>
<i>Figura 25: Gráfico contendo a média de tempo (eixo y) dos diferentes tamanhos de entrada utilizado para a ordenação de diferentes estruturas (eixo x) </i>
<br><br>

---

## Bibliotecas

<p>Para o funcionamento do programa, é necessário incluir as seguintes bibliotecas: 
<ul>
    <li><code>#include 'iostream'</code></li>
    <li><code>#include 'stdio.h'</code></li>
    <li><code>#include 'stdbool.h'</code></li>
    <li><code>#include 'stdlib.h'</code></li>
    <li><code>#include 'vector'</code></li>
    <li><code>#include 'fstream'</code></li>
    <li><code>#include 'random'</code></li>
    <li><code>#include 'iomanip'</code></li>
    <li><code>#include 'string'</code></li>
    <li><code>#include 'sstream'</code></li>
    <li><code>#include 'algorithm'</code></li>
    <li><code>#include 'bits/stdc++.h'</code></li>
    <li><code>#include 'ctime'</code></li>
    <li><code>#include 'unordered_map'</code></li>
    <li><code>#include 'map'</code></li>
</ul>

---

## Referências

[1] CORMEM, Thomas H. et al. __Algoritmos__: Teoria e Prática. 3. ed. Cambridge, Massachussetts: MIT Press, [2009]. 1292 p. ISBN 9780262033848.

[2] THAPLIYAL, Rohit. __Map vs unordered_map in C++__. [S. l.]: GeeksforGeeks, 7 jul. 2022. Disponível em: https://www.geeksforgeeks.org/map-vs-unordered_map-c/. Acesso em: 15 out. 2022.

[3]STROUSTRUP, B. Cplusplus. Disponível em: <https://cplusplus.com>. Acesso em: 17 out. 2022.

---

## Compilação e Execução

O programa feito de acordo com a proposta possui um arquivo Makefile que realiza todo o procedimento de compilação e execução. Para tanto, temos as seguintes diretrizes de execução:


| Comando                |  Função                                                                                           |                     
| -----------------------| ------------------------------------------------------------------------------------------------- |
|  `make clean`          | Apaga a última compilação realizada contida na pasta build                                        |
|  `make`                | Executa a compilação do programa utilizando o gcc, e o resultado vai para a pasta build           |
|  `make run`            | Executa o programa da pasta build após a realização da compilação             


---

## Autor

Desenvolvido por [Pedro Henrique Louback Campos](https://github.com/PedroLouback) e [João Marcelo Gonçalves Lisboa](https://github.com/joaojmgl), [João Pedro Martins Espíndola](https://github.com/JoaoMEspindola?tab=repositories)

Ambos alunos do 4° periodo do curso de `Engenharia de Computação` no [CEFET-MG](https://www.cefetmg.br)
