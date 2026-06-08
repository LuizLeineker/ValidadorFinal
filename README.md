# Validador Formal em Três Níveis — Hierarquia de Chomsky

![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![Análise Sintática](https://img.shields.io/badge/Teoria--da--Computação-Linguagens--Formais-green)
![Ambiente](https://img.shields.io/badge/Universidade-Positivo-green)

Este projeto consiste no desenvolvimento e análise de uma suíte de simuladores computacionais que mapeiam e validam três níveis fundamentais da **Hierarquia de Chomsky**. O sistema foi construído de forma puramente algorítmica em Python, sem a utilização de engines prontas de parsing (como o módulo nativo `re` de Expressões Regulares), focando estritamente na lógica matemática e estrutural de cada autômato.

O projeto adota o **Tema 1**, concentrando-se na validação estrutural de dados cadastrais, simetria de escopo e integridade de blocos lógicos.

---

## 🛠️ Estrutura dos Validadores

O sistema está dividido de forma estritamente modular, demonstrando o crescimento em poder computacional e a dependência de recursos de memória ($LR \subsetneq LLC \subsetneq R$):

### 1. Nível 3: Linguagem Regular (LR) — Validador de CPF
* **Modelo Abstrato:** Autômato Finito Determinístico (DFA).
* **Escopo:** Validação estrita da estrutura textual e da máscara de pontuação do padrão `ddd.ddd.ddd-dd`.
* **Alfabeto ($\Sigma$):** `{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ., -}`
* **Características:** Processamento estritamente linear sem uso de memória dinâmica auxiliar.

### 2. Nível 2: Linguagem Livre de Contexto (LLC) — Balanceamento de Parênteses
* **Modelo Abstrato:** Autômato com Pilha Determinístico (PDA).
* **Escopo:** Validação de simetria e aninhamento correto de agrupamentos de parênteses, simulando o controle de escopo presente em compiladores.
* **Alfabeto ($\Sigma$):** `{(, )}`
* **Características:** Utiliza uma pilha virtual orientada a uma estrutura LIFO (*Last-In, First-Out*).

### 3. Nível 0/1: Linguagem Recursiva (R) — Reconhecedor $w\#w$
* **Modelo Abstrato:** Máquina de Turing Determinística (MT).
* **Escopo:** Garante que a cadeia gerada antes do caractere separador `#` seja replicada de forma idêntica e na mesma ordem imediatamente após ele.
* **Alfabeto ($\Sigma$):** `{0, 1, #}`
* **Características:** Armazenamento irrestrito operado por um cabeçote de leitura/escrita bidirecional sobre uma fita sequencial.

---

## 📋 Matriz de Casos de Teste

O validador foi homologado e responde deterministicamente sob os seguintes cenários de teste:

| Módulo do Validador | Cadeia de Entrada (Input) | Comportamento Esperado |
| :--- | :--- | :--- |
| **DFA (CPF)** | `123.456.789-10` | **ACEITA** (Formato Correto) |
| **DFA (CPF)** | `111222333-44` | **REJEITADA** (Ausência de pontos) |
| **DFA (CPF)** | `abc.def.ghi-jk` | **REJEITADA** (Caracteres inválidos) |
| **PDA (Pilha)** | `(())` | **ACEITA** (Balanceamento Simétrico) |
| **PDA (Pilha)** | `(()` | **REJEITADA** (Pilha não vazia ao fim) |
| **PDA (Pilha)** | `)(` | **REJEITADA** (Fechamento sem abertura) |
| **MT (Turing)** | `101#101` | **ACEITA** (Cópia Perfeita) |
| **MT (Turing)** | `01#10` | **REJEITADA** (Cadeia invertida) |
| **MT (Turing)** | `110#` | **REJEITADA** (Bloco pós-separador vazio) |

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Ter o Python 3.8 ou superior instalado em sua máquina.

### Clonando o Repositório
```bash
git clone [https://github.com/LuizLeineker/ValidadorFinal.git](https://github.com/LuizLeineker/ValidadorFinal.git)
cd ValidadorFinal
