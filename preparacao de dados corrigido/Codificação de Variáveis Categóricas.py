# ═══════════════════════════════════════════════════════════════
#  PARTE 1: IMPORTS (só o básico)
# ═══════════════════════════════════════════════════════════════

import pandas as pd
from sklearn.preprocessing import LabelEncoder


# ═══════════════════════════════════════════════════════════════
#  PARTE 2: CONFIGURAÇÃO RÁPIDA
# ═══════════════════════════════════════════════════════════════

# Mostra TODAS as colunas (não esconde nada)
pd.set_option('display.max_columns', None)


# ═══════════════════════════════════════════════════════════════
#  PARTE 3: CARREGAR OS DADOS
# ═══════════════════════════════════════════════════════════════

df = pd.read_csv("clientes-v2-tratados.csv")

print("=" * 50)
print("PRIMEIRA OLHADA NOS DADOS")
print("=" * 50)
print(df.head())
print()


# ═══════════════════════════════════════════════════════════════
#  PARTE 4: ONE-HOT ENCODING
#  O que faz: cada tipo de 'estado_civil' vira uma coluna nova
#  Exemplo: solteiro → 1, casado → 0 (tipo SIM/NÃO)
# ═══════════════════════════════════════════════════════════════

df = pd.concat(
    [df, pd.get_dummies(df["estado_civil"], prefix="estado_civil")],
    axis=1
)

print("=" * 50)
print("DEPOIS DO ONE-HOT (estado_civil virou várias colunas)")
print("=" * 50)
print(df.head())
print()


# ═══════════════════════════════════════════════════════════════
#  PARTE 5: CODIFICAÇÃO ORDINAL
#  O que faz: transforma escolaridade em NÚMERO com ORDEM
#  Fundamental(1) < Médio(2) < Superior(3) < Pós(4)
# ═══════════════════════════════════════════════════════════════

educacao_ordem = {
    'Ensino Fundamental': 1,
    'Ensino Médio': 2,
    'Ensino Superior': 3,
    'Pós Graduação': 4
}

df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print("=" * 50)
print("DEPOIS DA ORDINAL (escolaridade virou número crescente)")
print("=" * 50)
print(df.head())
print()


# ═══════════════════════════════════════════════════════════════
#  PARTE 6: CÓDIGOS DE CATEGORIA (.cat.codes)
#  O que faz: cada área de atuação ganha um número automático
#  O PANDAS escolhe, você não precisa fazer nada
# ═══════════════════════════════════════════════════════════════

df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print("=" * 50)
print("DEPOIS DO .CAT.CODES (área virou número automático)")
print("=" * 50)
print(df.head())
print()


# ═══════════════════════════════════════════════════════════════
#  PARTE 7: LABEL ENCODER
#  O que faz: transforma ESTADO em número de 0 até N-1
#  Exemplo: SP=0, RJ=1, MG=2... (ordem alfabética)
# ═══════════════════════════════════════════════════════════════

label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print("=" * 50)
print("DEPOIS DO LABEL ENCODER (estado virou número)")
print("=" * 50)
print(df.head())
print()


# ═══════════════════════════════════════════════════════════════
#  FIM ✓
# ═══════════════════════════════════════════════════════════════