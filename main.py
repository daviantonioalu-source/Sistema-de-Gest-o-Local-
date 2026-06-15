#English - Function that import functions from arquive "functions"...
#Português - Função de importação das funções do arquivo "functions"...
from functions import (
    search_product_by_id,
    register_product,
    list_products,
    search_product,
    register_stock_entry,
    register_stock_exit,
    report_stock_movements,
    managerial_report,
    update_product,
)

#English - Function that import functions from arquive "storage"...
#Português - Função de importação das funções do arquivo "storage"...
from storage import save_json, load_json

#English - Start with the variables...
#Português - Inicia ás variaveis...
products = load_json("products.json") or []
stock_movements = load_json("stock_movements.json") or []

#English - Show the main menu for the user...
#Português - Mostra o menu principal para usuário...
while True:
    print("→ Sistema de Gestão Local ←")
    print("1 - Cadastrar Produto;")
    print("2 - Fazer Alteração de Produto;")
    print("3 - Buscar Produto Por ID;")
    print("4 - Buscar Produto Por Nome ou Categoria;")
    print("5 - Relatório de Produtos;")
    print("6 - Registrar Entrada de Estoque;")
    print("7 - Registrar Saída de Estoque;")
    print("8 - Relatório de Movimentações;")
    print("9 - Relatório Gerencial;")
    print("0 - Salvar e Sair...")
    try:
        option = int(input("Escolha uma Ação: ").strip())
    except ValueError:
        print("Digite Apenas Números!")
        continue

#English - Main menu's options...
#Português - Opções do menu principal...
    match option:
        case 1:
            register_product(products)
        case 2:
            update_product(products)
        case 3:
            search_product_by_id(products)
        case 4:
            search_product(products)
        case 5:
            list_products(products)
        case 6:
            register_stock_entry(products, stock_movements)
        case 7: 
            register_stock_exit(products, stock_movements)
        case 8:
            report_stock_movements(products, stock_movements)
        case 9:
            managerial_report(products, stock_movements)
        case 0:
            save_json(products, "products.json")
            save_json(stock_movements, "stock_movements.json")
            print("Informações Salvas! Saíndo do Sistema...")
            break
        case _:
            print("Opção Inválida! Tente Novamente...")