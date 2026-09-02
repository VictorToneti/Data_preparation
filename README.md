<div align="center">

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=2196F3&center=true&vCenter=true&width=600&lines=Data+Preparation+%26+Preprocessing;Limpeza%2C+Tratamento+e+EDA+em+Python;Pipeline+de+Engenharia+de+Dados" alt="Typing SVG" />
  </a>

  <p><i>Scripts, rotinas e pipelines completas para higienização e transformação de dados em Python.</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
    <img src="https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white" />
  </p>

</div>

---

## 📌 Objetivos do Projeto

- **Higienização:** Identificação e tratamento de registros nulos e duplicados.
- **Detecção de Anomalias:** Aplicação de métodos estatísticos ($IQR$ e $Z\text{-Score}$) para mitigar *outliers*.
- **Feature Engineering:** Codificação de variáveis categóricas (*One-Hot / Label Encoding*) e normalização escalar.
- **Análise Exploratória:** Construção de gráficos dinâmicos para validação de hipóteses.

---

## 📂 Estrutura do Repositório

```text
├── data/                       # Amostras de dados (.csv e .xlsx)
├── notebooks/                  # Análises exploratórias (.ipynb)
├── scripts/                    # Módulos Python em snake_case
│   ├── limpeza_de_dados.py
│   ├── tratar_outliers.py
│   ├── normalizacao_de_dados.py
│   └── codificacao_categoricas.py
├── .gitignore                  # Arquivos ignorados (IDE / caches)
└── requirements.txt            # Dependências do projeto
