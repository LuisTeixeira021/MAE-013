class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __repr__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Pilha:
    def __init__(self, iterable=None):
        self.dados = []
        if iterable:
            self.dados.extend(iterable)

    def length(self):
        return len(self.dados)

    def is_empty(self):
        return len(self.dados) == 0

    def is_full(self):
        return False  # Sem limite por enquanto

    # Push insere no fim (topo)
    def inserir_fim(self, item):
        self.dados.append(item)

    # Pop remove do fim (topo)
    def remover_fim(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")
        return self.dados.pop()

    # Consultar topo (fim)
    def consultar_fim(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")
        return self.dados[-1]

    # Troca elementos adjacentes no fim
    def trocar(self, pos):
        if pos < 0 or pos >= self.length() - 1:
            raise IndexError("Posição inválida para troca na pilha")
        self.dados[pos], self.dados[pos+1] = self.dados[pos+1], self.dados[pos]

    # Inserções/remover no início não fazem sentido aqui
    def inserir_inicio(self, item):
        raise NotImplementedError("Operação inválida para pilha")

    def remover_inicio(self):
        raise NotImplementedError("Operação inválida para pilha")

    def remover_i(self, i):
        raise NotImplementedError("Operação inválida para pilha")

    def consultar_inicio(self):
        raise NotImplementedError("Operação inválida para pilha")

    def consultar_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        return self.dados[i]

    def inserir_i(self, i, item):
        if i < 0 or i > self.length():
            raise IndexError("Índice fora do intervalo")
        self.dados.insert(i, item)


class Fila:
    def __init__(self, iterable=None):
        self.dados = []
        if iterable:
            self.dados.extend(iterable)

    def length(self):
        return len(self.dados)

    def is_empty(self):
        return len(self.dados) == 0

    def is_full(self):
        return False

    # Inserir no fim (fim da fila)
    def inserir_fim(self, item):
        self.dados.append(item)

    # Remover do início (frente da fila)
    def remover_inicio(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self.dados.pop(0)

    # Consultar início
    def consultar_inicio(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self.dados[0]

    # Consultar fim
    def consultar_fim(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self.dados[-1]

    # Trocar elementos adjacentes
    def trocar(self, pos):
        if pos < 0 or pos >= self.length() - 1:
            raise IndexError("Posição inválida para troca na fila")
        self.dados[pos], self.dados[pos+1] = self.dados[pos+1], self.dados[pos]

    # Inserções/remover em posições específicas (simples)
    def inserir_inicio(self, item):
        self.dados.insert(0, item)

    def remover_fim(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self.dados.pop()

    def remover_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        return self.dados.pop(i)

    def consultar_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        return self.dados[i]

    def inserir_i(self, i, item):
        if i < 0 or i > self.length():
            raise IndexError("Índice fora do intervalo")
        self.dados.insert(i, item)


class Array:
    def __init__(self, capacidade, iterable=None):
        self.capacidade = capacidade
        self.dados = []
        if iterable:
            for item in iterable:
                if len(self.dados) < capacidade:
                    self.dados.append(item)
                else:
                    break

    def length(self):
        return len(self.dados)

    def is_empty(self):
        return len(self.dados) == 0

    def is_full(self):
        return len(self.dados) >= self.capacidade

    def inserir_inicio(self, item):
        if self.is_full():
            raise OverflowError("Array cheio")
        self.dados.insert(0, item)

    def inserir_fim(self, item):
        if self.is_full():
            raise OverflowError("Array cheio")
        self.dados.append(item)

    def inserir_i(self, i, item):
        if self.is_full():
            raise OverflowError("Array cheio")
        if i < 0 or i > self.length():
            raise IndexError("Índice fora do intervalo")
        self.dados.insert(i, item)

    def remover_inicio(self):
        if self.is_empty():
            raise IndexError("Array vazio")
        return self.dados.pop(0)

    def remover_fim(self):
        if self.is_empty():
            raise IndexError("Array vazio")
        return self.dados.pop()

    def remover_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        return self.dados.pop(i)

    def consultar_inicio(self):
        if self.is_empty():
            raise IndexError("Array vazio")
        return self.dados[0]

    def consultar_fim(self):
        if self.is_empty():
            raise IndexError("Array vazio")
        return self.dados[-1]

    def consultar_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        return self.dados[i]

    def trocar(self, pos):
        if pos < 0 or pos >= self.length() - 1:
            raise IndexError("Posição inválida para troca no array")
        self.dados[pos], self.dados[pos+1] = self.dados[pos+1], self.dados[pos]


class NoSimples:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaSimples:
    def __init__(self, iterable=None):
        self.inicio = None
        if iterable:
            for item in iterable:
                self.inserir_fim(item)

    def length(self):
        count = 0
        atual = self.inicio
        while atual:
            count += 1
            atual = atual.proximo
        return count

    def is_empty(self):
        return self.inicio is None

    def is_full(self):
        return False

    def inserir_inicio(self, item):
        novo = NoSimples(item)
        novo.proximo = self.inicio
        self.inicio = novo

    def inserir_fim(self, item):
        novo = NoSimples(item)
        if self.is_empty():
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def inserir_i(self, i, item):
        if i < 0 or i > self.length():
            raise IndexError("Índice fora do intervalo")
        if i == 0:
            self.inserir_inicio(item)
            return
        atual = self.inicio
        for _ in range(i - 1):
            atual = atual.proximo
        novo = NoSimples(item)
        novo.proximo = atual.proximo
        atual.proximo = novo

    def remover_inicio(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        rem = self.inicio.dado
        self.inicio = self.inicio.proximo
        return rem

    def remover_fim(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        if self.inicio.proximo is None:
            rem = self.inicio.dado
            self.inicio = None
            return rem
        atual = self.inicio
        while atual.proximo.proximo:
            atual = atual.proximo
        rem = atual.proximo.dado
        atual.proximo = None
        return rem

    def remover_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        if i == 0:
            return self.remover_inicio()
        atual = self.inicio
        for _ in range(i - 1):
            atual = atual.proximo
        rem = atual.proximo.dado
        atual.proximo = atual.proximo.proximo
        return rem

    def consultar_inicio(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        return self.inicio.dado

    def consultar_fim(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        atual = self.inicio
        while atual.proximo:
            atual = atual.proximo
        return atual.dado

    def consultar_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        atual = self.inicio
        for _ in range(i):
            atual = atual.proximo
        return atual.dado

    def trocar(self, pos):
        if pos < 0 or pos >= self.length() - 1:
            raise IndexError("Posição inválida para troca na lista simples")
        if pos == 0:
            primeiro = self.inicio
            segundo = primeiro.proximo
            primeiro.proximo = segundo.proximo
            segundo.proximo = primeiro
            self.inicio = segundo
            return
        atual = self.inicio
        for _ in range(pos - 1):
            atual = atual.proximo
        primeiro = atual.proximo
        segundo = primeiro.proximo
        primeiro.proximo = segundo.proximo
        segundo.proximo = primeiro
        atual.proximo = segundo

    def __repr__(self):
        return "[" + ", ".join(str(dado) for dado in self) + "]"

    def __iter__(self):
        atual = self.inicio
        while atual:
            yield atual.dado
            atual = atual.proximo


class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class ListaDupla:
    def __init__(self, iterable=None):
        self.inicio = None
        self.fim = None
        if iterable:
            for item in iterable:
                self.inserir_fim(item)

    def length(self):
        count = 0
        atual = self.inicio
        while atual:
            count += 1
            atual = atual.proximo
        return count

    def is_empty(self):
        return self.inicio is None

    def is_full(self):
        return False

    def inserir_inicio(self, item):
        novo = NoDuplo(item)
        if self.is_empty():
            self.inicio = self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def inserir_fim(self, item):
        novo = NoDuplo(item)
        if self.is_empty():
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo

    def inserir_i(self, i, item):
        if i < 0 or i > self.length():
            raise IndexError("Índice fora do intervalo")
        if i == 0:
            self.inserir_inicio(item)
            return
        if i == self.length():
            self.inserir_fim(item)
            return
        atual = self.inicio
        for _ in range(i):
            atual = atual.proximo
        novo = NoDuplo(item)
        anterior = atual.anterior
        anterior.proximo = novo
        novo.anterior = anterior
        novo.proximo = atual
        atual.anterior = novo

    def remover_inicio(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        rem = self.inicio.dado
        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        return rem

    def remover_fim(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        rem = self.fim.dado
        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        return rem

    def remover_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        if i == 0:
            return self.remover_inicio()
        if i == self.length() - 1:
            return self.remover_fim()
        atual = self.inicio
        for _ in range(i):
            atual = atual.proximo
        rem = atual.dado
        anterior = atual.anterior
        proximo = atual.proximo
        anterior.proximo = proximo
        proximo.anterior = anterior
        return rem

    def consultar_inicio(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        return self.inicio.dado

    def consultar_fim(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        return self.fim.dado

    def consultar_i(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Índice fora do intervalo")
        atual = self.inicio
        for _ in range(i):
            atual = atual.proximo
        return atual.dado

    def trocar(self, pos):
        if pos < 0 or pos >= self.length() - 1:
            raise IndexError("Posição inválida para troca na lista dupla")
        if pos == 0:
            primeiro = self.inicio
            segundo = primeiro.proximo
            primeiro.proximo = segundo.proximo
            if segundo.proximo:
                segundo.proximo.anterior = primeiro
            segundo.proximo = primeiro
            segundo.anterior = None
            primeiro.anterior = segundo
            self.inicio = segundo
            if primeiro.proximo is None:
                self.fim = primeiro
            return
        atual = self.inicio
        for _ in range(pos - 1):
            atual = atual.proximo
        primeiro = atual.proximo
        segundo = primeiro.proximo
        primeiro.proximo = segundo.proximo
        if segundo.proximo:
            segundo.proximo.anterior = primeiro
        segundo.proximo = primeiro
        segundo.anterior = atual
        primeiro.anterior = segundo
        atual.proximo = segundo
        if primeiro.proximo is None:
            self.fim = primeiro

    def __repr__(self):
        return "[" + ", ".join(str(dado) for dado in self) + "]"

    def __iter__(self):
        atual = self.inicio
        while atual:
            yield atual.dado
            atual = atual.proximo

# === Menu geral ===

def menu_estrutura(estrutura, nome):
    while True:
        print(f"\n--- Menu {nome} ---")
        print("1. Inserir no início")
        print("2. Inserir no fim")
        print("3. Inserir na posição i")
        print("4. Remover do início")
        print("5. Remover do fim")
        print("6. Remover da posição i")
        print("7. Consultar início")
        print("8. Consultar fim")
        print("9. Consultar posição i")
        print("10. Trocar elementos adjacentes")
        print("11. Mostrar todos")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                nome_p = input("Nome: ")
                cpf = input("CPF: ")
                pessoa = Pessoa(nome_p, cpf)
                estrutura.inserir_inicio(pessoa)

            elif opcao == '2':
                nome_p = input("Nome: ")
                cpf = input("CPF: ")
                pessoa = Pessoa(nome_p, cpf)
                estrutura.inserir_fim(pessoa)

            elif opcao == '3':
                pos = int(input("Posição i: "))
                nome_p = input("Nome: ")
                cpf = input("CPF: ")
                pessoa = Pessoa(nome_p, cpf)
                estrutura.inserir_i(pos, pessoa)

            elif opcao == '4':
                rem = estrutura.remover_inicio()
                print(f"Removido: {rem}")

            elif opcao == '5':
                rem = estrutura.remover_fim()
                print(f"Removido: {rem}")

            elif opcao == '6':
                pos = int(input("Posição i para remover: "))
                rem = estrutura.remover_i(pos)
                print(f"Removido: {rem}")

            elif opcao == '7':
                print(f"Início: {estrutura.consultar_inicio()}")

            elif opcao == '8':
                print(f"Fim: {estrutura.consultar_fim()}")

            elif opcao == '9':
                pos = int(input("Posição i para consultar: "))
                print(f"Item na posição {pos}: {estrutura.consultar_i(pos)}")

            elif opcao == '10':
                pos = int(input("Posição para troca (posição inicial do par): "))
                estrutura.trocar(pos)
                print("Troca feita.")

            elif opcao == '11':
                print("Conteúdo:", estrutura)

            elif opcao == '0':
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    pilha = Pilha()
    fila = Fila()
    array = Array(50)
    lista_simples = ListaSimples()
    lista_dupla = ListaDupla()

    while True:
        print("\n=== Menu Principal ===")
        print("1. Pilha")
        print("2. Fila")
        print("3. Array")
        print("4. Lista Encadeada Simples")
        print("5. Lista Encadeada Dupla")
        print("0. Sair")

        escolha = input("Escolha uma estrutura: ")

        if escolha == '1':
            menu_estrutura(pilha, "Pilha")
        elif escolha == '2':
            menu_estrutura(fila, "Fila")
        elif escolha == '3':
            menu_estrutura(array, "Array")
        elif escolha == '4':
            menu_estrutura(lista_simples, "Lista Simples")
        elif escolha == '5':
            menu_estrutura(lista_dupla, "Lista Dupla")
        elif escolha == '0':
            print("Até mais!")
            break
        else:
            print("Opção inválida.")
