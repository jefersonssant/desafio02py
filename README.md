# API Livros Doados VnW

Essa é uma API simples feita com Flask e SQLite para fins de estudo na escola Vai Na Web, ela permite cadastrar e listar livros doados.

## Como rodar o projeto

1. Faça o clone do repositório:
```bash
git clone <LINK_DO_REPOSITÓRIO>
cd nome do projeto
```

2. Criar um ambiente virtual (Obrigatório):

**Windows**

```bash
python -m venv venv
source venv/Scripts/activate
```

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o servidor:

```bash
python app.py
```

> A API estará disponível em http://127.0.0.1:5000/

## Endpoints

### POST/doar

Para cadastrar novos livros você vai utilizar a rota http://127.0.0.1:5000/doar

**Envio (JSON)**

```json
{
  "titulo":"Exemplo de título",
  "categoria":"Exemplo de categoria",
  "autor":"Exemplo nome de autor",
  "image_url":"https://exemplo.com"
}
```

### GET/livros

Para fazer uma requisição e listar os livros cadastrados você vai usar a rota http://127.0.0.1:5000/livros