# Lista global para armazenar todos os produtos do estoque.
# Cada produto será um dicionário, e essa lista conterá vários desses dicionários.
estoque = []

def exibir_menu():
    """
    Exibe o menu principal de opções para o usuário.
    """
    print("\n--- Menu do Sistema de Estoque ---")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Excluir Produto")
    print("4. Visualizar Estoque")
    print("5. Sair do Sistema")
    print("---------------------------------")

def adicionar_produto():
    """
    Permite ao usuário adicionar um novo produto ao estoque.
    Solicita nome, preço e quantidade, e valida as entradas.
    Garanti que o nome do produto seja único.
    """
    print("\n--- Adicionar Novo Produto ---")

    # Loop para garantir que o nome do produto seja único.
    # Ele continua pedindo o nome até que um nome não existente seja digitado.
    while True:
        nome = input("Digite o nome do produto: ").strip() # .strip() remove espaços em branco extras do início/fim.
        
        # 'any()' verifica se ALGUM produto na lista 'estoque' tem o mesmo nome (ignorando maiúsculas/minúsculas).
        if any(p['nome'].lower() == nome.lower() for p in estoque):
            print(f"Produto '{nome}' já existe no estoque. Por favor, digite um nome único.")
        else:
            break # Se o nome for único, sai do loop.

    # Loop para garantir que o preço digitado seja um número positivo.
    while True:
        try:
            preco = float(input("Digite o preço do produto: R$ ")) # Converte a entrada para float (número decimal).
            if preco <= 0: # Valida se o preço é maior que zero.
                print("O preço deve ser um valor positivo.")
            else:
                break # Sai do loop se o preço for válido.
        except ValueError: # Captura erro se o usuário não digitar um número.
            print("Entrada inválida. Por favor, digite um número para o preço.")

    # Loop para garantir que a quantidade digitada seja um número inteiro não negativo.
    while True:
        try:
            quantidade = int(input("Digite a quantidade em estoque: ")) # Converte a entrada para int (número inteiro).
            if quantidade < 0: # Valida se a quantidade não é negativa.
                print("A quantidade não pode ser negativa.")
            else:
                break # Sai do loop se a quantidade for válida.
        except ValueError: # Captura erro se o usuário não digitar um número inteiro.
            print("Entrada inválida. Por favor, digite um número inteiro para a quantidade.")

    # Gera um código simples para o produto, útil para identificação interna,
    # mesmo que a busca principal seja pelo nome.
    codigo_gerado = f"PROD{len(estoque) + 1:03d}" # Ex: PROD001, PROD002, etc.

    # Cria um dicionário para o novo produto com as informações coletadas.
    novo_produto = {
        "nome": nome,
        "codigo": codigo_gerado,
        "preco": preco,
        "quantidade": quantidade
    }

    # Adiciona o dicionário do novo produto à lista 'estoque'.
    estoque.append(novo_produto)
    print(f"Produto '{nome}' adicionado ao estoque com sucesso!")

def atualizar_produto():
    """
    Permite ao usuário atualizar o preço e a quantidade de um produto existente.
    O produto é encontrado pelo nome.
    """
    print("\n--- Atualizar Produto Existente ---")
    
    # Verifica se o estoque está vazio antes de tentar atualizar.
    if not estoque:
        print("O estoque está vazio. Não há produtos para atualizar.")
        return # Sai da função.

    nome_busca = input("Digite o NOME do produto que deseja atualizar: ").strip()
    produto_encontrado = None # Variável para armazenar o dicionário do produto encontrado.

    # Percorre a lista de produtos para encontrar o produto pelo nome.
    for produto in estoque:
        # Compara o nome digitado com o nome do produto (ignorando maiúsculas/minúsculas para a busca).
        if produto['nome'].lower() == nome_busca.lower():
            produto_encontrado = produto # Se encontrou, armazena a referência ao dicionário.
            break # Sai do loop, pois o produto foi encontrado.

    if produto_encontrado:
        # Informa qual produto foi encontrado.
        print(f"\nProduto encontrado: {produto_encontrado['nome']} (Código: {produto_encontrado.get('codigo', 'N/A')})")
        print("Quais informações você deseja atualizar? (Preço e Quantidade)")

        # Loop para solicitar e validar o novo preço.
        while True:
            try:
                novo_preco = float(input(f"Novo preço (atual: R$ {produto_encontrado['preco']:.2f}): R$ "))
                if novo_preco <= 0:
                    print("O preço deve ser um valor positivo. Tente novamente.")
                else:
                    produto_encontrado['preco'] = novo_preco # Atualiza o preço no dicionário.
                    break
            except ValueError:
                print("Entrada inválida para o preço. Por favor, digite um número.")

        # Loop para solicitar e validar a nova quantidade.
        while True:
            try:
                nova_quantidade = int(input(f"Nova quantidade (atual: {produto_encontrado['quantidade']}): "))
                if nova_quantidade < 0:
                    print("A quantidade não pode ser negativa. Tente novamente.")
                else:
                    produto_encontrado['quantidade'] = nova_quantidade # Atualiza a quantidade no dicionário.
                    break
            except ValueError:
                print("Entrada inválida para a quantidade. Por favor, digite um número inteiro.")

        print(f"Produto '{produto_encontrado['nome']}' atualizado com sucesso!")
    else:
        print(f"Produto com nome '{nome_busca}' não encontrado no estoque.")

def excluir_produto():
    """
    Permite ao usuário excluir um produto do estoque.
    O produto é encontrado e removido pelo nome.
    """
    print("\n--- Excluir Produto ---")
    
    # Verifica se o estoque está vazio antes de tentar excluir.
    if not estoque:
        print("O estoque está vazio. Não há produtos para excluir.")
        return # Sai da função.

    nome_busca = input("Digite o NOME do produto que deseja excluir: ").strip()
    
    indice_para_remover = -1 # Variável para armazenar o índice do produto a ser removido.
    # 'enumerate' é usado para obter tanto o índice (i) quanto o item (produto) da lista.
    for i, produto in enumerate(estoque):
        # Compara o nome digitado com o nome do produto (ignorando maiúsculas/minúsculas).
        if produto['nome'].lower() == nome_busca.lower():
            indice_para_remover = i # Armazena o índice do produto encontrado.
            break # Sai do loop.
    
    if indice_para_remover != -1: # Se um produto foi encontrado (índice diferente de -1).
        # 'pop()' remove o item da lista pelo seu índice e retorna o item removido.
        produto_removido_info = estoque.pop(indice_para_remover)
        print(f"Produto '{produto_removido_info['nome']}' (Código: {produto_removido_info.get('codigo', 'N/A')}) removido do estoque com sucesso!")
    else:
        print(f"Produto com nome '{nome_busca}' não encontrado no estoque.")

def visualizar_estoque():
    """
    Exibe a lista de todos os produtos atualmente no estoque.
    Mostra nome, preço e quantidade.
    """
    print("\n--- Visualizar Estoque ---")
    
    # Verifica se o estoque está vazio.
    if not estoque:
        print("O estoque está vazio. Adicione alguns produtos primeiro.")
        return # Sai da função.

    print("\n--- Produtos em Estoque ---")
    # Percorre cada dicionário de produto na lista 'estoque'.
    for produto in estoque:
        # Acessa e imprime as informações específicas de cada produto.
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}") # Formata o preço para 2 casas decimais.
        print(f"Quantidade: {produto['quantidade']}")
        print("---------------------------")


def main():
    """
    Função principal que controla o fluxo do sistema.
    Exibe o menu e direciona para as funções apropriadas com base na escolha do usuário.
    """
    while True: # Loop infinito para manter o sistema rodando até que o usuário escolha sair.
        exibir_menu() # Chama a função para mostrar o menu.
        opcao = input("Escolha uma opção: ") # Pede ao usuário para escolher uma opção.

        # Estruturas condicionais (if/elif/else) para controlar o fluxo do programa.
        if opcao == '1':
            adicionar_produto() # Chama a função de adicionar produto.
        elif opcao == '2':
            atualizar_produto() # Chama a função de atualizar produto.
        elif opcao == '3':
            excluir_produto() # Chama a função de excluir produto.
        elif opcao == '4':
            visualizar_estoque() # Chama a função de visualizar estoque.
        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break # Sai do loop 'while True', encerrando o programa.
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

# Garante que a função 'main()' seja chamada apenas quando o script for executado diretamente.
if __name__ == "__main__":
    main()
