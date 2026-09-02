# ═══════════════════════════════════════════════════════════════
#  PARTE 1: IMPORTS (pandas + numpy)
# ═══════════════════════════════════════════════════════════════

import pandas as pd
import numpy as np


# ═══════════════════════════════════════════════════════════════
#  PARTE 2: CONFIGURAR VISUALIZAÇÃO
#  Mostra tudo sem cortar colunas ou texto
# ═══════════════════════════════════════════════════════════════

pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


# ═══════════════════════════════════════════════════════════════
#  PARTE 3: CARREGAR OS DADOS
# ═══════════════════════════════════════════════════════════════

df = pd.read_csv("clientes_remove_outliers.csv")

print("=" * 50)
print("PRIMEIRA OLHADA (antes de tratar)")
print("=" * 50)
print(df.head())


# ═══════════════════════════════════════════════════════════════
#  PARTE 4: MASCARAR CPF
#  Mostra só os 3 primeiros e 2 últimos dígitos
#  Exemplo: 123.***.***-45
# ═══════════════════════════════════════════════════════════════

df["cpf_mascara"] = df["cpf"].apply(lambda cpf: f"{cpf[:3]}.***.***{cpf[-2:]}")


# ═══════════════════════════════════════════════════════════════
#  PARTE 5: CORRIGIR DATAS
#  Converte texto em data e arruma anos errados
# ═══════════════════════════════════════════════════════════════

# Transforma string em data (formato: ano/mês/dia)
df["data"] = pd.to_datetime(df["data"], format="%y/%m/%d", errors="coerce")

# Pega a data de hoje
data_atual = pd.to_datetime("today")

# Se a data for no futuro, troca para 01/01/2000
df["data_atualizada"] = df["data"].where(df["data"] <= data_atual, pd.to_datetime("2000-01-01"))

# Calcula idade: ano atual - ano de nascimento
df["idade_ajustada"] = data_atual.year - df["data_atualizada"].dt.year

# Diminui 1 se o aniversário ainda não aconteceu este ano
df["idade_ajustada"] -= ((data_atual.month <= df["data_atualizada"].dt.month) & (data_atual.day < df["data_atualizada"].dt.day)).astype(int)

# Se idade for maior que 100, vira vazio (NaN)
df.loc[df["idade_ajustada"] > 100, "idade_ajustada"] = np.nan


# ═══════════════════════════════════════════════════════════════
#  PARTE 6: DIVIDIR O ENDEREÇO EM PARTES
#  Quebra o texto por linhas e separa rua, bairro e estado
# ═══════════════════════════════════════════════════════════════

# Primeira linha do endereço = rua/avenida
df["endereco_curto"] = df["endereco"].apply(lambda x: x.split("\n")[0].strip())

# Segunda linha do endereço = bairro (se não tiver, vira "Desconhecido")
df["bairro"] = df["endereco"].apply(lambda x: x.split("\n")[1].strip() if len(x.split("\n")) > 1 else "Desconhecido")

# Última parte do endereço = sigla do estado
df["estado_sigla"] = df["endereco"].apply(lambda x: x.split(" \ ")[-1].strip() if len(x.split("\n")) > 1 else "desconecido")


# ═══════════════════════════════════════════════════════════════
#  PARTE 7: VERIFICAR SE O ENDEREÇO FAZ SENTIDO
#  Se for muito curto (< 5) ou muito longo (> 50), é inválido
# ═══════════════════════════════════════════════════════════════

df["endereco_curto"] = df["endereco_curto"].apply(
    lambda x: "endereço inválido" if len(x) > 50 or len(x) < 5 else x
)


# ═══════════════════════════════════════════════════════════════
#  PARTE 8: CORRIGIR CPF ERRADO
#  CPF válido tem 14 caracteres (com pontos e traço)
# ═══════════════════════════════════════════════════════════════

df["cpf"] = df["cpf"].apply(lambda x: x if len(x) == 14 else "CPF inválido.")


# ═══════════════════════════════════════════════════════════════
#  PARTE 9: CORRIGIR ESTADO
#  Deixa em maiúsculo e aceita só siglas brasileiras válidas
# ═══════════════════════════════════════════════════════════════

estados_br = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "RN", "GO",
    "MA", "MT", "MG", "MS", "PA", "PB", "PI", "PR", "RO", "RJ",
    "SC", "SP", "SE", "TO"
]

df["estado_sigla"] = df["estado_sigla"].str.upper().apply(
    lambda x: x if x in estados_br else "Desconhecido"
)

print("Dados tratados:\n", df.head)


# ═══════════════════════════════════════════════════════════════
#  PARTE 10: TROCAR COLUNAS ANTIGAS PELAS TRATADAS
# ═══════════════════════════════════════════════════════════════

df["cpf"] = df["cpf_mascara"]
df["idade"] = df["idade_ajustada"]
df["endereco"] = df["endereco_curto"]
df["estado_sigla"] = df["estado_sigla"]


# ═══════════════════════════════════════════════════════════════
#  PARTE 11: ESCOLHER COLUNAS FINAIS E SALVAR
# ═══════════════════════════════════════════════════════════════

df_salvar = df[["nome", "cpf", "idade", "endereco", "bairro", "estado"]]

df_salvar.to_csv("cliente_tratados.csv", index=False)

print("=" * 50)
print("✓ ARQUIVO SALVO: cliente_tratados.csv")
print("=" * 50)