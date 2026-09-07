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

## Requisitos

- **Python 3.x** instalado e adicionado às variáveis de ambiente (**PATH**) do sistema.

---

## Instalação

Para que o comando `orgframes` funcione em qualquer pasta do seu computador, siga os passos abaixo:

**1. Clone o repositório**
Baixe ou clone este repositório em uma pasta da sua preferência:

```bash
git clone https://github.com/strLuckyyy/orgframes.git
```

**2. Adicione ao PATH do Windows**
Para rodar o script pelo CMD de qualquer diretório, você precisa adicionar a pasta da automação às Variáveis de Ambiente do sistema:

1. Pressione a tecla `Windows` e pesquise por **"Editar as variáveis de ambiente do sistema"**.
2. Na janela que abrir, clique no botão **Variáveis de Ambiente**.
3. Na seção "Variáveis do sistema" (parte inferior), procure pela variável **Path**, selecione-a e clique em **Editar**.
4. Clique em **Novo** e cole o caminho completo da pasta onde você clonou a automação (ex: `C:\Scripts\orgframes`).
5. Clique em **OK** em todas as janelas para salvar.

**3. Teste a instalação**
Feche todos os terminais abertos. Abra um novo **CMD** (Prompt de Comando) na pasta onde estão os seus frames do Blender e chame a automação.

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
