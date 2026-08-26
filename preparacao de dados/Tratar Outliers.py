import pandas as pd
from scipy import stats

pd.set_option("display.width", None)

df = pd.read_csv("clientes_limpeza.csv")

df_filtro_basico  = df[df["idade"] > 100]

print("Filtro Basico \n", df_filtro_basico[["nome", "idade"]])

# Identificar outliers com Z-score!
z_scores = stats.zscore(df["idade"].dropna())
outliers_z = df[z_scores >= 3]
print("Outliers pelo Z-score:\n", outliers_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df["idade"]) > 3)]

# Identificar outliers com IQR
Q1 = df["idade"].quantile(0.25)
Q3 = df["idade"].quantile(0.75)
IQR = Q3 - Q1

Limite_baixo = Q1 - 1.5 * IQR
Limite_alto = Q3 + 1.5 * IQR

print("Limites IQR: ", Limite_baixo, Limite_alto )

# Filtr outliers com IQR
df_iqr = df[(df["idade"] >= Limite_baixo) & df["idade"] <= Limite_alto]

Limite_baixo = 0
Limite_alto = 100

# Filtrar endereços inválidos
df["endereco"]  = df["endereco"].apply(lambda x: "Endereço inválido" if len(x.split("\n")) < 3 else x)
print("Qtd de registros com Endereços inválidos: ", (df["endereco"] == "Endereço inválido").sum)

# Filtrar campos de texto
df["nome"] = df["nome"].apply(lambda x: "Nome inválido" if isinstance(x, str) and len(x) >  50 else x)
print("Qtd registros com nomes grandes: ", (df["nome"] == "Nome inválido").sum)

print("\nDados com outliers tratados:\n", df)

# Salvar dataFrame
df.to_csv("clientes_remove_outliers.csv", index=False)