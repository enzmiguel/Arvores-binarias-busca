# Árvore Binária de Busca (ABB) - README

## Descrição do Projeto

Este projeto foi desenvolvido inspirado em um trabalho para a disciplina de Estrutura de Dados e Algoritmos para a Universidade Federal da Bahia. Todo o código foi elaborado de forma 100% autoral e individual, sendo uma iniciativa pessoal para aplicar os conceitos aprendidos durante o curso.

## Objetivo Didático

O principal objetivo deste projeto é fornecer uma implementação prática dos conceitos de Árvores Binárias de Busca. O algoritmo também utiliza de ferramentas utilizadas em outros conteúdos da disciplina como elementos encadeados, pilhas e algoritmo de exibição inspirados nos heaps. A estrutura da árvore e as operações associadas, como inclusão, exclusão e percurso em pré-ordem, foram implementadas com foco na compreensão didática.

Este código pode servir como uma ferramenta de aprendizado para estudantes que desejam consolidar seus conhecimentos em estruturas de dados, especialmente em relação às árvores binárias de busca.

## Descrição do Código

O código implementa uma Árvore Binária de Busca (ABB) em Python. A ABB é uma estrutura de dados que organiza os elementos de forma hierárquica, permitindo operações eficientes de busca, inserção e remoção. Cada nó da árvore contém um valor, um ponteiro para o filho esquerdo e um ponteiro para o filho direito.

O código inclui as seguintes funcionalidades:

**Inclusão (Inserção):** Permite adicionar um novo elemento à árvore.

**Exclusão (Remoção):** Permite remover um elemento da árvore.

**Busca:** Realiza a busca por um elemento na árvore.

**Percurso em Pré-ordem:** Percorre a árvore em pré-ordem e exibe os elementos.

**Exibição da Árvore em Lista:** Exibe a árvore em forma de lista, onde lista[1] é a raiz, lista[i\*2] é o filho esquerdo e lista[(i\*2)+1] é o filho direito do elemento lista[i].

*Obs: inspiração nos heaps.*

## Como Utilizar

1. Execute o código em um ambiente Python.

2. Digite a quantidade de elementos que será exibida na lista heap.

3. Será exibido um menu com opções numeradas.

4. Escolha a opção desejada digitando o número correspondente.

5. Siga as instruções para realizar a inclusão, exclusão, percurso em pré-ordem ou exibição da árvore.

6. Após finalizar a operação escolhida no menu, deverá escolher novamente a opção desejada.

7. Para encerrar o programa, escolha a opção correspondente no menu.

## Exemplo de Utilização

- Insira os seguintes comandos no terminal:

```7 > 1 > 20 > 1 > 30 > 1 > 5 > 1 > 25 > 1 > 35 > 4```

*Obs: a cada ">" pressione enter.*

e a seguinte árvore abaixo será exibida como um heap:


         20
       /   \
     10     30
     /      / \
    5      25 35
   
**Em formato de heap:** ['Header', 20, 10, 30, 5, None, 25, 35]


- Após o print, insira os comandos:

```2 > 30```


e o 35 substituirá o elemento 30 removido, junto com sua subárvore esquerda.

A árvore resultante será:

         20
       /   \
     10     35
     /      / 
    5      25 

**Em formato de heap:** ['Header', 20, 10, 35, 5, None, 25, None]


## Contribuições e Melhorias

Contribuições são encorajadas! Se você identificar oportunidades de melhoria, correções ou tiver sugestões adicionais para enriquecer o projeto, sinta-se à vontade para colaborar através de problemas (issues) ou solicitações de pull (pull requests).

---

*Este projeto foi desenvolvido com o intuito educacional e reflexo do aprendizado individual na disciplina mencionada.*
