import array
from abc import ABC, abstractmethod
import json

### --- Classes base e matrizes ---  ###

class Matriz(ABC):
    @abstractmethod
    def get(self, i, j): pass

    @abstractmethod
    def set(self, i, j, valor): pass

    @abstractmethod
    def mostrar(self): pass

    @abstractmethod
    def determinante(self): pass

    @abstractmethod
    def somar(self, outra): pass

    @abstractmethod
    def subtrair(self, outra): pass

    @abstractmethod
    def traco(self): pass

    @property
    @abstractmethod
    def n(self): pass

    @property
    @abstractmethod
    def tipo(self): pass

### ---Classe de matrizes diagonais--- ###
class MatrizDiagonal(Matriz):
    def __init__(self, diagonal: list[int]):
        self._n = len(diagonal)
        self.diagonal = array.array('i', diagonal)

    @property
    def n(self): return self._n
    @property
    def tipo(self): return 'Diagonal'

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            return self.diagonal[i] if i == j else 0
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def set(self, i, j, valor):
        if 0 <= i < self.n and 0 <= j < self.n:
            if i == j:
                self.diagonal[i] = valor
            else:
                raise ValueError("Só é possível alterar valores na diagonal.")
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def mostrar(self):
        for i in range(self.n):
            print([self.get(i, j) for j in range(self.n)])

    def determinante(self):
        det = 1
        for val in self.diagonal:
            det *= val
        return det

    def somar(self, outra):
        if not isinstance(outra, MatrizDiagonal) or self.n != outra.n:
            raise ValueError("Só é possível somar matrizes diagonais de mesma ordem.")
        nova_diag = [self.diagonal[i] + outra.diagonal[i] for i in range(self.n)]
        return MatrizDiagonal(nova_diag)

    def subtrair(self, outra):
        if not isinstance(outra, MatrizDiagonal) or self.n != outra.n:
            raise ValueError("Só é possível subtrair matrizes diagonais de mesma ordem.")
        nova_diag = [self.diagonal[i] - outra.diagonal[i] for i in range(self.n)]
        return MatrizDiagonal(nova_diag)

    def traco(self):
        return sum(self.diagonal)

### ---Classe de Matrizes Quadradas--- ###
class MatrizQuadrada(Matriz):
    def __init__(self, n: int, valores: list[int]):
        self._n = n
        if len(valores) != n*n:
            raise ValueError(f"Esperado {n*n} elementos, recebido {len(valores)}.")
        self.valores = array.array('i', valores)

    @property
    def n(self): return self._n
    @property
    def tipo(self): return 'Quadrada'

    def _indice(self, i, j):
        return i * self.n + j

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            return self.valores[self._indice(i, j)]
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def set(self, i, j, valor):
        if 0 <= i < self.n and 0 <= j < self.n:
            self.valores[self._indice(i, j)] = valor
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def mostrar(self):
        for i in range(self.n):
            print([self.get(i, j) for j in range(self.n)])

    def determinante(self):
        # Para simplicidade, só para matrizes 2x2 e 3x3
        if self.n == 1:
            return self.get(0, 0)
        elif self.n == 2:
            return self.get(0,0)*self.get(1,1) - self.get(0,1)*self.get(1,0)
        elif self.n == 3:
            a = self.get(0,0)
            b = self.get(0,1)
            c = self.get(0,2)
            d = self.get(1,0)
            e = self.get(1,1)
            f = self.get(1,2)
            g = self.get(2,0)
            h = self.get(2,1)
            i = self.get(2,2)
            return (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)
        else:
            raise NotImplementedError("Determinante implementado só para matrizes até 3x3.")

    def somar(self, outra):
        if not isinstance(outra, MatrizQuadrada) or self.n != outra.n:
            raise ValueError("Só é possível somar matrizes quadradas de mesma ordem.")
        nova = [self.valores[i] + outra.valores[i] for i in range(len(self.valores))]
        return MatrizQuadrada(self.n, nova)

    def subtrair(self, outra):
        if not isinstance(outra, MatrizQuadrada) or self.n != outra.n:
            raise ValueError("Só é possível subtrair matrizes quadradas de mesma ordem.")
        nova = [self.valores[i] - outra.valores[i] for i in range(len(self.valores))]
        return MatrizQuadrada(self.n, nova)

    def traco(self):
        soma = 0
        for i in range(self.n):
            soma += self.get(i,i)
        return soma

### ---Matriz Triangular Inferior--- ###
class MatrizTriangularInferior(Matriz):
    def __init__(self, n: int, valores: list[int]):
        self._n = n
        esperado = n*(n+1)//2
        if len(valores) != esperado:
            raise ValueError(f"Esperado {esperado} elementos, recebido {len(valores)}.")
        self.valores = array.array('i', valores)

    @property
    def n(self): return self._n
    @property
    def tipo(self): return 'Triangular Inferior'

    def _indice(self, i, j):
        if i < j:
            return None
        return i*(i+1)//2 + j

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            idx = self._indice(i, j)
            return self.valores[idx] if idx is not None else 0
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def set(self, i, j, valor):
        if 0 <= i < self.n and 0 <= j < self.n:
            idx = self._indice(i, j)
            if idx is not None:
                self.valores[idx] = valor
            else:
                raise ValueError("Não é possível alterar elemento acima da diagonal.")
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def mostrar(self):
        for i in range(self.n):
            print([self.get(i,j) for j in range(self.n)])

    def determinante(self):
        det = 1
        for i in range(self.n):
            det *= self.get(i,i)
        return det

    def somar(self, outra):
        if not isinstance(outra, MatrizTriangularInferior) or self.n != outra.n:
            raise ValueError("Só é possível somar matrizes triangulares inferiores de mesma ordem.")
        nova = [self.valores[i] + outra.valores[i] for i in range(len(self.valores))]
        return MatrizTriangularInferior(self.n, nova)

    def subtrair(self, outra):
        if not isinstance(outra, MatrizTriangularInferior) or self.n != outra.n:
            raise ValueError("Só é possível subtrair matrizes triangulares inferiores de mesma ordem.")
        nova = [self.valores[i] - outra.valores[i] for i in range(len(self.valores))]
        return MatrizTriangularInferior(self.n, nova)

    def traco(self):
        soma = 0
        for i in range(self.n):
            soma += self.get(i,i)
        return soma

### ---Matriz Triangular Superir--- ###
class MatrizTriangularSuperior(Matriz):
    def __init__(self, n: int, valores: list[int]):
        self._n = n
        esperado = n*(n+1)//2
        if len(valores) != esperado:
            raise ValueError(f"Esperado {esperado} elementos, recebido {len(valores)}.")
        self.valores = array.array('i', valores)

    @property
    def n(self): return self._n
    @property
    def tipo(self): return 'Triangular Superior'

    def _indice(self, i, j):
        if i > j:
            return None
        return i * self.n - i*(i-1)//2 + (j - i)

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            idx = self._indice(i, j)
            return self.valores[idx] if idx is not None else 0
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def set(self, i, j, valor):
        if 0 <= i < self.n and 0 <= j < self.n:
            idx = self._indice(i, j)
            if idx is not None:
                self.valores[idx] = valor
            else:
                raise ValueError("Não é possível alterar elemento abaixo da diagonal.")
        else:
            raise IndexError("Índice fora dos limites da matriz.")

    def mostrar(self):
        for i in range(self.n):
            print([self.get(i,j) for j in range(self.n)])

    def determinante(self):
        det = 1
        for i in range(self.n):
            det *= self.get(i,i)
        return det

    def somar(self, outra):
        if not isinstance(outra, MatrizTriangularSuperior) or self.n != outra.n:
            raise ValueError("Só é possível somar matrizes triangulares superiores de mesma ordem.")
        nova = [self.valores[i] + outra.valores[i] for i in range(len(self.valores))]
        return MatrizTriangularSuperior(self.n, nova)

    def subtrair(self, outra):
        if not isinstance(outra, MatrizTriangularSuperior) or self.n != outra.n:
            raise ValueError("Só é possível subtrair matrizes triangulares superiores de mesma ordem.")
        nova = [self.valores[i] - outra.valores[i] for i in range(len(self.valores))]
        return MatrizTriangularSuperior(self.n, nova)

    def traco(self):
        soma = 0
        for i in range(self.n):
            soma += self.get(i,i)
        return soma


### --- Funções utilitárias --- ###

def matriz_identidade(n: int, tipo: str) -> Matriz:
    if tipo == 'diagonal':
        return MatrizDiagonal([1]*n)
    elif tipo == 'quadrada':
        valores = []
        for i in range(n):
            for j in range(n):
                valores.append(1 if i==j else 0)
        return MatrizQuadrada(n, valores)
    elif tipo == 'triangular_inferior':
        # diagonal 1 + zeros abaixo da diagonal
        valores = []
        for i in range(n):
            for j in range(i+1):
                valores.append(1 if i == j else 0)
        return MatrizTriangularInferior(n, valores)
    elif tipo == 'triangular_superior':
        valores = []
        for i in range(n):
            for j in range(i, n):
                valores.append(1 if i == j else 0)
        return MatrizTriangularSuperior(n, valores)
    else:
        raise ValueError("Tipo inválido para matriz identidade.")


### --- Lista de matrizes e operações no menu --- ###

lista_matrizes = []

def adicionar_matriz(matriz: Matriz, nome:str = None):
    lista_matrizes.append({'matriz': matriz, 'nome': nome})

def listar_matrizes():
    if not lista_matrizes:
        print("Lista de matrizes está vazia.")
        return
    for i, item in enumerate(lista_matrizes):
        nome = item['nome'] if item['nome'] else f"Matriz_{i}"
        matriz = item['matriz']
        print(f"[{i}] Nome: {nome}, Tipo: {matriz.tipo}, Ordem: {matriz.n}x{matriz.n}")
        print("Valores:")
        matriz.mostrar()  # Usa o método mostrar da matriz para imprimir os valores
        print()  # linha em branco para separar visualmente

def alterar_remover_matriz():
    listar_matrizes()
    idx = int(input("Digite o índice da matriz para alterar ou remover: "))
    if idx < 0 or idx >= len(lista_matrizes):
        print("Índice inválido.")
        return
    acao = input("Digite 'a' para alterar, 'r' para remover: ").strip().lower()
    if acao == 'r':
        lista_matrizes.pop(idx)
        print("Matriz removida.")
    elif acao == 'a':
        matriz = lista_matrizes[idx]['matriz']
        print("Digite o índice e valor para alteração (ex: i j valor), sair para sair:")
        while True:
            linha = input("Alterar: ")
            if linha.strip() == 'sair':
                break
            try:
                i_, j_, val_ = map(int, linha.split())
                matriz.set(i_, j_, val_)
                print(f"Valor alterado em ({i_},{j_}) para {val_}")
            except Exception as e:
                print(f"Erro: {e}")
    else:
        print("Ação inválida.")

def salvar_lista(nome_arquivo):
    lista_serializavel = []
    for item in lista_matrizes:
        m = item['matriz']
        tipo = m.tipo
        n = m.n
        nome = item['nome']
        # Serializar matriz conforme tipo
        if tipo == 'Diagonal':
            dados = list(m.diagonal)
        elif tipo == 'Quadrada':
            dados = list(m.valores)
        elif tipo == 'Triangular Inferior':
            dados = list(m.valores)
        elif tipo == 'Triangular Superior':
            dados = list(m.valores)
        else:
            dados = []
        lista_serializavel.append({'tipo': tipo, 'n': n, 'dados': dados, 'nome': nome})
    with open(nome_arquivo, 'w') as f:
        json.dump(lista_serializavel, f)
    print(f"Lista salva em {nome_arquivo}.")

def carregar_lista(nome_arquivo, substituir=True):
    try:
        with open(nome_arquivo, 'r') as f:
            dados = json.load(f)
        novas_matrizes = []
        for item in dados:
            tipo = item['tipo']
            n = item['n']
            nome = item.get('nome', None)
            dados_mat = item['dados']
            if tipo == 'Diagonal':
                m = MatrizDiagonal(dados_mat)
            elif tipo == 'Quadrada':
                m = MatrizQuadrada(n, dados_mat)
            elif tipo == 'Triangular Inferior':
                m = MatrizTriangularInferior(n, dados_mat)
            elif tipo == 'Triangular Superior':
                m = MatrizTriangularSuperior(n, dados_mat)
            else:
                continue
            novas_matrizes.append({'matriz': m, 'nome': nome})
        if substituir:
            lista_matrizes.clear()
        lista_matrizes.extend(novas_matrizes)
        print(f"Lista carregada de {nome_arquivo}.")
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")

def zerar_lista():
    lista_matrizes.clear()
    print("Lista de matrizes zerada.")


### --- Operações entre matrizes --- ###

def selecionar_matriz(titulo="Selecione a matriz pelo índice"):
    listar_matrizes()
    idx = int(input(f"{titulo}: "))
    if idx < 0 or idx >= len(lista_matrizes):
        raise IndexError("Índice inválido.")
    return lista_matrizes[idx]['matriz']

def operacoes_matrizes():
    print("\nOperações disponíveis:")
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Traço")
    print("[4] Determinante")
    op = input("Escolha a operação: ")

    if op == '1' or op == '2':
        print("Selecione a primeira matriz:")
        m1 = selecionar_matriz()
        print("Selecione a segunda matriz:")
        m2 = selecionar_matriz()
        try:
            if op == '1':
                resultado = m1.somar(m2)
                print("Resultado da soma:")
            else:
                resultado = m1.subtrair(m2)
                print("Resultado da subtração:")
            resultado.mostrar()
        except Exception as e:
            print(f"Erro na operação: {e}")
    elif op == '3':
        m = selecionar_matriz()
        try:
            print(f"Traço da matriz: {m.traco()}")
        except Exception as e:
            print(f"Erro no cálculo do traço: {e}")
    elif op == '4':
        m = selecionar_matriz()
        try:
            det = m.determinante()
            print(f"Determinante da matriz: {det}")
        except Exception as e:
            print(f"Erro no cálculo do determinante: {e}")
    else:
        print("Operação inválida.")


### --- Matriz padrão para cada tipo --- ###

def adicionar_matrizes_padroes():
    # Matriz diagonal padrão 3x3
    diag = MatrizDiagonal([1, 2, 3])
    adicionar_matriz(diag, "Diagonal padrão 3x3")

    # Matriz quadrada padrão 3x3
    quad = MatrizQuadrada(3, [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ])
    adicionar_matriz(quad, "Quadrada padrão 3x3")

    # Matriz triangular inferior padrão 3x3
    tri_inf = MatrizTriangularInferior(3, [
        1,
        2, 3,
        4, 5, 6
    ])  # armazenamento linear: linha0(1), linha1(2,3), linha2(4,5,6)
    adicionar_matriz(tri_inf, "Triangular Inferior padrão 3x3")

    # Matriz triangular superior padrão 3x3
    tri_sup = MatrizTriangularSuperior(3, [
        1, 2, 3,
           4, 5,
              6
    ])  # armazenamento linear: linha0(1,2,3), linha1(4,5), linha2(6)
    adicionar_matriz(tri_sup, "Triangular Superior padrão 3x3")


### --- Menu principal --- ###

def menu():
    adicionar_matrizes_padroes()
    while True:
        print("\nMenu:")
        print("[1] Listar matrizes")
        print("[2] Adicionar nova matriz")
        print("[3] Inserir matriz identidade")
        print("[4] Alterar/remover matriz")
        print("[5] Salvar lista (backup)")
        print("[6] Carregar lista de arquivo")
        print("[7] Zerar lista")
        print("[8] Operações com matrizes")
        print("[0] Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            listar_matrizes()
        elif escolha == '2':
            tipo = input("Tipo (diagonal, quadrada, triangular_inferior, triangular_superior): ").strip().lower()
            n = int(input("Ordem n: "))
            if tipo == 'diagonal':
                valores = list(map(int, input(f"Digite os {n} elementos da diagonal separados por espaço: ").split()))
                m = MatrizDiagonal(valores)
            elif tipo == 'quadrada':
                valores = list(map(int, input(f"Digite os {n*n} elementos da matriz separados por espaço: ").split()))
                m = MatrizQuadrada(n, valores)
            elif tipo == 'triangular_inferior':
                esperado = n*(n+1)//2
                valores = list(map(int, input(f"Digite os {esperado} elementos da matriz triangular inferior (linha a linha) separados por espaço: ").split()))
                m = MatrizTriangularInferior(n, valores)
            elif tipo == 'triangular_superior':
                esperado = n*(n+1)//2
                valores = list(map(int, input(f"Digite os {esperado} elementos da matriz triangular superior (linha a linha) separados por espaço: ").split()))
                m = MatrizTriangularSuperior(n, valores)
            else:
                print("Tipo inválido.")
                continue
            nome = input("Nome (opcional): ").strip()
            adicionar_matriz(m, nome if nome else None)
            print("Matriz adicionada.")
        elif escolha == '3':
            tipo = input("Tipo de matriz identidade (diagonal, quadrada, triangular_inferior, triangular_superior): ").strip().lower()
            n = int(input("Ordem n: "))
            try:
                m = matriz_identidade(n, tipo)
                nome = input("Nome (opcional): ").strip()
                adicionar_matriz(m, nome if nome else None)
                print("Matriz identidade adicionada.")
            except Exception as e:
                print(f"Erro: {e}")
        elif escolha == '4':
            alterar_remover_matriz()
        elif escolha == '5':
            arquivo = input("Digite o nome do arquivo para salvar (ex: backup.json): ").strip()
            salvar_lista(arquivo)
        elif escolha == '6':
            arquivo = input("Digite o nome do arquivo para carregar (ex: backup.json): ").strip()
            substituir = input("Substituir lista atual? (s/n): ").strip().lower() == 's'
            carregar_lista(arquivo, substituir)
        elif escolha == '7':
            zerar_lista()
        elif escolha == '8':
            operacoes_matrizes()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
