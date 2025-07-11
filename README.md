# Sistema de Gestão de Funcionários

## Visão Geral

API robusta para gestão de funcionários, desenvolvida com foco em segurança, escalabilidade e boas práticas de arquitetura. Utiliza FastAPI, Supabase (PostgreSQL), SQLAlchemy, autenticação JWT e hash seguro de senhas com Bcrypt.

## Stack Tecnológica
- **Backend:** FastAPI
- **Banco de Dados:** Supabase (PostgreSQL)
- **ORM:** SQLAlchemy (async)
- **Autenticação:** JWT
- **Segurança:** Bcrypt para hash de senhas

## Arquitetura
- Clean Architecture simplificada
- Separação clara entre camadas: API, serviços, modelos, esquemas e utilitários
- Configuração via `.env` para variáveis sensíveis

## Funcionalidades
- Cadastro, consulta, atualização e remoção de funcionários
- Autenticação segura via JWT
- Hash seguro de senhas
- APIs REST estruturadas e documentadas

## Como Executar
1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure o arquivo `.env`:**
   ```
   SECRET_KEY=...
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   DATABASE_URL=postgresql+asyncpg://usuario:senha@host:porta/db
   ```

3. **Execute os testes de conexão:**
   ```bash
   PYTHONPATH=. python test/test_connection.py
   ```

4. **Inicie o servidor FastAPI:**
   ```bash
   uvicorn app.main:app --reload
   ```

## Futuras Evoluções
- Controle de ponto
- Folha de pagamento
- Painéis administrativos

## Segurança
- Todas as rotas sensíveis exigem autenticação JWT
- Senhas nunca são armazenadas em texto puro

## Contribuição
Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.