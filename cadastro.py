class Cadastro:
    def __init__(self):
        self.produtos=[]

    def obter_nome_produto(self):
        while True:
            nome=input("Insira o nome do produto:").strip()
            if nome:
                return nome
            print("O nome do produto é obrigatório")
    def obter_descricao(self):
        while True:
            descricao=input("Descrição do produto:").strip()
            if descricao:
                return descricao
            print("A descrição é obrigatório")
    def obter_valor(self):
        while True:
            try:
                valor=float(input("Valor do produto:"))
                if valor > 0:
                    return valor
                print("O valor deve ser maior que zero")
            except ValueError:
                print("Por favor insira um número valido")
    def obter_disponibilidade(self):
        while True:
           disponibilidade=input("O produto está disponivel para venda? (sim/não):").strip().lower()
           if disponibilidade in ["sim","não"]:
               return disponibilidade == "sim"
           print("Responta iválida, responda apenas com sim ou não")
    def cadastrar_produto(self):
        print("\n------Cadastro de produtos------")
        nome=self.obter_nome_produto()
        descricao=self.obter_descricao()
        valor=self.obter_valor()
        disponibilidade=self.obter_disponibilidade()

        #adicionar o produto como um dicionario na lista
        self.produtos.append({
            "nome": nome,
            "descricao":descricao,
            "valor":valor,
            "disponibilidade":disponibilidade
        })
        print("Produtos cadastrado com sucesso!")
        self.listar_produto()
         
    def listar_produto(self):
        print("\n--- Listagem de Produtos ---")
        print(f"{'Nome':<20}{'Valor':<10}")
        print("-" * 30)
        # Ordena os produtos pelo valor
        produtos_ordenados = sorted(self.produtos, key=lambda x: x["valor"])
        for produto in produtos_ordenados:
            print(f"{produto['nome']:<20}{produto['valor']:<10.2f}")
        print("-" * 30)
        self.menu()
    def menu(self):
        while True:
            print('\n [1] Cadastrar novo produto')
            print("[2] Sair da listagem")
            opcao=input("Esconha uma opção:").strip()

            if opcao == "1":
                self.cadastrar_produto()
                break
            elif opcao == "2":
                print("Voltando ao Menu principal...")
                break

cadastro=Cadastro()
cadastro.cadastrar_produto()
cadastro.listar_produto()
cadastro.menu()

    
