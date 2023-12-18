class Elemento: # Cria a classe do nó (chamado elemento para deixar mais claro).
    def __init__(self): # Método construtor do nó, utilizado para instanciá-lo.
        self.valor = 0 # Definindo os valores padrão dos atributos da classe (0 e None). 
        self.dir = None 
        self.esq = None

def busca(chave, pont, pai=None):  # Adicione o parâmetro pai com o valor padrão None.
    if pont is None:
        f = 0  # A árvore está vazia, indica que a chave não foi encontrada.
    else:
        if pont.valor == chave:
            f = 1  # A chave foi encontrada no nó atual.
        else:
            if chave < pont.valor:
                if pont.esq is None:
                    f = 2  # O valor buscado é menor que a chave, e o filho esquerdo é nulo, indica que a chave não está na árvore.
                else:
                    pai = pont  # Atualize o valor de pai quando descer para o filho esquerdo.
                    pont = pont.esq
                    pont, f, aux = busca(chave, pont)  # Recursivamente continua a busca no filho esquerdo.
            else:
                if pont.dir is None:
                    f = 3  # O valor buscado é maior que a chave, e o filho direito é nulo, indica que a chave não está na árvore.
                else:
                    pai = pont  # Atualize o valor de pai quando descer para o filho direito.
                    pont = pont.dir
                    pont, f, aux = busca(chave, pont)  # Recursivamente continua a busca no filho direito.
    return pont, f, pai

def inclusao(chave, raiz):
    pont, flag, pai = busca(chave, raiz) # Realiza a busca que retorna respectivamente o último ponteiro buscado e sua flag.
    if flag == 1: # Se a flag = 1, o valor já está na árvore e não é possível repetí-lo.
        print()
        print('A chave já está na árvore!')
        print()
    else:
        novo = Elemento()   # Instancia um novo nó com o valor da chave inserida como argumento da função.
        novo.valor = chave
        if flag == 0:       # Se a flag = 0 (árvore vazia), o elemento instanciado passa a ser o primeiro da árvore, logo, a raiz.
            raiz = novo
        else:
            if flag == 2:   # Se a flag = 2 (elemento não está na árvore e o valor a ser inserido é na posição de filho esquerdo do ponteiro), atualiza o valor de pont.esq.
                pont.esq = novo # O valor pont.esq que antes era None passa a ser o elemento instanciado.
            else: # Se a flag = 3 (elemento não está na árvore e o valor a ser inserido é na posição de filho direito do ponteiro), atualiza o valor de pont.dir.
                pont.dir = novo # O valor pont.esq que antes era None passa a ser o elemento instanciado.
        pont = novo
        print()
        print('Elemento incluído!') # Informa a inclusão devida do elemento.
        print()
    return raiz # Retorna o valor atualizado da raiz.

def exclusao(chave, raiz):
    raiz, flag = exclusao_recursiva(chave, raiz)
    if flag == 1:
        print()
        print('O elemento foi devidamente excluído!') # Se, no algoritmo de exclusao, a flag for = 1 (elemento foi excluído), retorna esta mensagem.
        print()
    if flag == 0:
        print()
        print('A chave não está na árvore!') # Se, no algoritmo de exclusao, a flag for = 0 (elemento não foi excluído), retorna esta mensagem.
        print()
    return raiz

def exclusao_recursiva(chave, pont):
    # Inicializa uma variável de controle 'flag' como 0.
    flag = 0

    # Verifica se o nó atual (pont) não é nulo.
    if pont is not None:
        # Verifica se a chave a ser excluída é menor que o valor do nó atual.
        if chave < pont.valor:
            # Chama recursivamente a função para o nó à esquerda.
            pont.esq, flag = exclusao_recursiva(chave, pont.esq)
        # Se a chave for maior que o valor do nó atual:
        elif chave > pont.valor:
            # Chama recursivamente a função para o nó à direita.
            pont.dir, flag = exclusao_recursiva(chave, pont.dir)
        # Se a chave for igual ao valor do nó atual (caso de exclusão):
        else:
            # Verifica se o nó à esquerda é nulo.
            if pont.esq is None:
                # Se sim, substitui o nó atual pelo nó à direita.
                pont = pont.dir
                flag = 1  # Define a flag como 1 indicando que a exclusão foi realizada.
            # Se o nó à direita é nulo:
            elif pont.dir is None:
                # Substitui o nó atual pelo nó à esquerda.
                pont = pont.esq
                flag = 1  # Define a flag como 1 indicando que a exclusão foi realizada.
            # Se o nó possui ambos os filhos:
            else:
                # Encontra o valor mínimo na subárvore à direita.
                pont.valor = valor_min(pont.dir).valor
                # Chama recursivamente a exclusão para remover o valor mínimo encontrado.
                pont.dir, _ = exclusao_recursiva(pont.valor, pont.dir)
                flag = 1  # Define a flag como 1 indicando que a exclusão foi realizada.

    # Retorna o nó atual e a flag para indicar se a exclusão ocorreu.
    # Obs.: as verificações acima servem para saber se o nó a ser removido possui sub-árvores. Se for o caso, a substituição pode ser diferente.
    return pont, flag

def valor_min(pont):
    while pont.esq is not None: # Enquanto existir um filho a esquerda do ponteiro atual, seu valor será atualizado como seu filho esquerdo.
        pont = pont.esq
    return pont # Retorna o filho mais a esquerda da árvore (menor valor).

def percorrer_bfs(raiz):
    global c # Variável global usada para determinar a quantidade de elementos da árvore e, consequentemente, da lista de exibição.
    header = Elemento()
    header.valor = "Header"    # É criado um objeto do tipo Elemento e atribuído à variável header. O valor desse elemento é definido como "Header". Depos cria uma lista em que o primeiro e único elemento até então seja o header.
    resultado = [header.valor] # Seu objetivo é fazer com que o primeiro elemento da lista seja resultado[1], de forma que A[i*2] seja sempre o filho esquerdo e A[i*2+1] o filho direito de A[i].
    if not raiz: # Verificação se a árvore está vazia
        resultado = 'Árvore vazia!'
    else:
        zero = Elemento() # Caso a árvore não esteja vazia, é criado um novo elemento zero cujo valor é None.
        zero.valor = None # Isso será usado para representar os nós ausentes nos níveis mais baixos da árvore.
        lista = [raiz]
        indice = 0
        while indice < len(lista):
            elemento_atual = lista[indice]          # Obtém o elemento atual da lista com base no índice e adiciona o valor desse elemento à lista 'resultado'.
            resultado.append(elemento_atual.valor)       
            if elemento_atual.esq is not None:      # Verifica se o nó atual tem um filho esquerdo. Se tiver, adiciona o filho esquerdo à lista 'lista'.
                lista.append(elemento_atual.esq)    # Caso contrário, adiciona o elemento zero à lista para representar a ausência de um filho esquerdo.
            else:
                lista.append(zero)
                if c + 1 == len(resultado):
                    break

            if elemento_atual.dir is not None:      # Faz o mesmo para o filho direito.
                lista.append(elemento_atual.dir)
            else:
                lista.append(zero)                  # O bloco if c + 1 == len(resultado): break verifica se a próxima posição na lista seria o início de um novo nível da árvore.
                if c + 1 == len(resultado):         # Se for verdadeiro, o loop é interrompido.
                    break
            indice += 1                             # Incrementa o índice para passar para o próximo elemento.
    return resultado

def empilhar(pilha, node):
    # Verifica se o nó não é nulo (node is not None).
    # Se o nó não é nulo, adiciona o nó à lista da pilha.
    if node is not None:
        pilha.append(node)

def desempilhar(pilha):
    if not pilha:
        pilha = None # Se a pilha está vazia, a função atribui None à pilha.
    else:
        pilha = pilha.pop() # Se a pilha não está vazia, a função remove o último elemento da pilha e atribui a lista resultante à variável pilha.
    return pilha

def preordem(raiz):
    resultado = []
    pilha = []
    empilhar(pilha, raiz) # Chama a função empilhar para empilhar a raiz na pilha

    while pilha: # Entra em um loop while que continua enquanto a pilha não está vazia.
        no_atual = desempilhar(pilha) # A função desempilhar retira o último nó da pilha e atribui a no_atual.
        
        if no_atual is not None:
            # Se o nó atual não for nulo, o valor do nó é adicionado à lista resultado.
            # Empilha os filhos direito e esquerdo do nó (se é que eles existem).
            resultado.append(no_atual.valor)
            empilhar(pilha, no_atual.dir) # O filho direito é empilhado primeiro para garantir que seja processado antes do filho esquerdo, mantendo a ordem de pré-ordem.
            empilhar(pilha, no_atual.esq)
    return resultado

arvore = []
raiz = None
c = int(input('Por favor, digite a quantidade máxima de elementos a serem exibidos na árvore: '))
def Menu():
    global raiz, arvore
    menu = 1
    while menu == 1:
        print('-'*15, 'MENU', '-'*15)
        print('Se deseja incluir um novo elemento, digite 1.')
        print('Se deseja excluir um elemento, digite 2.')
        print('Se deseja percorrer a árvore em pré-ordem, digite 3 para fazer o percurso e exibir o resultado.')
        print('Para exibir a árvore numa lista onde lista[1] é a raíz, lista[i] é um elemento tal que lista[i*2] é seu filho esquerdo e lista [(i*2)+1] seu filho direito, digite 4.')
        print('Para encerrar a aplicação, digite 5.')
        opcao = int(input('Opção escolhida: '))
        while opcao <= 0 or opcao >= 6:
            opcao = int(input('Opção inválida. Escreva um número de 1 a 5: '))
        if opcao == 1:
            incluir = int(input('Elemento a ser incluído (digite a chave): '))
            raiz = inclusao(incluir, raiz)
        elif opcao == 2:
            excluir = int(input('Elemento a ser excluído (digite a chave): '))
            raiz = exclusao(excluir, raiz)
        elif opcao == 3:
            listapreordem = preordem(raiz)
            print()
            print(f'Lista com os elementos na ordem do percurso: {listapreordem}')
            print()
        elif opcao == 4:
            arvore = percorrer_bfs(raiz)
            print()
            print(f'A árvore é: {arvore}')
            print()
        else:
            menu = 0
            print()
            print('O programa está sendo encerrado. Obrigado por utilizá-lo!')
            print()

Menu()
