# FlyFood

Projeto desenvolvido para a disciplina de **Projeto Interdisciplinar para Sistemas de Informação II (PISI2)**, com o objetivo de aplicar conceitos de algoritmos na resolução do **Problema do Caixeiro Viajante (PCV)** no contexto de entregas realizadas por drones.

## 👥 Autores

- Guilherme Vasconcellos
- Carlos Yuri
- Leon Marcelino
- Vinicius Thalles

---

## 📌 Sobre o projeto

O **FlyFood** é um sistema desenvolvido para encontrar uma rota de menor custo para um drone realizar entregas em diferentes pontos de uma matriz.

O drone parte de um ponto inicial, representado por `R`, deve visitar todas as cidades representadas por letras e, ao final, retornar ao ponto de origem.

A movimentação do drone é permitida somente nas direções **horizontal e vertical**, sem movimentação diagonal.

Para calcular a distância entre dois pontos, é utilizada a **distância de Manhattan**:

\[
d(P_i,P_j) = |x_i-x_j| + |y_i-y_j|
\]

Na **primeira unidade da disciplina**, o projeto utiliza uma abordagem de **força bruta**, avaliando todas as possíveis ordens de visita das cidades para encontrar a rota de menor distância.

---

## 📂 Estrutura dos Arquivos

O projeto é organizado nos seguintes arquivos:


```text
Flyfood/
│
├── algoritmo.py
├── cidade.py
├── entrada.txt
├── main.py
├── README.md
└── .gitignore
```

| Arquivo | Descrição |
|---|---|
| `main.py` | Arquivo principal do projeto. É onde ocorre o fluxo principal do programa e onde a execução deve ser iniciada. Nele, a variável `caso_escolhido` define qual matriz de entrada presente em `entrada.txt` será utilizada. |
| `algoritmo.py` | Contém as principais funções responsáveis pelo processamento do problema, que são o cálculo da distância entre as cidades e a geração das permutações das cidades para avaliação das possíveis rotas. |
| `cidade.py` | Contém a classe `Cidade`, criada para facilitar o tratamento das cidades encontradas na matriz. Cada objeto armazena informações como o nome e a posição da cidade na matriz. |
| `entrada.txt` | Arquivo que contém as matrizes utilizadas como casos de entrada. O caso que será executado é selecionado no `main.py` por meio da variável `caso_escolhido`. |


## 📥 Como clonar o repositório

Para obter uma cópia do projeto em seu computador, é necessário ter o **Git** instalado.

### 1. Clonagem do repositório

Abra o terminal e execute o comando:

git clone https://github.com/GuilhermeValois/Flyfood.git

Depois abra o projeto com:

cd Flyfood