# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Sistema de Autenticação - Login e Registro

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 07  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Desenvolvimento do router auth.py com endpoints seguros  
- Implementação do serviço de autenticação (auth_service.py)  
- Tratamento de erros e validações de credenciais  
- Integração JWT com FastAPI Dependency Injection  
- Proteção de rotas e middleware de autenticação  

### 🎯 Objetivo Geral
Implementar rotas de autenticação com login e registro de usuários, desenvolvendo sistema completo de autenticação seguindo boas práticas de segurança para sistemas de saúde.

### 💡 Habilidades e Competências
✅ Desenvolver endpoints seguros de autenticação  
✅ Implementar validação robusta de credenciais  
✅ Aplicar tratamento de erros de segurança  
✅ Integrar JWT com dependency injection do FastAPI  

### 📌 Materiais Necessários
📌 Funções de segurança da aula anterior (utils.py)  
📌 Modelos User e schemas implementados  
📌 Conhecimento de HTTP status codes de segurança  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Cenário de Segurança:**  
Análise de caso: "Como garantir que apenas psicólogos e pacientes autorizados acessem o sistema? Quais são os riscos de uma autenticação mal implementada em sistemas médicos?"

---

### **Tópico 1: Router de Autenticação - Estrutura Segura (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Arquitetura de Segurança:**  
Estruturação do router auth.py, definição de endpoints seguros e padrões de resposta para autenticação em sistemas críticos.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar estrutura base do router de autenticação  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Seguro:**  
Implementar router auth.py com estrutura base, importações necessárias e configuração de tags para documentação.

**Parte do Projeto Construída:** Router auth.py estruturado e configurado

---

### **Tópico 2: Endpoint de Login - Validação de Credenciais (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding Seguro:**  
Implementação do endpoint /login com validação de credenciais, verificação de senha e geração de token JWT seguro.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar login seguro com JWT  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação Defensiva:**  
Criar endpoint POST /login, validar credenciais, verificar hash de senha e retornar token JWT com dados do usuário.

**Parte do Projeto Construída:** Endpoint /login funcional e seguro

---

### **Tópico 3: Endpoint de Registro - Validação e Criação (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Validação Robusta:**  
Implementação do endpoint /register com validações específicas para psicólogos (CRP) e pacientes, prevenção de duplicatas.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar registro seguro de usuários  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Orientado a Regras:**  
Criar endpoint POST /register, validar dados únicos (email, CRP), hash de senha e criação segura de usuários.

**Parte do Projeto Construída:** Endpoint /register com validações completas

---

### **Tópico 4: Serviço de Autenticação e Tratamento de Erros (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Arquitetura de Serviços:**  
Implementação do auth_service.py, separação de responsabilidades e tratamento robusto de erros de autenticação.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Criar camada de serviço e tratamento de erros  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação por Camadas:**  
Implementar auth_service.py, funções de validação, dependency para usuário atual e tratamento de exceções HTTP.

**Parte do Projeto Construída:** Serviço de autenticação completo com tratamento de erros

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Análise de Vulnerabilidades:**  
Reflexão sobre ataques comuns (brute force, credential stuffing) e como as implementações realizadas protegem contra essas ameaças.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio de Integração:**  
Pensar em como proteger endpoints de pacientes usando a autenticação implementada. Como garantir que apenas o psicólogo responsável acesse dados do paciente?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação FastAPI Security  
- Guia OWASP Authentication  
- Boas práticas de autenticação em sistemas médicos  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Implementação correta dos endpoints de login e registro  
✅ Validação adequada de credenciais e dados únicos  
✅ Tratamento robusto de erros de autenticação  
✅ Integração funcional com JWT e dependency injection  

### **Avaliação Somativa (Entregáveis):**
✅ Router auth.py completo e funcional  
✅ Serviço auth_service.py implementado  
✅ Endpoints testados e validados via Swagger  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Autenticação segura completa, tratamento robusto de erros, código seguindo boas práticas de segurança  
- **Bom (7-8):** Funcionalidades implementadas corretamente com pequenos ajustes de segurança  
- **Satisfatório (6-7):** Implementação básica mas com melhorias necessárias na validação  
- **Insatisfatório (<6):** Vulnerabilidades de segurança ou falhas na autenticação  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de implementação de autenticação JWT em FastAPI  
- Compreensão de validação segura de credenciais  
- Conhecimento de tratamento de erros de segurança  

🎯 **Aplicação Prática:**  
- Capacidade de desenvolver sistemas de login seguros  
- Habilidade para implementar validações robustas  
- Competência em arquitetura de serviços de autenticação  

🎯 **Competências Profissionais:**  
- Desenvolvimento orientado à segurança  
- Consciência sobre proteção de dados médicos  
- Aplicação de boas práticas de autenticação  

### **Conexão com o Projeto:**  
Esta aula implementa o sistema de autenticação central do Lunysse, permitindo que psicólogos e pacientes façam login seguro e acessem funcionalidades específicas do sistema de agendamento psicológico.

### **Preparação para Próxima Aula:**  
O sistema de autenticação será utilizado na próxima aula para implementar o CRUD completo de pacientes, aplicando proteção de rotas e garantindo que apenas psicólogos autorizados possam gerenciar seus pacientes.