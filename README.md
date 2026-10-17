# Monitor do reservatório

Programa em Python para classificar o nível de um reservatório, informado em
metros, em uma das cinco faixas de situação. Cada classificação é exibida com
uma cor para facilitar a leitura.

## Faixas de classificação

O programa aceita níveis de `5,00 m` a `100,00 m`. Os limites superiores de
cada faixa são inclusivos:

| Nível informado | Classificação |
| --- | --- |
| De `5,00 m` até `24,00 m` | Nível 1 - Muito baixo (CRÍTICO) |
| Acima de `24,00 m` até `43,00 m` | Nível 2 - Baixo |
| Acima de `43,00 m` até `62,00 m` | Nível 3 - Médio |
| Acima de `62,00 m` até `81,00 m` | Nível 4 - Alto |
| Acima de `81,00 m` até `100,00 m` | Nível 5 - Muito alto (ALERTA) |

## Requisitos

- Python 3 instalado.
- Biblioteca `colorama`.

Instale a dependência com:

```bash
python -m pip install colorama
```

## Como executar

Salve o código do programa em `monitor_reservatorio.py` e execute no terminal:

```bash
python monitor_reservatorio.py
```

Digite o nível em metros quando solicitado. O programa aceita ponto ou vírgula
como separador decimal, por exemplo `37.5` ou `37,5`. Para encerrar, digite
`sair`.

Entradas que não forem numéricas ou estiverem fora do intervalo de `5,00 m` a
`100,00 m` são informadas e solicitadas novamente.
