# ═══════════════════════════════════════════════════════════════
#  PARTE 1: IMPORTS (o que precisa pra rodar)
# ═══════════════════════════════════════════════════════════════

import pandas as pd
import random
from faker import Faker


# ═══════════════════════════════════════════════════════════════
#  PARTE 2: LIGAR O GERADOR DE DADOS FAKE
#  "pt_BR" = dados brasileiros (nome, CPF, endereço...)
# ═══════════════════════════════════════════════════════════════

faker = Faker("pt_BR")


# ═══════════════════════════════════════════════════════════════
#  PARTE 3: CRIAR LISTA VAZIA
#  Aqui vai entrar cada pessoa falsa depois
# ═══════════════════════════════════════════════════════════════

dados_pessoas = []


# ═══════════════════════════════════════════════════════════════
#  PARTE 4: LOOP (repete 10 vezes)
#  Cada volta = 1 pessoa fake completa
# ═══════════════════════════════════════════════════════════════

for _ in range(10):

    # --- DADOS PESSOAIS (gerados automaticamente) ---
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)

    # Data de nascimento baseada na idade que já sorteou
    data = faker.date_of_birth(
        minimum_age=idade,
        maximum_age=idade
    ).strftime("%d/%m/%Y")

    endereco = faker.address()
    estado = faker.state()
    pais = "Brasil"

    # --- JUNTAR TUDO NUM DICIONÁRIO ---
    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "data": data,
        "endereco": endereco,
        "estado": estado,
        "pais": pais
    }

    # --- JOGAR NA LISTA ---
    dados_pessoas.append(pessoa)


# ═══════════════════════════════════════════════════════════════
#  PARTE 5: TRANSFORMAR LISTA EM TABELA (DataFrame)
# ═══════════════════════════════════════════════════════════════

df_pessoas = pd.DataFrame(dados_pessoas)

print("=" * 50)
print("TABELA PADRÃO (pode cortar colunas)")
print("=" * 50)
print(df_pessoas)
print()


# ═══════════════════════════════════════════════════════════════
#  PARTE 6: CONFIGURAR PRA MOSTRAR TUDO
#  Sem cortar colunas, linhas ou texto grande
# ═══════════════════════════════════════════════════════════════

pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", None)

print("=" * 50)
print("TABELA COMPLETA (tudo visível)")
print("=" * 50)
print(df_pessoas.to_string())
print()


# ═══════════════════════════════════════════════════════════════
#  PARTE 7: SALVAR EM ARQUIVO CSV
#  Vai criar "clientes.csv" na mesma pasta do código
# ═══════════════════════════════════════════════════════════════

df_pessoas.to_csv("clientes.csv")

print("=" * 50)
print("✓ ARQUIVO SALVO: clientes.csv")
print("=" * 50)
