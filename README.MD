# 🧠 Lunysse API

A **Lunysse API** é um backend desenvolvido com **FastAPI**, voltado para o **gerenciamento de atendimentos psicológicos**.  
Inclui funcionalidades de autenticação, cadastro de pacientes e psicólogos, agendamento de consultas, geração de relatórios e integração com serviços de análise via **Machine Learning**.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3.10+**
- ⚡ **FastAPI**
- 🗃️ **SQLAlchemy**
- 💾 **SQLite** (ou outro banco configurável via `.env`)
- 🧩 **Pydantic**
- 🌱 **dotenv**
- 🔒 **CORS Middleware**
- 🤖 **Serviços de Machine Learning (customizados)**

---

## 📂 Estrutura do Projeto

codigo/
│
├── core/ # Configurações principais do app e do banco de dados
│ └── database.py
│
├── models/ # Modelos ORM (SQLAlchemy)
│ └── models.py
│
├── routers/ # Definição das rotas e endpoints
│ ├── auth.py
│ ├── appointments.py
│ ├── patients.py
│ ├── psychologists.py
│ ├── requests.py
│ ├── reports.py
│ └── ml_analysis.py
│
├── schemas/ # Modelos Pydantic (validação de dados)
│ └── schemas.py
│
├── services/ # Lógica de negócio e integração com ML
│ ├── auth_service.py
│ ├── ml_services.py
│ └── report_service.py
│
├── main.py # Ponto de entrada da aplicação FastAPI
├── seed_data.py # (Opcional) Popula o banco com dados iniciais
├── test.py # Testes locais
├── Utils.py # Funções auxiliares
├── requirements.txt # Dependências do projeto
├── .env # Variáveis de ambiente
├── lunysse.db # Banco SQLite local
└── README.md

yaml
Copiar código

---

## ⚙️ Configuração e Execução

### 🧩 1. Clone o repositório
```bash
git clone https://github.com/1067790/backend-lunysse.git
cd backend-lunysse


🧱 2. Crie e ative o ambiente virtual
bash
Copiar código
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


📦 3. Instale as dependências
bash
Copiar código
pip install -r requirements.txt


🔑 4. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

env
Copiar código
DATABASE_URL=sqlite:///./lunysse.db
CORS_ORIGINS=http://localhost:3000
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


▶️ 5. Execute a aplicação
bash
Copiar código
uvicorn main:app --reload
A API estará disponível em:
👉 http://127.0.0.1:8000

📘 Endpoints Principais
Recurso	Descrição
/auth	Autenticação e registro de usuários
/patients	CRUD de pacientes
/psychologists	CRUD de psicólogos
/appointments	Agendamento e gerenciamento de consultas
/reports	Relatórios e análises
/requests	Solicitações diversas do sistema
/ml_analysis	Integração com serviços de Machine Learning
/health	Verificação de saúde da API
/	Mensagem de boas-vindas

🧩 Funcionalidades Existentes
✅ Autenticação e controle de acesso (JWT)
✅ CRUD completo de pacientes e psicólogos
✅ Agendamento e gerenciamento de consultas
✅ Geração e exportação de relatórios
✅ Análise automatizada via modelos de Machine Learning

🌟 Futuras Implementações
🧠 Integração com dashboards analíticos para visualização de métricas e insights.
📈 Relatórios estatísticos mais detalhados com base em dados históricos.
🔔 Sistema de notificações para lembretes de agendamento.

🧪 Testes
Para executar os testes (com pytest configurado):

bash
Copiar código
pytest
💡 Desenvolvido com FastAPI e dedicação para otimizar o gerenciamento de atendimentos psicológicos.