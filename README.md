# Sistema Completo de Atendimento e Análise

## Descrição

Este projeto foi desenvolvido em Python com o objetivo de gerenciar atendimentos em uma clínica ou central de atendimento. O sistema permite cadastrar clientes e atendentes, controlar filas de atendimento, registrar históricos, gerar relatórios e exportar dados.

Além das funcionalidades de negócio, o projeto demonstra a aplicação prática de estruturas de dados e algoritmos estudados em sala de aula, incluindo filas, pilhas, listas encadeadas, busca binária, recursão e ordenação.

---

# Objetivos

* Gerenciar clientes e atendentes.
* Controlar filas de atendimento normais e prioritárias.
* Registrar histórico de atendimentos.
* Permitir desfazer a última finalização de atendimento.
* Gerar relatórios estatísticos.
* Exportar relatórios para CSV.
* Demonstrar o uso de estruturas de dados e análise de complexidade.

---

# Estrutura do Projeto

```text
projeto_atendimento/

│
├── main.py
│
├── modelos/
│   ├── cliente.py
│   ├── atendente.py
│   └── atendimento.py
│
├── estruturas/
│   ├── fila.py
│   ├── pilha.py
│   ├── lista_encadeada.py
│   └── busca_binaria.py
│
├── servicos/
│   ├── clientes.py
│   ├── atendentes.py
│   ├── atendimentos.py
│   └── relatorios.py
│
├── persistencia/
│   ├── arquivos.py
│   └── logs.py
│
├── testes/
│   ├── test_clientes.py
│   ├── test_fila.py
│   └── test_relatorios.py
│
├── dados/
│   ├── clientes.json
│   ├── atendentes.json
│   ├── atendimentos.json
│   ├── relatorio.csv
│   └── logs.txt
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Como Executar

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar o sistema

```bash
python main.py
```

---

# Menu Principal

Ao iniciar o programa, será exibido o menu principal:

```text
=== SISTEMA DE ATENDIMENTO ===

1 - Clientes
2 - Atendentes
3 - Atendimento
4 - Relatórios
0 - Sair
```

---

# Módulo de Clientes

Menu:

```text
1 - Cadastrar
2 - Listar
3 - Buscar por ID
0 - Voltar
```

## Cadastrar Cliente

Informações necessárias:

* ID
* Nome
* Telefone
* Prioridade (Sim ou Não)

Exemplo:

```text
ID: 1
Nome: João
Telefone: 11999999999
Prioridade? s
```

## Listar Clientes

Exibe todos os clientes cadastrados em ordem crescente de ID.

## Buscar Cliente

Busca realizada utilizando busca binária em vetor ordenado.

---

# Módulo de Atendentes

Menu:

```text
1 - Cadastrar
2 - Listar
0 - Voltar
```

## Cadastrar Atendente

Informações:

* ID
* Nome

Exemplo:

```text
ID: 1
Nome: Carlos
```

## Listar Atendentes

Exibe todos os atendentes cadastrados.

---

# Módulo de Atendimento

Menu:

```text
1 - Entrar na fila
2 - Chamar próximo
3 - Finalizar atendimento
4 - Histórico cliente
5 - Desfazer última finalização
0 - Voltar
```

## Entrar na Fila

Adiciona um cliente à fila.

Clientes prioritários entram na fila de prioridade.

Clientes normais entram na fila comum.

## Chamar Próximo

Regras:

* Clientes prioritários possuem preferência.
* Dentro da mesma fila é respeitada a ordem de chegada.
* Um atendente não pode atender mais de um cliente simultaneamente.

## Finalizar Atendimento

Registra:

* Data
* Duração
* Atendente responsável

## Histórico

Exibe todos os atendimentos realizados por um cliente.

## Desfazer Última Finalização

Utiliza uma pilha para restaurar a última operação de finalização.

---

# Módulo de Relatórios

Menu:

```text
1 - Tempo médio
2 - Top 5 clientes
3 - Exportar CSV
4 - Ordenar por duração
0 - Voltar
```

## Tempo Médio

Calcula a média das durações dos atendimentos realizados.

## Top 5 Clientes

Mostra os cinco clientes com maior quantidade de atendimentos.

## Exportação CSV

Gera o arquivo:

```text
dados/relatorio.csv
```

## Ordenação por Duração

Utiliza Merge Sort para ordenar os atendimentos.

---

# Estruturas de Dados Utilizadas

## Vetor Ordenado

Utilizado para armazenar clientes.

Permite a realização de busca binária.

Complexidade:

```text
Busca: O(log n)
Inserção: O(n)
```

---

## Busca Binária

Utilizada para localizar clientes pelo ID.

Complexidade:

```text
O(log n)
```

Também foi implementada uma versão recursiva.

---

## Fila

Utilizada para controlar:

* Fila comum
* Fila prioritária

Complexidade:

```text
Inserção: O(1)
Remoção: O(n)
```

---

## Pilha

Utilizada para desfazer a última finalização.

Complexidade:

```text
Push: O(1)
Pop: O(1)
```

---

## Lista Encadeada

Utilizada para manter a lista de clientes ativos.

Complexidade:

```text
Inserção: O(n)
Busca: O(n)
Remoção: O(n)
```

---

## Recursão

Aplicada na implementação da busca binária recursiva.

---

## Ordenação

Foi utilizado o algoritmo Merge Sort.

Complexidade:

```text
O(n log n)
```

---

# Persistência

Os dados são armazenados em arquivos JSON:

```text
dados/clientes.json
dados/atendentes.json
dados/atendimentos.json
```

Ao iniciar o sistema:

* Os dados são carregados automaticamente.

Ao encerrar:

* Os dados são salvos automaticamente.

---

# Logs

As operações importantes são registradas em:

```text
dados/logs.txt
```

Exemplos:

* Cadastro de clientes.
* Cadastro de atendentes.
* Entrada em filas.
* Finalização de atendimentos.

---

# Testes

Executar:

```bash
pytest
```

Os testes verificam:

* Cadastro de clientes.
* Busca binária.
* Funcionamento da fila.
* Funcionamento da pilha.
* Relatórios.

---

# Requisitos Atendidos

* Cadastro de clientes.
* Cadastro de atendentes.
* Fila comum.
* Fila prioritária.
* Chamada de atendimento.
* Finalização de atendimento.
* Histórico por cliente.
* Desfazer última finalização.
* Lista encadeada para clientes ativos.
* Busca binária.
* Vetor ordenado.
* Recursão.
* Relatórios.
* Exportação CSV.
* Persistência em arquivos.
* Testes básicos.
* Modularização.
* Tratamento de erros.
* Logs de operações.

---

# Autor

Projeto desenvolvido para fins acadêmicos na disciplina de Estruturas de Dados e Programação em Python.
