import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, features='html.parser')

# Exibir o texto
# print(extracao.text.strip())

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Título:', titulo)

...
#Desafio Filtrar tags['h2', 'p'] Contar quantos h2
#e p existem no documento(linha_texto.name == tag)

# Contar gtd de titulos e paragrafos

contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 # contar_titulos contar_titulos 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1
print('Total de titulos', contar_titulos)
print('Total de paragrafos', contar_paragrafos)

#exibir tags alinhadas
for titulo in extracao.find_all('h2'):
    print("\n Título: ", titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all("a", href=True):
            print("Texto Link: ", a.text.strip(), "URL: ", a['href'])

