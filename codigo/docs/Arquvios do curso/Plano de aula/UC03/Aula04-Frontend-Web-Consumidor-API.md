# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Frontend Web Consumidor da API

📌 **Disciplina:** Desenvolver Serviços Web  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 4  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Desenvolvimento de SPA (Single Page Application)  
- Implementação de autenticação JWT no frontend  
- Consumo de endpoints da API com fetch/axios  
- Interface responsiva para agendamentos e relatórios  
- Estruturas de segurança e controle de acesso no frontend  

### 🎯 Objetivo Geral
Desenvolver interface web completa que consome a API Lunysse, implementando autenticação segura e controle de acesso por perfis de usuário

### 💡 Habilidades e Competências
✅ Consumir APIs REST de forma segura no frontend  
✅ Implementar autenticação JWT em aplicações web  
✅ Criar interfaces responsivas e acessíveis  
✅ Estruturar código frontend para consumo de serviços web  

### 📌 Materiais Necessários
📌 API Lunysse com notificações da aula anterior  
📌 Editor de código (VSCode)  
📌 Navegador web moderno  
📌 Biblioteca CSS (Bootstrap ou similar)  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (20min)
**Metodologia Ativa - Problematização:**  
"Como criar uma interface web que permita psicólogos e pacientes acessarem o sistema de forma segura e intuitiva? Como garantir que dados sensíveis sejam protegidos no frontend?" Discussão sobre segurança e UX em sistemas de saúde.

---

### **Tópico 1: Estruturação da SPA e Arquitetura Frontend (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Arquitetura Guiada:**  
Estruturação de SPA com HTML5, organização de módulos JavaScript, configuração de roteamento client-side, estrutura de componentes.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar estrutura base da aplicação web  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Colaborativo:**  
Criar estrutura HTML com páginas (login, dashboard, agendamentos, pacientes), configurar CSS responsivo e JavaScript modular.

**Parte do Projeto Construída:** Estrutura base da SPA com navegação

---

### **Tópico 2: Implementação de Autenticação JWT (80min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding Seguro:**  
Implementação de login/logout, armazenamento seguro de tokens, interceptação de requisições, controle de sessão e redirecionamentos.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar sistema completo de autenticação  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação Segura:**  
Criar módulo auth.js com funções de login, logout, verificação de token, implementar middleware para rotas protegidas.

**Parte do Projeto Construída:** Sistema de autenticação JWT funcional no frontend

---

### **Tópico 3: Consumo de Endpoints e Manipulação de Dados (70min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Integração API:**  
Consumo de endpoints com fetch/axios, tratamento de respostas e erros, manipulação de dados JSON, atualização dinâmica da interface.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar consumo completo da API Lunysse  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Full-Stack:**  
Criar módulo api.js para consumir endpoints (pacientes, agendamentos, relatórios), implementar CRUD completo na interface.

**Parte do Projeto Construída:** Interface completa consumindo API Lunysse

---

### **Tópico 4: Controle de Acesso e Segurança por Perfis (30min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Implementação de Segurança:**  
Controle de acesso baseado em roles (psicólogo/paciente), ocultação de funcionalidades por perfil, validação de permissões no frontend.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar controle de acesso granular  
📝 **Tarefa:**  
- **Metodologia Ativa - Segurança por Design:**  
Implementar sistema de permissões no frontend, criar componentes específicos por perfil, validar acesso a funcionalidades sensíveis.

**Parte do Projeto Construída:** Sistema de controle de acesso por perfis implementado

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Avaliação de Segurança:**  
Análise da segurança implementada, discussão sobre boas práticas de frontend, avaliação da experiência do usuário criada.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Preparação Técnica:**  
Pesquisar Redis e estratégias de cache, analisar gargalos de performance na aplicação desenvolvida.

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação da API Lunysse (Swagger)  
- Exemplos de SPAs seguras  
- Guias de boas práticas de segurança frontend  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Qualidade da estruturação da SPA  
✅ Implementação segura da autenticação JWT  
✅ Eficiência do consumo de API  
✅ Adequação do controle de acesso por perfis  

### **Avaliação Somativa (Entregáveis):**
✅ SPA funcional com navegação completa  
✅ Sistema de autenticação JWT implementado  
✅ Interface consumindo todos os endpoints da API  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Interface profissional, segurança robusta, UX excelente, controle de acesso completo  
- **Bom (7-8):** Interface funcional, autenticação adequada, consumo de API eficiente  
- **Satisfatório (6-7):** SPA básica funcionando, login/logout implementado  
- **Insatisfatório (<6):** Dificuldades na implementação ou problemas de segurança  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Desenvolvimento de SPAs modernas  
- Autenticação JWT no frontend  
- Consumo seguro de APIs REST  

🎯 **Aplicação Prática:**  
- Interface completa para sistema Lunysse  
- Controle de acesso por perfis  
- Experiência de usuário profissional  

🎯 **Competências Profissionais:**  
- Segurança em aplicações web  
- Integração frontend-backend  
- Design de interfaces responsivas  

### **Conexão com o Projeto:**  
Esta aula completa o ciclo de desenvolvimento full-stack do sistema Lunysse, criando interface de usuário que consome todas as funcionalidades desenvolvidas nas aulas anteriores.

### **Preparação para Próxima Aula:**  
A aplicação completa será otimizada com sistema de cache Redis para melhorar performance e escalabilidade do sistema integrado.