# 🏥 Lunysse FastAPI - Sistema de Agendamento Psicológico

**Projeto Integrador - Curso Desenvolvimento de Sistemas com Machine Learning**  
**SENAC - 96 horas | Docente: Jeremias de Oliveira Nunes**

API REST completa desenvolvida em FastAPI para sistema de agendamento psicológico com análise inteligente de risco de pacientes usando Machine Learning personalizado.

## 🎓 Sobre o Projeto Pedagógico

Este projeto foi desenvolvido como **Projeto Integrador** do curso "Desenvolvimento de Sistemas com Machine Learning" seguindo metodologia de **Aprendizagem Baseada em Projetos**. O sistema representa um caso real de aplicação de tecnologias modernas em saúde mental.

### 📚 Material Pedagógico Completo

#### **UC 02 - Desenvolvimento do Sistema Base (60h)**
Todos os **15 planos de aula** detalhados estão disponíveis em: `Arquivos do curso/Plano de aula/UC 02/`

- **Aula 01-04**: Fundação (Estrutura, Banco, Modelos)
- **Aula 05-07**: Segurança (Schemas, Utils, Autenticação)
- **Aula 08-10**: Funcionalidades (CRUD, Agendamentos, Solicitações)
- **Aula 11-12**: Inteligência (Relatórios, Machine Learning)
- **Aula 13-15**: Qualidade (Testes, Documentação, Deploy)

#### **UC 03 - Serviços Web Avançados (36h)**
Todos os **9 planos de aula** detalhados estão disponíveis em: `Arquivos do curso/Plano de aula/UC03/`

- **Aula 01**: Revisão e Versionamento da API
- **Aula 02**: Integração com APIs Externas (ViaCEP)
- **Aula 03**: Sistema de Notificações (SendGrid)
- **Aula 04**: Frontend Web Consumidor
- **Aula 05**: Cache Distribuído (Redis)
- **Aula 06**: Microserviços de Relatórios
- **Aula 07**: Testes de Integração End-to-End
- **Aula 08**: Monitoramento e Observabilidade
- **Aula 09**: Deploy e CI/CD Pipeline

## 🚀 Funcionalidades

### **Sistema Base (UC 02)**
- **Autenticação JWT** - Login e registro de usuários
- **Gerenciamento de Agendamentos** - Criar, listar, atualizar e cancelar sessões
- **Gestão de Pacientes** - Cadastro e acompanhamento de pacientes
- **Solicitações** - Sistema de pedidos de novos pacientes
- **Relatórios** - Estatísticas e análises para psicólogos
- **Psicólogos** - Listagem de profissionais disponíveis
- **🤖 Machine Learning** - Análise de risco de pacientes baseada em frequência

### **Serviços Web Avançados (UC 03)**
- **🔄 Versionamento de API** - Suporte a múltiplas versões (v1, v2)
- **🌐 Integração Externa** - ViaCEP para endereços automáticos
- **📧 Notificações** - Sistema de emails com SendGrid
- **💻 Frontend Web** - SPA responsiva consumindo a API
- **⚡ Cache Distribuído** - Redis para otimização de performance
- **📊 Microserviços** - Relatórios independentes com PDFs/Excel
- **🧪 Testes Avançados** - Integração e end-to-end completos
- **📈 Observabilidade** - Monitoramento com Prometheus/Grafana
- **🚀 CI/CD** - Deploy automatizado em produção

## 📦 Estrutura do Projeto

```
lunysse-fastapi/
├── app/                     # 🏗️ Aplicação principal
│   ├── main.py              # Ponto de entrada FastAPI
│   ├── database.py          # Configuração SQLite + SQLAlchemy
│   ├── utils.py             # Funções auxiliares (JWT, bcrypt, idade)
│   ├── config.py            # Configurações e variáveis de ambiente
│   ├── validators.py        # Validadores personalizados
│   ├── logging_config.py    # Configuração de logs
│   ├── routers/             # 🛣️ Rotas da API
│   │   ├── auth.py          # Autenticação (login/register)
│   │   ├── appointments.py  # Sistema de agendamentos
│   │   ├── patients.py      # Gestão de pacientes
│   │   ├── psychologists.py # Listagem de profissionais
│   │   ├── requests.py      # Solicitações de novos pacientes
│   │   ├── reports.py       # Relatórios e estatísticas
│   │   └── ml_analysis.py   # 🤖 Análise ML de risco
│   ├── models/              # 🗄️ Modelos SQLAlchemy
│   │   └── models.py        # Definições das tabelas e relacionamentos
│   ├── schemas/             # ✅ Schemas Pydantic
│   │   └── schemas.py       # Validação e serialização de dados
│   └── services/            # 🔧 Lógica de negócio
│       ├── auth_service.py  # Serviços de autenticação
│       ├── report_service.py# Geração de relatórios
│       └── ml_service.py    # 🧠 Algoritmos de Machine Learning
├── Arquivos do curso/       # 📚 Material pedagógico
│   ├── Plano de Trabalho Docente/  # PTDs das UCs
│   ├── Plano de aula/       # Planos de aula organizados
│   │   ├── UC 02/           # 15 aulas - Sistema base (60h)
│   │   └── UC03/            # 9 aulas - Serviços web (36h)
│   └── Modelos de documentos/
├── logs/                    # 📝 Arquivos de log
├── .env                     # 🔐 Variáveis de ambiente
├── requirements.txt         # 📦 Dependências Python
├── seed_data.py            # 🌱 Dados de teste
├── test_api.py             # 🧪 Testes de API
├── test_ml.py              # 🧪 Testes de Machine Learning
├── run.py                  # 🚀 Script de execução
├── README.md               # 📖 Documentação principal
└── DOCUMENTACAO-BACKEND.md # 📋 Documentação técnica detalhada
```

## 🛠️ Instalação e Execução

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Popular banco com dados de teste
```bash
python seed_data.py
```

### 3. Executar a API
```bash
uvicorn app.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

### 4. Documentação interativa
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔐 Usuários de Teste

### Psicólogos:
- **ana@test.com** / 123456 - Dra. Ana Costa (TCC)
- **carlos@test.com** / 123456 - Dr. Carlos Mendes (Psicologia Infantil)
- **lucia@test.com** / 123456 - Dra. Lucia Ferreira (Terapia Familiar)

### Paciente:
- **paciente@test.com** / 123456 - Maria Santos

## 📋 Endpoints Principais

### Autenticação
- `POST /auth/login` - Login de usuário
- `POST /auth/register` - Registro de novo usuário

### Agendamentos
- `GET /appointments/` - Listar agendamentos do usuário
- `POST /appointments/` - Criar novo agendamento
- `PUT /appointments/{id}` - Atualizar agendamento
- `DELETE /appointments/{id}` - Cancelar agendamento
- `GET /appointments/available-slots` - Horários disponíveis

### Pacientes
- `GET /patients/` - Listar pacientes (psicólogos)
- `POST /patients/` - Cadastrar novo paciente
- `GET /patients/{id}/sessions` - Sessões do paciente
- `POST /patients/{id}/notes` - Adicionar anotação

### Solicitações
- `GET /requests/` - Listar solicitações (psicólogos)
- `POST /requests/` - Criar nova solicitação
- `PUT /requests/{id}` - Atualizar status da solicitação

### Relatórios
- `GET /reports/{psychologist_id}` - Dados para relatórios

### Machine Learning
- `GET /ml/risk-analysis` - Análise de risco de todos os pacientes
- `GET /ml/risk-analysis/{patient_id}` - Análise detalhada de um paciente

### Psicólogos
- `GET /psychologists/` - Listar psicólogos disponíveis

## 🔧 Tecnologias Utilizadas

### **Stack Principal**
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para Python
- **SQLite** - Banco de dados leve
- **Pydantic** - Validação de dados
- **JWT** - Autenticação via tokens
- **Bcrypt** - Hash de senhas
- **Uvicorn** - Servidor ASGI
- **NumPy** - Computação científica para ML

### **Integrações e Serviços**
- **ViaCEP API** - Consulta automática de endereços
- **SendGrid** - Envio profissional de emails
- **Redis** - Cache distribuído e performance
- **Prometheus** - Métricas e monitoramento
- **Grafana** - Dashboards e visualização
- **GitHub Actions** - CI/CD automatizado
- **Railway/Heroku** - Deploy em produção
- **🤖 ML Personalizado** - Algoritmo de análise de risco

## 📊 Status de Agendamentos

- `agendado` - Sessão marcada
- `concluido` - Sessão realizada
- `cancelado` - Sessão cancelada
- `reagendado` - Sessão remarcada

## 🔒 Autenticação

A API utiliza JWT (JSON Web Tokens) para autenticação. Após o login, inclua o token no header:

```
Authorization: Bearer <seu_token_jwt>
```

## 🤖 Análise de Machine Learning

### Algoritmo de Risco
O sistema analisa automaticamente o risco de cada paciente baseado em:

- **Frequência de consultas** - Consultas por mês
- **Taxa de cancelamento** - % de consultas canceladas
- **Ausências** - Dias desde última consulta
- **Tendências** - Padrão de comparecimento recente
- **Agendamentos futuros** - Presença de consultas marcadas

### Níveis de Risco
- 🔴 **Alto (70-100)** - Paciente em risco de abandono
- 🟡 **Moderado (40-69)** - Requer atenção
- 🟢 **Baixo (0-39)** - Padrão normal

### Métricas Calculadas
- Score de risco (0-100)
- Razão principal do risco
- Estatísticas de comparecimento
- Padrões de comportamento

## 🚨 Exceções Personalizadas

A API retorna erros HTTP estruturados:
- `400` - Bad Request (dados inválidos)
- `401` - Unauthorized (não autenticado)
- `403` - Forbidden (sem permissão)
- `404` - Not Found (recurso não encontrado)
- `500` - Internal Server Error (erro interno)

## 🎯 Indicadores Pedagógicos Atendidos

✅ **Desenvolvimento orientado a objetos** - Aplicado em modelos, serviços e funcionalidades  
✅ **Uso de SQL para manipulação e relatórios** - SQLAlchemy ORM e consultas complexas  
✅ **Documentação do projeto web** - README, Swagger UI e documentação técnica  
✅ **Integração de segurança da informação** - JWT, bcrypt, validações e testes  

## 🏆 Competências Desenvolvidas

### 💻 **Conhecimentos Técnicos**
- Arquitetura FastAPI profissional
- SQLAlchemy ORM e modelagem de dados
- Autenticação JWT e segurança
- Machine Learning aplicado à saúde
- Testes automatizados e validações

### 🛠️ **Habilidades Práticas**
- Estruturar projetos backend completos
- Implementar APIs RESTful seguras
- Desenvolver algoritmos de análise de dados
- Documentar sistemas complexos
- Trabalhar com versionamento Git

### 🎯 **Atitudes Profissionais**
- Responsabilidade com dados sensíveis de saúde
- Colaboração em equipe de desenvolvimento
- Ética no tratamento de informações médicas
- Busca por excelência técnica
- Pensamento sistêmico e analítico

## 📖 Metodologias Ativas Aplicadas

- **Aprendizagem Baseada em Projetos** - Desenvolvimento do sistema completo
- **Resolução de Problemas** - Desafios reais de consultórios psicológicos
- **Live Coding** - Implementação colaborativa em tempo real
- **Programação em Pares** - Desenvolvimento colaborativo
- **Estudo de Casos** - Cenários reais de uso do sistema

## 🚀 Evolução do Projeto

### **UC 02 - Sistema Base (60h - 15 aulas)**

#### **Fase 1: Fundação (Aulas 1-4)**
- Estrutura profissional do projeto
- Configuração de banco de dados
- Modelagem orientada a objetos
- Relacionamentos complexos

#### **Fase 2: Segurança (Aulas 5-7)**
- Validação de dados com Pydantic
- Funções de segurança (JWT, bcrypt)
- Sistema de autenticação completo

#### **Fase 3: Funcionalidades (Aulas 8-10)**
- CRUD completo de pacientes
- Sistema central de agendamentos
- Gestão de solicitações e workflows

#### **Fase 4: Inteligência (Aulas 11-12)**
- Relatórios e estatísticas avançadas
- Algoritmo ML personalizado para análise de risco

#### **Fase 5: Qualidade (Aulas 13-15)**
- Testes automatizados completos
- Documentação técnica profissional
- Deploy e versionamento

### **UC 03 - Serviços Web Avançados (36h - 9 aulas)**

#### **Fase 1: Evolução e Integração (Aulas 1-3)**
- Versionamento profissional da API
- Integração com APIs externas (ViaCEP)
- Sistema de notificações (SendGrid)

#### **Fase 2: Interface e Performance (Aulas 4-5)**
- Frontend web consumidor completo
- Cache distribuído com Redis

#### **Fase 3: Arquitetura Distribuída (Aulas 6-7)**
- Microserviços de relatórios
- Testes de integração end-to-end

#### **Fase 4: Produção (Aulas 8-9)**
- Monitoramento e observabilidade
- Deploy automatizado com CI/CD

## 📊 Resultados de Aprendizagem

### **UC 02 - Sistema Base**
- ✅ **Sistema completo** de agendamento psicológico
- ✅ **Algoritmo ML personalizado** para análise de risco
- ✅ **Arquitetura profissional** seguindo padrões de mercado
- ✅ **Documentação completa** para colaboração
- ✅ **Testes automatizados** para garantia de qualidade

### **UC 03 - Serviços Web Avançados**
- ✅ **Integração com serviços externos** (ViaCEP, SendGrid)
- ✅ **Frontend web responsivo** consumindo a API
- ✅ **Arquitetura de microserviços** escalável
- ✅ **Cache distribuído** para alta performance
- ✅ **Monitoramento profissional** em produção
- ✅ **Deploy automatizado** com CI/CD
- ✅ **Portfólio completo** pronto para mercado

---

---

## 🎯 **Projeto Pedagógico Completo - 96 Horas**

### **📈 Progressão de Aprendizagem:**
- **UC 02 (60h):** Desenvolvimento completo do sistema base
- **UC 03 (36h):** Evolução para serviços web avançados e produção

### **🏆 Competências Desenvolvidas:**
- Desenvolvimento full-stack profissional
- Arquitetura de sistemas distribuídos
- Integração com serviços externos
- DevOps e operação em produção
- Machine Learning aplicado à saúde

### **💼 Preparação para o Mercado:**
- Portfólio completo com sistema em produção
- Experiência em tecnologias modernas
- Conhecimento em arquitetura escalável
- Práticas profissionais de desenvolvimento

**💡 Este projeto demonstra a aplicação prática de tecnologias modernas em um contexto real de saúde mental, preparando desenvolvedores para desafios profissionais com responsabilidade social e excelência técnica.**