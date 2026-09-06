# orgframes: Organização de Frames Renderizados pelo Blender

Automação com o objetivo de agilizar a organização dos frames renderizados pelo Blender em pastas separadas.

## Funcionalidades

Atualmente essa automação consegue:

* Reconhecer os frames na pasta;
* Criar uma pasta com o nome solicitado;
* Copiar os frames para a pasta criada;
* **Opcional:** Criar 2 subpastas, uma com o sufixo `-in` com a ordem dos frames normal e uma com o sufixo `-out` com os mesmos frames, porem que com a ordem invertida (ex: 1 -> 10, 2 -> 9, ...).
* **Opcional:** Apagar os frames na pasta original.

---

## Como usar

A automação funciona pelo CMD. A estrutura básica do comando é:

```bash
orgframes NomePasta -ninout/-inout -d

```

### Tags e Parâmetros

| Comando / Tag | Descrição |
| --- | --- |
| `orgframes` | Nome da automação (call). |
| `NomePasta` | O nome da pasta que desejas criar. |
| `-ninout` | Cria a pasta pedida e as subpastas `-in` e `-out`. Move os frames para tal. |
| `-inout` | Apenas cria as pastas `-in` e `-out` dentro da pasta atual. |
| `-d` | Deleta os arquivos na pasta original. |
