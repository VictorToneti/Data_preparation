import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('/preparacao de dados/clientes-v2-tratados.csv')

print(df.head())

# Transformação Logarítimica
df['salario_log'] = np.log1p(df['salario']) # logip é usado para evitar problemas com valores zero

print("\nDataFrame após transformação logarítimica no salario:\n", df.head())

# Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)

print("\nDataFrame após transformação boxcox no salario:\n", df.head())

# Codificação de Frequência para estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)

print("\nDataFrame após codificação de frequência para 'estado':\n", df.head())

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']

print("\nDataframe após criação de interaçao entre idade e numero filho:\n", df.head())