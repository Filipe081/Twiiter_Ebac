# Tweeter Clone

Tweeter Clone é um projeto desenvolvido em Django que replica funcionalidades básicas de uma plataforma de microblogging. Este projeto permite aos usuários criar uma conta, autenticar-se, postar mensagens curtas (“tweets”), editar ou deletá-las, e realizar logout.

## Funcionalidades

### 1. **Criar Usuário**
   - Permite o registro de novos usuários.
   - Campos obrigatórios: nome de usuário, username, e-mail e senha.

### 2. **Login**
   - Usuários registrados podem acessar sua conta fornecendo nome de usuário e senha.

### 3. **Criar Tweet**
   - Disponível para usuários autenticados.
   - Os tweets são limitados a 140 caracteres.

### 4. **Editar Tweet**
   - Apenas o autor do tweet pode editá-lo.
   - A edição é restrita a usuários autenticados.

### 5. **Deletar Tweet**
   - Apenas o autor do tweet pode deletá-lo.
   - A exclusão está disponível apenas para usuários autenticados.

### 6. **Logout**
   - Permite que o usuário saia da sua sessão atual com segurança.

## Como Rodar o Projeto Localmente

### Requisitos

- Python 3.10 ou superior
- Django 5.1
- Banco de dados configurado (MySql, sqlite, etc.)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Filipe081/tweeter.git
   cd tweeter
   ```

2. instale um gerenciador de projetos:
   ```bash
   pip3 install poetry
   ```

3. Instale as dependências:
   ```bash
   poetry install
   ```

4. Configure o banco de dados:
   ```bash
   poetry run python manage.py migrate
   ```

5. Crie um superusuário (opcional, para acessar o admin):
   ```bash
   poetry run python manage.py createsuperuser
   ```

6. Inicie o servidor local:
   ```bash
   poetry run python manage.py runserver
   ```

7. Acesse o projeto em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Como Usar

### 1. Criar Usuário
   - Navegue até a página de registro.
   - Preencha o formulário com nome de usuário, username, e-mail e senha.

### 2. Fazer Login
   - Acesse a página de login.
   - Insira seu username e senha.

### 3. Criar Tweet
   - Estando autenticado, acesse a página principal.
   - Preencha o formulário de criação de tweet e clique em "Tweet".

### 4. Editar Tweet
   - Clique no ícone de edição ao lado do tweet desejado.
   - Edite o conteúdo e salve.

### 5. Deletar Tweet
   - Clique no ícone de exclusão ao lado do tweet desejado.
   - Confirme a ação de exclusão.

### 6. Fazer Logout
   - Clique no botão de logout no lado esquerdo da página.
r