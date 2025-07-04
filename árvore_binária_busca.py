from dataclasses import dataclass

# -------------------------------
# Classe Registro
# -------------------------------
@dataclass
class Registro:
    cpf: str
    nome: str
    data_nasc: str
    deletado: bool = False  # flag para indicar se o registro foi deletado

    def __lt__(self, outro):
        return self.cpf < outro.cpf

    def __eq__(self, outro):
        return self.cpf == outro.cpf

    def __str__(self):
        return f"{self.cpf} - {self.nome} - {self.data_nasc}" if not self.deletado else "REGISTRO DELETADO"


# -------------------------------
# Nó da Árvore Binária de Busca
# -------------------------------
class NoABB:
    def __init__(self, chave, indice):
        self.chave = chave
        self.indice = indice
        self.esq = None
        self.dir = None


# -------------------------------
# Classe ABB
# -------------------------------
class ABB:
    def __init__(self, iterable=None):
        self.raiz = None
        if iterable:
            for chave, indice in iterable:
                self.inserir(chave, indice)

    def inserir(self, chave, indice):
        def _inserir(no, chave, indice):
            if no is None:
                return NoABB(chave, indice)
            elif chave < no.chave:
                no.esq = _inserir(no.esq, chave, indice)
            elif chave > no.chave:
                no.dir = _inserir(no.dir, chave, indice)
            return no
        self.raiz = _inserir(self.raiz, chave, indice)

    def buscar(self, chave):
        def _buscar(no, chave):
            if no is None:
                return None
            elif chave == no.chave:
                return no.indice
            elif chave < no.chave:
                return _buscar(no.esq, chave)
            else:
                return _buscar(no.dir, chave)
        return _buscar(self.raiz, chave)

    def remover(self, chave):
        def _remover(no, chave):
            if no is None:
                return None
            if chave < no.chave:
                no.esq = _remover(no.esq, chave)
            elif chave > no.chave:
                no.dir = _remover(no.dir, chave)
            else:
                if no.esq and no.dir:
                    sucessor = self._minimo(no.dir)
                    no.chave, no.indice = sucessor.chave, sucessor.indice
                    no.dir = _remover(no.dir, sucessor.chave)
                else:
                    no = no.esq if no.esq else no.dir
            return no
        self.raiz = _remover(self.raiz, chave)

    def _minimo(self, no):
        while no.esq:
            no = no.esq
        return no

    def em_ordem(self):
        resultado = []
        def _em_ordem(no):
            if no:
                _em_ordem(no.esq)
                resultado.append((no.chave, no.indice))
                _em_ordem(no.dir)
        _em_ordem(self.raiz)
        return resultado


# -------------------------------
# Classe BaseDeDados
# -------------------------------
class BaseDeDados:
    def __init__(self):
        self.registros = []
        self.indice = ABB()

    def inserir_registro(self, registro: Registro):
        self.registros.append(registro)
        pos = len(self.registros) - 1
        self.indice.inserir(registro.cpf, pos)

    def buscar_por_cpf(self, cpf):
        indice = self.indice.buscar(cpf)
        if indice is not None:
            return self.registros[indice]
        return None

    def deletar_por_cpf(self, cpf):
        indice = self.indice.buscar(cpf)
        if indice is not None:
            self.registros[indice].deletado = True
            self.indice.remover(cpf)

    def listar_registros_ordenados(self):
        ordenados = []
        for chave, indice in self.indice.em_ordem():
            ordenados.append(self.registros[indice])
        return ordenados

# -------------------------------
# Interface Interativa via Terminal
# -------------------------------

def menu():
    bd = BaseDeDados()
    while True:
        print("\n--- MENU ---")
        print("1. Inserir novo registro")
        print("2. Buscar registro por CPF")
        print("3. Deletar registro por CPF")
        print("4. Listar registros ordenados por CPF")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data = input("Data de nascimento (D-M-A): ")
            bd.inserir_registro(Registro(cpf, nome, data))
            print("Registro inserido com sucesso.")
        elif opcao == '2':
            cpf = input("CPF para buscar: ")
            reg = bd.buscar_por_cpf(cpf)
            print(f"Resultado: {reg}" if reg else "Registro não encontrado.")
        elif opcao == '3':
            cpf = input("CPF para deletar: ")
            bd.deletar_por_cpf(cpf)
            print("Registro deletado, se existia.")
        elif opcao == '4':
            print("\nRegistros ordenados:")
            for r in bd.listar_registros_ordenados():
                print(r)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


# -------------------------------
# Interface Interativa via Terminal
# -------------------------------

def menu():
    bd = BaseDeDados()
    while True:
        print("\n--- MENU ---")
        print("1. Inserir novo registro")
        print("2. Buscar registro por CPF")
        print("3. Deletar registro por CPF")
        print("4. Listar registros ordenados por CPF")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data = input("Data de nascimento (D-M-A): ")
            bd.inserir_registro(Registro(cpf, nome, data))
            print("Registro inserido com sucesso.")
        elif opcao == '2':
            cpf = input("CPF para buscar: ")
            reg = bd.buscar_por_cpf(cpf)
            print(f"Resultado: {reg}" if reg else "Registro não encontrado.")
        elif opcao == '3':
            cpf = input("CPF para deletar: ")
            bd.deletar_por_cpf(cpf)
            print("Registro deletado, se existia.")
        elif opcao == '4':
            print("\nRegistros ordenados:")
            for r in bd.listar_registros_ordenados():
                print(r)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Rodar o menu se for o script principal
if __name__ == "__main__":
    menu()
