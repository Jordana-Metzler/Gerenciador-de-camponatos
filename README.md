# 🏐 Gerenciador de Campeonatos

Sistema de gerenciamento de campeonatos de vôlei desenvolvido em Python, com o objetivo de automatizar processos manuais, garantir assertividade e imparcialidade na gestão de times, partidas e classificações.

---

## ✅ Funcionalidades

- **Cadastro de times** — adiciona múltiplos times ao campeonato em sequência
- **Registro de partidas** — registra resultado com sets e pontos por set de cada time
- **Classificação** — exibe a tabela ordenada por pontos, vitórias e média de pontos
- **Sorteio de chaves** — distribui os times em grupos de forma aleatória e imparcial
- **Exibição de chaves** — lista os times por grupo após o sorteio
- **Persistência automática** — salva e carrega o estado do campeonato em JSON a cada operação

---

## 📁 Estrutura do Projeto

```
Gerenciador-de-camponatos/
│
├── main.py                         # Ponto de entrada — menu principal e loop de execução
├── menu.py                         # Funções de interação com o usuário (input/output)
│
├── Classes/
│   ├── Campeonato.py               # Classe principal — times, partidas, chaves e classificação
│   ├── Time.py                     # Classe Time — estatísticas e cálculo de média de pontos
│   └── Partida.py                  # Classe Partida — resultado, sets e parciais
│
├── service/
│   ├── persistencia.py             # Salvar e carregar campeonato em JSON
│   └── sorteio.py                  # Lógica de sorteio e distribuição de chaves
│
└── estadual_adulto_2026.json       # Exemplo de campeonato salvo
```

---

## ⚙️ Pré-requisitos

- Python 3.10+
- Sem dependências externas — usa apenas a biblioteca padrão do Python

---

## 🚀 Como usar

```bash
python main.py
```

Ao iniciar, o sistema pergunta o nome do campeonato. Se já existir um arquivo salvo com esse nome, ele é carregado automaticamente. Caso contrário, um novo campeonato é criado.

```
Nome do campeonato: estadual adulto 2026
Campeonato carregado!

=== GESTOR DE CAMPEONATO ===
1. Cadastrar time
2. Registrar partida
3. Ver classificação
4. Sortear chaves
5. Exibir chaves
6. Times cadastrados
0. Sair
```

---

## 🗂️ Persistência

O estado do campeonato é salvo automaticamente em um arquivo `.json` após cada operação de escrita (cadastro, partida, sorteio). O nome do arquivo é gerado a partir do nome do campeonato informado na inicialização.

Exemplo de arquivo gerado (`estadual_adulto_2026.json`):

```json
{
  "nome": "estadual adulto 2026",
  "times": [
    { "nome": "BE8/UPF", "vitorias": 1, "pontos": 3, "sets_vencidos": 3 }
  ],
  "partidas": [
    { "vencedor": "BE8/UPF", "perdedor": "AVV", "sets_vencedor": 3, "sets_perdedor": 0 }
  ],
  "chaves": {
    "A": ["UFSM", "BE8/UPF"],
    "B": ["SGNH", "JUVENTUS", "AVV"]
  }
}
```

---

## 📊 Regras de Pontuação

O sistema segue o formato padrão do vôlei:

| Resultado | Pontos Vencedor | Pontos Perdedor |
|-----------|----------------|----------------|
| 3 x 0     | 3              | 0              |
| 3 x 1     | 3              | 0              |
| 3 x 2     | 2              | 1              |

A classificação é ordenada por: **Pontos → Vitórias → Média de Pontos**

---

## 🏗️ Arquitetura

O projeto segue orientação a objetos com separação clara de responsabilidades:

- **`Classes/`** — modela as entidades do domínio (Campeonato, Time, Partida)
- **`service/`** — isola a lógica de persistência e sorteio das classes de negócio
- **`menu.py`** — centraliza toda a interação com o usuário, mantendo o `main.py` limpo
