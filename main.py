
from utils import (
register_product ,
list_products, 
search_product, 
register_stock_entry,
register_stock_exit, 
report_stock_movements,
managerial_report
)

from storage import save_json, load_json

products = load_json('products.json') or []
stock_movements = load_json('stock_movements.json') or []


while True:
    print("\n -->> SGL <<--:")
    print("1. Cadastrar produto")
    print("2. Listar produtos (relatório)")
    print("3. Buscar produto por nome")
    print("4. Registrar ENTRADA de estoque")    
    print("5. Registrar SAÍDA de estoque ")
    print("6. Relatório de movimentações ")
    print("7. Relatório gerencial")
    print("8. Salvar e sair")
    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números.")
        continue


    match op:
        case 1:
            register_product(products)
        case 2:
            list_products(products)
        case 3:
            search_product(products)
        case 4:
            register_stock_entry(products, stock_movements)
        case 5:
            register_stock_exit(products, stock_movements)
        case 6:
            report_stock_movements(stock_movements)
        case 7:
            managerial_report(products, stock_movements)
        case 8:
            save_json(products, 'products.json')
            save_json(stock_movements, 'stock_movements.json')
            print("Dados salvos. Saindo...")
            break
        case _:
            print("Opção inválida. Tente novamente.")

            
