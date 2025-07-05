import csv
from typing import Callable

class TabelaHash:
    def __init__(self, tamanho=100, funcao_hash: Callable = None):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]  # encadeamento exterior
        self.funcao_hash = funcao_hash or self.hash_divisao

    def hash_divisao(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, dado):
        indice = self.funcao_hash(chave)
        for k, _ in self.tabela[indice]:
            if k == chave:
                return False  # duplicata detectada
        self.tabela[indice].append((chave, dado))
        return True

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        return None

    def remover(self, chave):
        indice = self.funcao_hash(chave)
        for i, (k, _) in enumerate(self.tabela[indice]):
            if k == chave:
                del self.tabela[indice][i]
                return True
        return False

    def __getitem__(self, chave):
        return self.buscar(chave)

    def __setitem__(self, chave, valor):
        self.inserir(chave, valor)

    def __delitem__(self, chave):
        self.remover(chave)

    def elementos(self):
        for lista in self.tabela:
            for _, v in lista:
                yield v


# ===================== Função de deduplicação =====================

def deduplicar_csv(arquivo_csv, chave_func):
    tabela = TabelaHash(tamanho=200)
    dados_unicos = []

    with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            chave = chave_func(linha)
            if tabela.inserir(chave, linha):
                dados_unicos.append(linha)

    return dados_unicos

# ===================== Menu Interativo =====================

def menu():
    arquivo = "dados.csv"
    tabela = None
    dados_deduplicados = []

    while True:
        print("\n==== MENU ====")
        print("1 - Gerar CSV de exemplo")
        print("2 - Deduplicar dados (usando CPF como chave)")
        print("3 - Mostrar dados únicos")
        print("4 - Buscar por CPF")
        print("5 - Remover por CPF")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            with open(arquivo, "w", newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerow(["nome", "cpf", "ano"])
                escritor.writerow(["Alice", "13226251740", "2023"])
                escritor.writerow(["Bob", "22222222222", "2022"])
                escritor.writerow(["Alice", "11111111111", "2023"])  # duplicata
                escritor.writerow(["Carlos", "33333333333", "2023"])
            print("CSV de exemplo gerado.")

        elif opcao == "2":
            dados_deduplicados = deduplicar_csv(arquivo, chave_func=lambda linha: linha["cpf"])
            tabela = TabelaHash(tamanho=200)
            for linha in dados_deduplicados:
                tabela.inserir(linha["cpf"], linha)
            print("Deduplicação concluída.")

        elif opcao == "3":
            if not tabela:
                print("Você precisa deduplicar os dados primeiro (opção 2).")
            else:
                print("\nDados únicos:")
                for dado in tabela.elementos():
                    print(dado)

        elif opcao == "4":
            if not tabela:
                print("Deduplica primeiro! (opção 2)")
            else:
                cpf = input("Digite o CPF para buscar: ").strip()
                resultado = tabela.buscar(cpf)
                if resultado:
                    print("Encontrado:", resultado)
                else:
                    print("CPF não encontrado.")

        elif opcao == "5":
            if not tabela:
                print("Deduplica primeiro! (opção 2)")
            else:
                cpf = input("Digite o CPF para remover: ")
                if tabela.remover(cpf):
                    print("Removido com sucesso.")
                else:
                    print("CPF não encontrado.")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
