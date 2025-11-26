
# Algoritmo Genético — TSP (repos clone → Jupyter Web)

Repositório com a implementação do Algoritmo Genético para o Problema do Caixeiro Viajante (TSP).
Fluxo de uso: **clonar → abrir Jupyter no navegador → abrir `experiment_AG.ipynb` → executar células**.

---

## Estrutura de pastas (do repositório)

```
.
├── data/                    # instâncias .tsp (EUC_2D, ATT, etc.)
├── stc/                     # código e módulos usados (separados)
├── results/                 # gráficos e arquivos gerados automaticamente
├── report/                  # relatório e arquivos para entrega (PDF/DOCX)
├── experiment_AG.ipynb      # notebook principal (abra no Jupyter)
└── requirements.txt         # dependências (opcional)
```

> Observação: todas as funções já estão no notebook ou na pasta `stc/` — não é necessário reorganizar nada após clonar.

---

## Como rodar (modo simples — Jupyter Web)

1. Clone o repositório:

```bash
git clone <URL-do-seu-repo>
cd <nome-do-repo>
```

2. Abra o Jupyter Notebook (navegador web). A forma mais direta que funciona mesmo quando `jupyter` não está no PATH:

```bash
python -m notebook
```

ou

```bash
py -m notebook
```

Isso abre o Jupyter no navegador na pasta do repositório.

3. No navegador, clique em:

```
experiment_AG.ipynb
```

e execute as células (Shift + Enter) na ordem. Use *Run → Run All Cells* para rodar tudo de uma vez.

---

## Dependências (opcionais)

Se quiser instalar dependências antes de rodar (recomendado), execute:

```bash
python -m pip install numpy pandas matplotlib
```

ou instale todas do `requirements.txt` (se existir):

```bash
python -m pip install -r requirements.txt
```

> Se o comando `pip` não for reconhecido, use sempre `python -m pip ...` ou `py -m pip ...`.

---

## Onde colocar / encontrar os arquivos

* Coloque suas instâncias `.tsp` dentro de `data/` (já pode haver subpastas `EUC_2D/` e `ATT/`), por exemplo:

  * `data/EUC_2D/berlin52.tsp`
  * `data/ATT/att48.tsp`

* Resultados (gráficos, CSVs) serão gravados automaticamente em `results/`.

* Relatório final (doc/pdf) coloque em `report/`.

* Código utilitário já está em `stc/` (separado para organização) — o notebook importa funções de lá.

---

## Observações úteis

* Use barras `/` ao informar caminhos no notebook (funciona no Windows e Linux): `data/ATT/att48.tsp`.
* Se preferir, abra o notebook com `jupyter lab` (se instalado): `python -m jupyterlab`.
* Se tiver erro de dependência dentro do Jupyter, rode numa célula:

  ```python
  !python -m pip install numpy pandas matplotlib
  ```

---

## Execuções e resultados

O notebook `experiment_AG.ipynb` já contém células para:

* ler instâncias `.tsp` (EUC_2D / ATT) automaticamente,
* rodar experimentos M×N (variação de parâmetro),
* salvar DataFrame com resultados,
* gerar e salvar gráficos (boxplot, evolução, melhor rota).

Basta abrir e rodar as células.





