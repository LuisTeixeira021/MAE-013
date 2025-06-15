import array
import time

class PilhaCheiaErro(Exception):
    pass

class PilhaVaziaErro(Exception):
    pass

class TipoErro(Exception):
    pass

class Pilha:
    def __init__(self, tipo: str, capacidade: int):
        self.tipo = tipo  # 'i' para inteiro, 'u' para caractere
        self.capacidade = capacidade
        self._dados = array.array(tipo)
    
    def empilha(self, dado):
        if len(self._dados) >= self.capacidade:
            raise PilhaCheiaErro("A pilha está cheia.")
        if not isinstance(dado, int) and self.tipo == 'i':
            raise TipoErro("Tipo incorreto: esperado inteiro.")
        self._dados.append(dado)

    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro("A pilha está vazia.")
        return self._dados.pop()

    def pilha_esta_vazia(self):
        return len(self._dados) == 0

    def pilha_esta_cheia(self):
        return len(self._dados) >= self.capacidade

    def troca(self):
        if self.tamanho() < 2:
            raise PilhaVaziaErro("Não há elementos suficientes para trocar.")
        topo = self._dados.pop()
        abaixo_topo = self._dados.pop()
        self._dados.append(topo)
        self._dados.append(abaixo_topo)

    def tamanho(self):
        return len(self._dados)

    def visualizar(self, altura=5):
        print()
        for i in range(altura-1, -1, -1):
            for p in self._dados[::-1]:  # Discos maiores embaixo
                print(f"{'#' * p:^10}", end="  ")
                break
            else:
                print(f"{'|':^10}", end="  ")
        print("\n" + "-"*35)

    def get_disco(self, nivel):
        if nivel < self.tamanho():
            return self._dados[-nivel-1]
        else:
            return 0

def imprimir_pinos(pinos, altura, passo):
    print(f"\nPosição após {passo} passo(s):\n")
    for nivel in range(altura-1, -1, -1):
        for pino in pinos:
            disco = pino.get_disco(nivel)
            if disco:
                print(f"{'#' * disco:^10}", end="  ")
            else:
                print(f"{'|':^10}", end="  ")
        print()
    print("-" * 35)

def hanoi(n, origem, destino, auxiliar, pinos, altura, m, contador):
    if n == 1:
        disco = origem.desempilha()
        destino.empilha(disco)
        contador[0] += 1
        if contador[0] % m == 0 or contador[1]:
            imprimir_pinos(pinos, altura, contador[0])
            input("Pressione ENTER para continuar...")
        return

    hanoi(n - 1, origem, auxiliar, destino, pinos, altura, m, contador)
    disco = origem.desempilha()
    destino.empilha(disco)
    contador[0] += 1
    if contador[0] % m == 0 or contador[1]:
        imprimir_pinos(pinos, altura, contador[0])
        input("Pressione ENTER para continuar...")
    hanoi(n - 1, auxiliar, destino, origem, pinos, altura, m, contador)


# Execução principal


def main():
    try:
        n = int(input("Digite o número de discos: "))
        m = int(input("Quantidade M de passos entre visualizações (M=1 mostra cada passo): ") or 1)
        mostrar_inicial = input("Deseja mostrar o estado inicial? (s/n): ").strip().lower() == 's'
        
        pino_a = Pilha('i', n)
        pino_b = Pilha('i', n)
        pino_c = Pilha('i', n)

        for disco in range(n, 0, -1):
            pino_a.empilha(disco)

        pinos = [pino_a, pino_b, pino_c]
        altura = n
        if mostrar_inicial:
            imprimir_pinos(pinos, altura, 0)
            input("Pressione ENTER para iniciar...")

        contador = [0, m == 0]  # [número de passos, se deve mostrar o final mesmo que m=0]
        hanoi(n, pino_a, pino_c, pino_b, pinos, altura, m or 999999, contador)

        print(f"\nPosição final: {contador[0]} movimentos")
        imprimir_pinos(pinos, altura, contador[0])
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
