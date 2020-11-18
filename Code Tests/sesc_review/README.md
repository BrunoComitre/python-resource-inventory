# Newton 3


## Como rodar
```
- export SESC_CONFIG=[local, remote, production, default]
- export FLASK_APP=sesc.py

Optional (para debug)
-export FLASK_ENV=development
```

## CLI

### manage-db:
    - reset-db (deleta base, cria uma nova e cria as tabelas)
    - create-admin (cria um usuário admin para a aplicação) *TODO

## Estrutura base do projeto

### Análise
Descrever o q e necessário para a parte da análise

- A principio: Escrever o nome dos pratos, mas pensar no auto-complete, para pratos futuros.
- Os dados são inseridos de seg a sex, pós horário de almoço.
- Será um serviço rodando em background (análise).
- A análise estatística, será gerada aos finais de semana.
- Criar stopwords de comidas (exemplo, se o cara colocar papel, não pode aceitar).
- Exibição de estatísticas, apenas para cadastrados.

possíveis avaliações:
- extração por comentários (word2vec, cbow)
- Custo-benefício gerado pela inteligência

trava apenas para cadastrados:
- exibir histórico de exibição.
- exibição de estatísticas.

### Rotas
- de avaliação
- de cardápio do dia
- do usuário, devolvendo os dados
- da análise

### Limitação

- A avaliação só será liberada entre meio dia e quatro da tarde, de segunda a sexta.

***

## Development

### Architecture

sesc_review/
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── routes.py
│   └── models.py
│
├── images/
│   └── modelo_cabecalho_local_.png
│
├── .gitignore
├── config.py
├── README.md
├── requirements.txt
└── sesc.py

### Database

database:
- PostgreSQL

requirements/framework:
- Numpy
- Matplotlib
- Virtualenv
- Pandas
- Pip
- Scikit-learn
- SciPy
- Flask
- Flask-SQLAlchemy
- SQLAlchemy     
- SQLAlchemy-Utils
- psycopg2-binary

tools:
- Markdown
- Git(version control)
- GitHub
- Docker
- draw.io
- PEP 8

***



**ALMOÇO**

descrição prato:
- [arroz, feijão, salada de baataata, frutas vermelhas]

qualidade do prato:
- [ ] péssimo
- [ ] ruim
- [ ] normal
- [ ] ótimo
- [ ] excelente

**SERVIÇO**

tempo de espera:
- [campo em minutos] ou,
- [horário de chegada] - [horário de atendimento]

tempo na fila:
- [ ] péssimo
- [ ] ruim
- [ ] normal
- [ ] ótimo
- [ ] excelente

tamanho da fila do caixa:
- [ ] pequena
- [ ] média
- [ ] grande

tempo na fila do caixa/atendimento pagamento:
- [ ] péssimo
- [ ] ruim
- [ ] normal
- [ ] ótimo
- [ ] excelente

**GASTO**
total gasto durante o almoço:
- [inserir valor]


**CADASTRO AVALIADOR**
- nome
- email

***

## Implementação Futura
Obter o cardápio do sesc por pdf e sugerir no cardádio o que tiver por pessoa

***

## links:
- [Modelos de aprendizagem profunda](https://github.com/rasbt/deeplearning-models)

- [Cheatsheets de Ciência de Dados](https://github.com/abhat222/Data-Science--Cheat-Sheet)

- [Awesome Microservices](https://github.com/mfornos/awesome-microservices)

- [Quando usar redes neurais MLP, CNN e RNN](https://machinelearningmastery.com/when-to-use-mlp-cnn-and-rnn-neural-networks/)

- [Primeiros passos no InfluxDB](http://gcruz.com.br/blog/primeiros-passos-influxdb/)

- [git e github parte 1: o que são e como usar?](https://www.ratamero.com/blog/git-e-github-parte-1-o-que-sao-e-como-usar/)

- [Classificando Músicas do Spotify com SVM (Python)](http://minerandodados.com.br/index.php/2018/04/04/spotify-svm-python/)

- [Notebook para integração de vários pacotes com Neo4j, incluindo py2neo, ipython-cypher, pandas, networkx, igraph, e jgraph](https://nicolewhite.github.io/neo4j-jupyter/hello-world.html) 

- [10 hacks simples para acelerar sua análise de dados em Python](https://towardsdatascience.com/10-simple-hacks-to-speed-up-your-data-analysis-in-python-ec18c6396e6b)

- [Criando um modelo NLP de classificação de tweets com fklearn](https://medium.com/data-hackers/criando-um-modelo-nlp-de-classifica%C3%A7%C3%A3o-de-tweets-com-fklearn-b8ff88b96cde)

- [Guia para iniciantes em modelagem de tópicos em Python](https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/)

- [Steppy 1](https://github.com/neptune-ml/steppy) - experimentação de aprendizado de máquina rápida e reproduzível.

- [Optimus](https://github.com/ironmussa/Optimus) - Limpeza, pré-processamento, engenharia de recursos, análise exploratória.

- [variancecharts](http://variancecharts.com/index.html) -  Criem gráficos de dados para a Web, usando apenas HTML e CSS.

- [Data Science IPython Notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) [EN-US] - Ciência de Dados: notebooks Python: Aprendizado profundo (TensorFlow, Theano, Caffe, Keras), scikit-learn, Kaggle, big data (Spark, Hadoop MapReduce, HDFS), matplotlib, pandas, NumPy, SciPy, Python essentials, AWS e vários comandos linhas.

***
