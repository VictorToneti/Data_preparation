import pandas as pd

df = pd.read_csv("C:/Users/Usuário/Downloads/clientes.csv")

pd.set_option("display.width", None)
print(df.head())

#remover dados (Sempre remover dados "Inúteis, exemplo: país)
df.drop("pais", axis=1, inplace=True) #Coluna
df.drop(2, axis=0, inplace=True) #Linha

#Normalizar campos de texto
df["nome"] = df["nome"].str.title() #Todas as palavras começam maiúsculas
df["endereco"]  =  df["endereco"].str.lower() #minusculo
df["estado"] = df["estado"].str.strip().str.upper()

#converter os tipos de dados (para inteiro)
df["idade"] = df["idade"].astype(int)

print(df.head())

#tratar valores nulos (ou ausentes)
df_fillna = df.fillna(0) #substituir valores nulos por 0
df_dropna = df.dropna() #remover registros com valores nulos
df_dropna4 = df.dropna(thresh=4) #Manter registro com no minimo 4 não nulos
df = df.dropna(subset=["cpf"]) # Remover registro com cpf nulo

print("Valores nulos:\n", df.isnull().sum())
print("Qtd de registros nulos com fillna:", df.isnull().sum().sum().sum())
print("Qtd de registros nulos com dropna", df_dropna.isnull().sum().sum())
print("Qtd de registros nulos com dropna4:", df_dropna4.isnull().sum().sum())
print("Qtd de registros nulos com cpf:", df.isnull().sum().sum())

df.fillna({"estado": "Desconhecido"}, inplace=True) #Quando nao por o estado, classifica como desconhecido
df["endereco"] = df["endereco"].fillna("Endereço não informado!!")
df["idade_corrigida"] = df["idade"].fillna(df["idade"].mean())

#Tratar formato de dadods
df["data_corrigida"] = pd.to_datetime(df["data"], format="%d/%m/%Y", errors="coerce")

#Tratar dados duplicados
print("Qtd de registros atual:", df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset=["cpf"], inplace=True)
print("Qtd de registros atual:", len(df))

print("Dados Limpos:\n", df)

# Salvar DataFrame
df["data"]  = df["data_corrigida"]
df["idade_corrigida"] = df["idade_corrigida"]

df_salvar  = df[["nome", "endereco", "estado", "cpf", "data", "idade"]]
df_salvar.to_csv("clientes_limpeza.csv", index=False) #Nao repetir colunas!!

print("Novo DataFrame: \n", pd.read_csv("clientes_limpeza.csv"))