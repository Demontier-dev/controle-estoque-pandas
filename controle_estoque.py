import pandas as pd

# 1) Ler os arquivos
prod = pd.read_csv("produtos.csv")
vendas = pd.read_csv("vendas.csv")

# 2) Somar vendas por produto
vendas_por_produto = vendas.groupby("id")["quantidade"].sum().reset_index()

# 3) Juntar vendas com produtos
tabela = pd.merge(vendas_por_produto, prod, on="id")

# 4) Calcular estoque final
tabela["estoque_final"] = tabela["estoque"] - tabela["quantidade"]

# 5) Renomear colunas para algo mais claro
tabela = tabela.rename(columns={
    "quantidade": "qtd_vendida",
    "estoque": "estoque_inicial"
})

# 6) Criar coluna de alerta
tabela["precisa_repor"] = tabela["estoque_final"] < 10


# 7) Mostrar relatório no terminal
print("===== RELATÓRIO DE ESTOQUE =====")
print(tabela)
print("================================")

# 8) Salvar estoque atualizado em CSV
tabela.to_csv("estoque_atualizado.csv", index=False)
print("\nArquivo 'estoque_atualizado.csv' salvo com sucesso!")

# Mostrar apenas produtos que precisam de reposição
criticos = tabela[tabela["precisa_repor"]]

print("\n=== PRODUTOS QUE PRECISAM DE REPOSIÇÃO ===")
print(criticos)