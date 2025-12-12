# BarbearIA - Documentação da API

API REST para gerenciamento de barbearia desenvolvida com FastAPI.

## 📋 Índice

- [URL Base](#url-base)
- [Endpoints](#endpoints)
  - [Clientes](#clientes)
  - [Funcionários](#funcionários)
- [Modelos de Dados](#modelos-de-dados)
- [Respostas de Erro](#respostas-de-erro)

## URL Base

```
http://localhost:8000
```

## Endpoints

### Clientes

#### Listar Todos os Clientes

```http
GET /clientes
```

**Exemplo de Requisição:**

```bash
curl http://localhost:8000/clientes
```

**Exemplo de Resposta (200 OK):**

```json
[
  {
    "id": 1,
    "email": "joao@email.com",
    "telefone": "84999887766",
    "foto": null
  },
  {
    "id": 2,
    "email": "maria@email.com",
    "telefone": "84988776655",
    "foto": null
  }
]
```

#### Criar Novo Cliente

```http
POST /clientes
```

**Corpo da Requisição:**

```json
{
  "email": "cliente@email.com",
  "senha": "senha123",
  "telefone": "84999887766",
  "foto": null
}
```

**Exemplo de Requisição:**

```bash
curl -X POST http://localhost:8000/clientes \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@email.com",
    "senha": "senha123",
    "telefone": "84999887766"
  }'
```

**Exemplo de Resposta (201 Created):**

```json
{
  "id": 3,
  "email": "cliente@email.com",
  "telefone": "84999887766",
  "foto": null
}
```

---

### Funcionários

#### Listar Todos os Funcionários

```http
GET /funcionarios
```

**Exemplo de Requisição:**

```bash
curl http://localhost:8000/funcionarios
```

**Exemplo de Resposta (200 OK):**

```json
[
  {
    "id": 1,
    "email": "barbeiro@barbearia.com",
    "foto": null,
    "eh_barbeiro": true,
    "eh_admin": false
  },
  {
    "id": 2,
    "email": "admin@barbearia.com",
    "foto": null,
    "eh_barbeiro": false,
    "eh_admin": true
  }
]
```

#### Criar Novo Funcionário

```http
POST /funcionarios
```

**Corpo da Requisição:**

```json
{
  "email": "funcionario@barbearia.com",
  "senha": "senha123",
  "foto": null,
  "eh_barbeiro": true,
  "eh_admin": false
}
```

**Exemplo de Requisição:**

```bash
curl -X POST http://localhost:8000/funcionarios \
  -H "Content-Type: application/json" \
  -d '{
    "email": "funcionario@barbearia.com",
    "senha": "senha123",
    "eh_barbeiro": true,
    "eh_admin": false
  }'
```

**Exemplo de Resposta (201 Created):**

```json
{
  "id": 3,
  "email": "funcionario@barbearia.com",
  "foto": null,
  "eh_barbeiro": true,
  "eh_admin": false
}
```

---

## Modelos de Dados

### Cliente

| Campo     | Tipo   | Obrigatório | Descrição                    |
|-----------|--------|-------------|------------------------------|
| id        | int    | Não*        | ID único (gerado pelo banco) |
| email     | string | Sim         | Email do cliente             |
| senha     | string | Sim**       | Senha (hash bcrypt)          |
| telefone  | string | Sim         | Telefone do cliente          |
| foto      | string | Não         | URL ou caminho da foto       |

\* Gerado automaticamente ao criar  
\** Obrigatório na criação, nunca retornado nas respostas

### Funcionário

| Campo       | Tipo    | Obrigatório | Descrição                         |
|-------------|---------|-------------|-----------------------------------|
| id          | int     | Não*        | ID único (gerado pelo banco)      |
| email       | string  | Sim         | Email do funcionário              |
| senha       | string  | Sim**       | Senha (hash bcrypt)               |
| foto        | string  | Não         | URL ou caminho da foto            |
| eh_barbeiro | boolean | Sim         | Se o funcionário é barbeiro       |
| eh_admin    | boolean | Sim         | Se o funcionário é administrador  |

\* Gerado automaticamente ao criar  
\** Obrigatório na criação, nunca retornado nas respostas

---

## Respostas de Erro

### 400 Bad Request

Retornado quando há erro de validação ou dados inválidos.

```json
{
  "detail": "Email já cadastrado"
}
```

### 404 Not Found

Retornado quando um recurso não é encontrado.

```json
{
  "detail": "Cliente não encontrado"
}
```

### 500 Internal Server Error

Retornado quando há erro interno no servidor.

```json
{
  "detail": "Erro interno do servidor"
}
```

---

## Testando a API

### Swagger UI (Recomendado)

Acesse a documentação interativa em:

```
http://localhost:8000/docs
```

### ReDoc

Documentação alternativa em:

```
http://localhost:8000/redoc
```

### Exemplos com Python

```python
import requests

# Listar clientes
response = requests.get('http://localhost:8000/clientes')
clientes = response.json()
print(clientes)

# Criar novo cliente
novo_cliente = {
    "email": "teste@email.com",
    "senha": "senha123",
    "telefone": "84999887766"
}
response = requests.post('http://localhost:8000/clientes', json=novo_cliente)
cliente_criado = response.json()
print(cliente_criado)
```

### Exemplos com JavaScript (fetch)

```javascript
// Listar clientes
fetch('http://localhost:8000/clientes')
  .then(response => response.json())
  .then(data => console.log(data));

// Criar novo cliente
fetch('http://localhost:8000/clientes', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    email: 'teste@email.com',
    senha: 'senha123',
    telefone: '84999887766'
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```
