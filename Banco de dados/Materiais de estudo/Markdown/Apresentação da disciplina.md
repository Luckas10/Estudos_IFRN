# Apresentação da disciplina

## 🏦🎲 Banco de dados 🎲🏦

### 💡 Definição:

É uma coleção de dados inter-relacionados, representando informações sobreum domínio específico.

### 📌 Objetivos:

- Evitar redundâncias;
- Evitar Inconsistência nos dados;
- Segurança;
- Garantir atomicidade.

### 🛋 Qual a utilidade desses dados?

- Organização
- Ajuda na tomada de decisão
– O que aconteceu (passado);
– Como agir (presente);
– O que pode ser feito (futuro).

### 👨🏻‍💻 Como usar os dados armazenados em BD?

- Sistemas desktop;
- Sistemas web;
- Aplicativos mobile.

### 📍 Métodos de modelagem:

Através de um método de modelagem é possível, seguindo regras e etapas determinadas, sair da definição informal de um sistema para a modelagem final de um banco de dados.

### ⬆ Top-Down:

- É a abordagem que será adotada.
- Parte do princípio de estudar primeiramente
as definições de baixa abstração (simples) até
as com alta complexidade (abstratas).

![Mundo_real](Images/Mundo_real.png)

### 🌎 Mundo Real:

No nível do mundo “Real” nós não temos um modelo formal de informações. Elas estão dispostas sem limitações. O projetista de banco de dados tem que definir o que interessa do mundo real para o seu projeto. Os objetos do mundo real são os seres, os fatos, as coisas e os organismos sociais.

### ✍🏻 Modelo Descritivo:

- Neste modelo você já filtrou o que interessa no mundo real e já estabelece alguns limites para a organização da informação utilizando linguagens não formais.
- Perceba que, neste nível, você começa a ter algo palpável, pois, neste modelo, já serão colocadas impressões a respeito de como os dados irão organizar-se.
- No nível de mundo real, você irá observar, entrevistar, pesquisar para poder ter subsídios para o modelo descritivo.
- Resumindo: o mundo real não é modelado, ele existe e pronto.
- Já o modelo descritivo é produto do seu trabalho.
- Por ser um nível onde não usamos ainda linguagens formais, a escolha da linguagem a ser utilizada é bem subjetiva.
- Alguns podem querer usar o próprio português, outros podem querer usar alguma linguagem gráfica. Este é um nível de ideias e pensamentos de como as informações irão organizar-se.

### 👔 Modelo conceitual:

- Primeiro nível formal: Aqui definimos estruturas de informação que servem de base para o nosso modelo operacional.
- São identificados os conjuntos de informação e as ligações existentes entre eles.
- Utilizamos, nesta fase, o Modelo de Entidade e Relacionamento (MER) e sua linguagem gráfica(Diagrama de Entidade e Relacionamento).

### 🔁 Modelo Lógico:

- Esse é o modelo Conceitual “desmembrado”.
- A diferença é que agora teremos toda a estrutura do banco de dados, de forma bem detalhada e pronta.
- É independente de SGBD, ou seja, pode ser aplicado a qualquer Banco de Dados relacional.

### 👨🏻‍🔬 Modelo físico:

- É o banco de dados automatizado, específico para a utilização em um Sistema Gerenciador de Banco de Dados (SGBD), tais como:
– Exemplos: ACCESS, Dbase, Paradox, Oracle, SQL Server, Lotus Approach, dentre outros
- Cada um destes SGBD’s tem sua maneira de implementar o seu modelo operacional, porém com pequenas diferenças entre eles.