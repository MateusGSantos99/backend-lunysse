# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Configuração do Banco de Dados e SQLAlchemy

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 02  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Configuração do SQLite como banco de dados  
- Setup do SQLAlchemy ORM (Object-Relational Mapping)  
- Implementação de sessões de banco de dados  
- Dependency Injection com FastAPI  
- Base declarativa para modelos de dados  

### 🎯 Objetivo Geral
Implementar configuração completa do banco SQLite e setup do SQLAlchemy ORM para suportar operações de dados do sistema Lunysse de agendamento psicológico.

### 💡 Habilidades e Competências
✅ Configurar bancos de dados relacionais com SQLAlchemy  
✅ Implementar padrões de acesso a dados com ORM  
✅ Aplicar Dependency Injection para gerenciamento de sessões  
✅ Estruturar base para manipulação SQL através de Python  

### 📌 Materiais Necessários
📌 Projeto estruturado da aula anterior  
📌 SQLAlchemy instalado via requirements.txt  
📌 Conhecimento básico de SQL  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Estudo de Caso:**  
Análise do problema: "Como um sistema de agendamento psicológico precisa armazenar e gerenciar dados de usuários, pacientes, consultas e relatórios de forma eficiente e segura?"

---

### **Tópico 1: Fundamentos do SQLAlchemy ORM (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração Interativa:**  
Explicação conceitual do ORM, vantagens sobre SQL puro, e como o SQLAlchemy mapeia objetos Python para tabelas relacionais.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Compreender conceitos de ORM na prática  
📝 **Tarefa:**  
- **Metodologia Ativa - Aprendizagem Colaborativa:**  
Discussão em grupos sobre cenários de uso do ORM no sistema de agendamento e mapeamento de entidades.

**Parte do Projeto Construída:** Compreensão conceitual da arquitetura de dados

---

### **Tópico 2: Configuração do Engine e Sessões (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding:**  
Implementação do database.py com engine SQLite, configuração de sessões e parâmetros de conexão.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Configurar conexão com banco de dados  
📝 **Tarefa:**  
- **Metodologia Ativa - Hands-on Programming:**  
Criar database.py, configurar engine SQLite e implementar SessionLocal para gerenciamento de conexões.

**Parte do Projeto Construída:** Configuração de banco funcional (database.py)

---

### **Tópico 3: Base Declarativa e Dependency Injection (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração Guiada:**  
Implementação da Base declarativa e função get_db() para dependency injection no FastAPI.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar padrão de injeção de dependência  
📝 **Tarefa:**  
- **Metodologia Ativa - Prática Orientada:**  
Criar Base declarativa, implementar get_db() e testar injeção de dependência em endpoint básico.

**Parte do Projeto Construída:** Sistema de injeção de dependência para sessões DB

---

### **Tópico 4: Teste de Conexão e Validação (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Debugging Colaborativo:**  
Teste da configuração, verificação de conexão e resolução de possíveis problemas de configuração.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Validar configuração do banco de dados  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Problemas:**  
Testar conexão, criar endpoint de health check do banco e validar funcionamento completo.

**Parte do Projeto Construída:** Sistema de banco validado e funcional

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Reflexão Crítica:**  
Análise da importância do ORM em projetos profissionais e como a configuração adequada impacta performance e manutenibilidade.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio Conceitual:**  
Pensar na modelagem das entidades do sistema: usuários, pacientes, agendamentos. Como essas entidades se relacionam?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação oficial SQLAlchemy  
- Guia FastAPI Database  
- Exemplos práticos de ORM  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Compreensão dos conceitos de ORM  
✅ Sucesso na configuração do engine SQLite  
✅ Implementação correta da injeção de dependência  
✅ Funcionamento da conexão com banco de dados  

### **Avaliação Somativa (Entregáveis):**
✅ Arquivo database.py completo e funcional  
✅ Teste de conexão bem-sucedido  
✅ Endpoint básico usando injeção de dependência  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Configuração completa, conexão estável, código limpo seguindo boas práticas  
- **Bom (7-8):** Configuração funcional com pequenos ajustes na estrutura  
- **Satisfatório (6-7):** Conexão básica funcionando mas com melhorias necessárias  
- **Insatisfatório (<6):** Problemas na conexão ou configuração incompleta  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de configuração SQLAlchemy ORM  
- Compreensão de padrões de acesso a dados  
- Conhecimento de dependency injection no FastAPI  

🎯 **Aplicação Prática:**  
- Capacidade de configurar bancos relacionais em projetos Python  
- Habilidade para implementar camadas de persistência  
- Competência em gerenciamento de sessões de banco  

🎯 **Competências Profissionais:**  
- Pensamento em arquitetura de dados  
- Aplicação de padrões de design para acesso a dados  
- Preparação para desenvolvimento de CRUDs complexos  

### **Conexão com o Projeto:**  
Esta aula estabelece a camada de persistência do sistema Lunysse, criando a base sólida para armazenar dados de usuários, pacientes, agendamentos e relatórios que serão implementados nas próximas aulas.

### **Preparação para Próxima Aula:**  
A configuração do banco será utilizada na próxima aula para criar os modelos SQLAlchemy das entidades principais: User, Patient, Appointment, definindo relacionamentos e constraints do sistema.