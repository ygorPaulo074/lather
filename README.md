# lather

SDK Python para processamento e leitura de dados, com saída estruturada e otimizada para modelos de linguagem.

## Instalação

```bash
pip install lather
```

## Uso básico

```python
from lather import Lather

lather = Lather()

lather.configure({
    "privacy":    False,
    "data_limit": "medium",
    "drivers":    ["pdf", "excel"]
})

lather.read("contrato.pdf")
lather.read("planilha.xlsx")

# string única pronta para LLM
resultado = lather.dump()

# lista com um item por arquivo
itens = lather.store()
```

## Drivers disponíveis

| Driver | Formatos |
|--------|----------|
| `pdf`  | `.pdf` |
| `excel` | `.xlsx`, `.xls` |
| `csv`  | `.csv` |
| `word` | `.docx` |

## Parâmetro configurations

| Chave | Tipo | Valores |
|-------|------|---------|
| `privacy` | bool | `True` / `False` |
| `data_limit` | str | `testing` `poor` `medium` `rich` `unlimited` |
| `drivers` | list | lista de drivers ativos |

## Métodos

| Método | Descrição |
|--------|-----------|
| `configure({...})` | Define configurações da instância |
| `read(source)` | Lê e processa um arquivo |
| `dump()` | Retorna string única com todos os documentos |
| `store()` | Retorna lista com um item por documento |
| `history()` | Retorna metadados dos processamentos realizados |
| `clear()` | Limpa o estado interno da instância |

## Status

Em desenvolvimento. O escopo atual cobre leitura algorítmica de arquivos sem dependência de LLM.

## Licença

A definir.# lather
