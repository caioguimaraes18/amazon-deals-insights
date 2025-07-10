# 🛍️ Amazon Deals Insights

Este projeto coleta, armazena e analisa ofertas da Amazon Brasil em tempo real usando uma API pública. Ele filtra e destaca os produtos com maior percentual de desconto, permitindo visualizar insights de forma clara e objetiva.


---

## 🔍 Objetivo

- Coletar dados da API `real-time-amazon-data` (via RapidAPI)
- Armazenar os dados em formato `.json`
- Processar e transformar os dados em um DataFrame com Pandas
- Gerar gráficos para visualizar os produtos mais atrativos por desconto

---

## 🚀 Tecnologias Utilizadas

- Python 3
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Requests](https://docs.python-requests.org/)
- API da Amazon (via [RapidAPI](https://rapidapi.com))

---

## 📦 Estrutura do Projeto

```bash
📁 amazon-deals-insights/
├── Dataset/
│   └── amazon_deals.json        # Dados brutos extraídos da API
├── py_api/
│   ├── main.py                  # Script que coleta os dados e salva o JSON
│   └── headers.py               # Armazena as chaves da API (não versionado)
├── Notebook/
│   └── main.ipynb               # Análise dos dados e visualização dos descontos
├── .gitignore                   # Ignora arquivos sensíveis e pastas temporárias
├── README.md
└── requirements.txt
```

## ✨ Melhorias Futuras

- Dashboard interativo com Streamlit

- Exportação em CSV ou PDF

- Filtros por categoria, faixa de preço e nota do produto


## 🧠 Autor

**Caio Guimarães** - [LinkedIn](https://www.linkedin.com/in/caio-guimar%C3%A3ess/)  


