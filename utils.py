from datetime import datetime


def next_id(products):          #gerar próximo ID para produtos ou movimentações
    if not products:
        return 1
    return max(product['id'] for product in products) + 1



def find_product_by_id(products, product_id):      #função auxiliar para encontrar produto por ID
    for product in products:
        if product['id'] == product_id:
            return product
    return None



def list_products(products):   # Listar produtos (relatório)
    if not products:
        print("Nenhum produto cadastrado.")
        return
    print("ID | Nome | Categoria | Preço | Estoque ")
    print("-------------------")
    for product in products:
        print(f"{product['id']} | {product['name']} | {product['category']} | R${product['price']:.2f} | {product['stock']}")

    print("deseja listar os produtos por nome?")
    choice = input("Digite 's' para sim ou 'n' para não: ")
    if choice == 's':
        sorted_products = sorted(products, key=lambda p: p['name'])
        print("ID | Nome | Categoria | Preço | Estoque ")
        print("-------------------")
        for product in sorted_products:
            print(f"{product['id']} | {product['name']} | {product['category']} | R${product['price']:.2f} | {product['stock']}")



def register_product(products):         #cadastrar produto
    
    name = input("Nome do produto: ")
    category = input("Categoria do produto: ")
    price = ler_float_validado("Preço do produto: ")
    stock = ler_int_validado("Quantidade em estoque: ")
    product_id = next_id(products)
    new_product = {
        'id': product_id,
        'name': name,
        'category': category,
        'price': price,
        'stock': stock
    }
    products.append(new_product)
    print(f"Produto '{name}' cadastrado com ID {product_id}.")



def search_product(products):       #buscar produto por nome
    search_term = input("Digite o nome ou categoria do produto para buscar: ").lower()
    found_products = [p for p in products if search_term in p['name'].lower() or search_term in p['category'].lower()]
    if not found_products:
        print("Nenhum produto encontrado.")
        return
    print("ID | Nome | Categoria | Preço | Estoque ")
    print("-------------------")
    for product in found_products:
        print(f"{product['id']} | {product['name']} | {product['category']} | R${product['price']:.2f} | {product['stock']}")



def register_stock_entry(products, stock_movements):        #registrar entrada de estoque
    product_id = ler_int_validado("ID do produto para entrada de estoque: ")
    product = find_product_by_id(products, product_id)
    if not product:
        print("Produto não encontrado.")
        return
    quantity = ler_int_validado("Quantidade a adicionar: ")
    product['stock'] += quantity
    stock_movements.append({
        'id': next_id(stock_movements),
        'product_id': product_id,
        'type': 'entrada',
        'quantity': quantity,   
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'observant': input("Observação (opcional): ")
    })
    print(f"Entrada de {quantity} unidades registrada para o produto '{product['name']}'.")



def register_stock_exit(products, stock_movements):     #registrar saída de estoque
    product_id = ler_int_validado("ID do produto para saída de estoque: ")
    product = find_product_by_id(products, product_id)
    if not product:
        print("Produto não encontrado.")
        return
    quantity = ler_int_validado("Quantidade a remover: ")
    if quantity > product['stock']:
        print("Quantidade insuficiente em estoque.")
        return
    product['stock'] -= quantity
    stock_movements.append({
        'id': next_id(stock_movements),
        'product_id': product_id,
        'type': 'saída',
        'quantity': quantity,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'observant': input("Observação (opcional): ")
    })
    print(f"Saída de {quantity} unidades registrada para o produto '{product['name']}'.")



def report_stock_movements(stock_movements):        #relatório de movimentações
    if not stock_movements:
        print("Nenhuma movimentação de estoque registrada.")
        return
    print("ID Produto | Tipo | Quantidade | Data | Observação")
    print("-------------------")
    for movement in stock_movements:
        print(f"{movement['product_id']} | {movement['type']} | {movement['quantity']} | {movement['date']} | {movement['observant']}")
    



def managerial_report(products, stock_movements):       #relatório gerencial, precisa complementar com mais informações
    total_products = len(products)
    total_stock = sum(p['stock'] for p in products)
    total_entries = sum(m['quantity'] for m in stock_movements if m['type'] == 'entrada')
    total_exits = sum(m['quantity'] for m in stock_movements if m['type'] == 'saída')
    plus_products_max = max(p['stock']for p in products)
    plus_products_min = min(p['stock'] for p in products)
    values_total = sum(p['price'] * p['stock'] for p in products)
    qtd_categories_produtos = {}
    for p in products:
        if p['category'] not in qtd_categories_produtos:
            qtd_categories_produtos[p['category']] = 0
        qtd_categories_produtos[p['category']] += 1 
    top_pro_price_stock = sorted(products, key=lambda p: p['price'] * p['stock'], reverse=True)[:5]        

    print("Relatório Gerencial:")
    print(f"Total de produtos cadastrados: {total_products}")
    print(f"Total em estoque: {total_stock}")
    print(f"Total de entradas de estoque: {total_entries}")
    print(f"Total de saídas de estoque: {total_exits}")
    print(f"Produto com maior estoque: {plus_products_max}")
    print(f"Produto com menor estoque: {plus_products_min}")
    print(f"Valor total do estoque: R${values_total:.2f}")
    print("Quantidade de produtos por categoria:")
    for category, count in qtd_categories_produtos.items():
        print(f"  {category}: {count} produtos")
    print("Top 5 produtos por valor total em estoque:")
    for product in top_pro_price_stock:
        print(f"  {product['name']} (ID: {product['id']}): R${product['price'] * product['stock']:.2f}")
    print("Deseja exportar o relatório gerencial para um arquivo TXT?")
    choice = input("Digite 's' para sim ou 'n' para não: ")
    if choice == 's':
        export_TXT_gerencial(products, stock_movements, 'relatorio_gerencial.txt')

        



def ler_int_validado(prompt):       #validar entrada de número inteiro
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite um número inteiro válido.")



def ler_float_validado(prompt):         


            #validar entrada de número decimal
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Digite um número decimal válido.")







def export_TXT_gerencial(products, stock_movements, file_path):         #exportar relatório gerencial em formato TXT, precisa ajustar algumas coisas, pois ele não está exportando as informações do relatório, apenas a lista de produtos
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("ID | Nome | Categoria | Preço | Estoque \n")
        f.write("-------------------\n")
        for product in products:
            f.write(f"{product['id']} | {product['name']} | {product['category']} | R${product['price']:.2f} | {product['stock']}\n")
            
    print(f"Relatório exportado para {file_path}.")