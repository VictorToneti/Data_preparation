import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option("display.max_columns", None)

df = pd.read_csv("funcionarios.csv")

print(df.head())

df = pd.concat([df, pd.get_dummies(df['departamento'], prefix='departamento')], axis=1)

print("\nCodificação da coluna Departamentos para OneHot_encoding")
print(df.head())