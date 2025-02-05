# API com Copilot

Este projeto é uma aplicação de gerenciamento de tarefas construída com FastAPI e Python, utilizando a arquitetura limpa. A aplicação permite criar, listar e deletar tarefas, armazenando os dados em um arquivo de memória.

## Estrutura do Projeto

```
API-com-Copilot
├── app
│   ├── api
│   │   ├── v1
│   │   │   ├── endpoints
│   │   │   │   ├── create_task.py
│   │   │   │   ├── list_tasks.py
│   │   │   │   └── delete_task.py
│   │   │   └── api.py
│   │   └── dependencies.py
│   ├── core
│   │   ├── config.py
│   │   └── security.py
│   ├── models
│   │   └── task.py
│   ├── repositories
│   │   └── task_repository.py
│   ├── schemas
│   │   └── task.py
│   ├── services
│   │   └── task_service.py
│   ├── main.py
│   └── memory.py
├── requirements.txt
└── README.md
```

## Funcionalidades

- **Criar Tarefa**: Endpoint para criar uma nova tarefa.
- **Listar Tarefas**: Endpoint para listar todas as tarefas existentes.
- **Deletar Tarefa**: Endpoint para deletar uma tarefa específica pelo ID.

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu_usuario/API-com-Copilot.git
   ```
2. Navegue até o diretório do projeto:
   ```
   cd API-com-Copilot
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para iniciar a aplicação, execute o seguinte comando:

```
uvicorn app.main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

## Documentação da API

A documentação interativa da API pode ser acessada em `http://127.0.0.1:8000/docs` após iniciar a aplicação.