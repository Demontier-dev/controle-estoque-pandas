# 🧮 Sistema de Controle de Estoque com Python e Pandas

Este projeto implementa um **sistema simples e automatizado de controle de estoque**, utilizando **Python** e a biblioteca **Pandas** para manipulação de dados.

O sistema:

- Lê arquivos CSV contendo **produtos** e **vendas**
- Calcula automaticamente a **quantidade total vendida**
- Atualiza o **estoque final**
- Identifica **produtos com estoque crítico**
- Gera um arquivo `estoque_atualizado.csv` com os dados finais

É um projeto ideal para quem está estudando Python para **automação, análise de dados e freelas**.

---

## 📁 Arquivos do Projeto

| Arquivo | Descrição |
|--------|-----------|
| `controle_estoque.py` | Script principal do sistema |
| `produtos.csv` | Lista de produtos e estoque inicial |
| `vendas.csv` | Registros de vendas por ID do produto |
| `estoque_atualizado.csv` | Arquivo gerado pelo sistema (saída) |

---

## ⚙️ Tecnologias Usadas

- Python 3
- Pandas (manipulação de dados)
- CSV (formato básico de armazenamento)

---

## 🚀 Como Executar o Projeto

### 1️⃣ Instale o Pandas (se necessário)

```bash
pip install pandas
```

### 2️⃣ Coloque os arquivos `.csv` na mesma pasta do script

### 3️⃣ Execute o programa

```bash
python controle_estoque.py
```

Você verá no terminal:

- Relatório completo do estoque  
- Produtos que precisam de reposição  
- Confirmação da geração do arquivo atualizado  

---

## 📊 Exemplo de Saída

```
===== RELATÓRIO DE ESTOQUE =====
   id  qtd_vendida      produto  estoque_inicial  estoque_final  precisa_repor
0   1            8  Hambúrguer               20             12          False
1   2           10  Refrigerante             50             40          False
2   3            1       Pizza               12             11          False
3   4            2    Milkshake              8              6           True
================================
```

---

## 🔎 Funcionalidades

- 📥 **Leitura automática de CSVs**
- ➕ **Agrupamento e soma de vendas por produto**
- 🔗 **Merge estilo PROCV com Pandas**
- 🧮 **Cálculo do estoque final**
- 🚨 **Detecção de estoque crítico**
- 📤 **Geração de um novo CSV atualizado**
- 🖨️ **Exibição de relatório no terminal**

---

## 🧠 O que esse projeto demonstra?

- Habilidade com **Pandas**
- Manipulação de dados reais
- Lógica aplicada em problemas de negócios
- Organização de código
- Preparação para freelas simples de automação

---

## 💼 Possíveis usos reais

- Lanchonetes, pizzarias, hamburguerias  
- Mercadinhos e pequenos comércios  
- Controle básico de estoque de qualquer negócio  
- Automação interna para empresas pequenas  

---

## 🔧 Melhorias futuras

- Criar uma interface gráfica simples  
- Transformar em API com FastAPI  
- Gerar gráficos com Matplotlib ou Plotly  
- Integrar com planilhas Excel  
- Enviar relatório por e-mail automaticamente  

---

## 👨‍💻 Autor

**Demontier Pinheiro**  
GitHub: [https://github.com/Demontier-dev](https://github.com/Demontier-dev)
