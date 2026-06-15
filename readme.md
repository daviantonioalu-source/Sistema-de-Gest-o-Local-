O presente trabalho segue a organização e divisão da seguinte forma:

main.py ➔ Arquivo principal. Contém o menu interativo e controla o fluxo de execução do programa.
functions.py ➔ Contém a lógica de negócio (cadastro, buscas, geração de relatórios e exportações para TXT).
storage.py ➔ Responsável pela comunicação com o disco rígido (carregar e salvar os arquivos JSON).
products.json ➔ (Gerado automaticamente) Banco de dados local que armazena os produtos cadastrados.
stock_movements.json ➔ (Gerado automaticamente) Banco de dados local que armazena o histórico de entradas e saídas.
*.txt ➔ (Gerados sob demanda) Relatórios exportados pelo usuário.

Casos de Teste (Entrada → Saída Esperada)

Teste 1: Cadastro de Produto com Validação
Ação: Tentar cadastrar um produto com valor negativo.
Entrada: Nome: Teclado | Categoria: Eletrônicos | Preço: -50
Saída Esperada: O sistema bloqueia a ação, exibe a mensagem "O valor Não Pode Ser Negativo! Tente Novamente." e pede a digitação do preço novamente.

Teste 2: Busca Robusta (Ignorando Espaços e Maiúsculas)
Ação: Pesquisar um produto usando formatação "suja".
Entrada: Termo de pesquisa: teCLado 
Saída Esperada: O sistema limpa os espaços (.strip()), converte para minúsculo (.lower()) e exibe perfeitamente a ficha do produto "Teclado".

Teste 3: Movimentação de Saída (Controle de Estoque)
Ação: Retirar itens do estoque.
Entrada: ID do Produto: 1 | Tipo: Saída | Quantidade: 5 | Observação: Venda balcão
Saída Esperada: A quantidade do produto ID 1 cai em 5 unidades. O arquivo stock_movements.json recebe um novo registro, e o arquivo products.json é atualizado.

Teste 4: Busca Estrita pelo ID
Ação: Pesquisar o produto de ID 1 (garantindo que não traga o ID 10 junto).
Entrada: Termo de pesquisa: 1
Saída Esperada: O sistema detecta que é um número e exibe apenas o produto que possui o ID exato "1", ignorando produtos cujos nomes contenham o número 1 ou IDs terminados em 1.

Teste 5: Empate no Relatório Gerencial
Ação: Gerar relatório com dois produtos possuindo a mesma quantidade máxima no estoque.
Pré-condição: Produto A (Estoque: 100), Produto B (Estoque: 100).
Entrada: Solicitar geração do "Relatório Gerencial".
Saída Esperada: Na linha de Maior Estoque, o sistema não omite nenhum item, exibindo: "Produto(s) de Maior Estoque → Produto A, Produto B (Qtd: 100)".