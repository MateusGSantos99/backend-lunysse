# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Microserviço de Relatórios

📌 **Disciplina:** Desenvolver Serviços Web  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 6  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Criação de microserviço separado para relatórios  
- Comunicação entre serviços via HTTP/gRPC  
- Geração de PDFs e planilhas Excel  
- Processamento assíncrono de relatórios pesados  
- Workflows complexos e gerenciamento de estados  

### 🎯 Objetivo Geral
Desenvolver microserviço independente para geração de relatórios complexos, implementando workflows avançados e comunicação entre serviços distribuídos

### 💡 Habilidades e Competências
✅ Arquitetar e desenvolver microserviços independentes  
✅ Implementar comunicação eficiente entre serviços  
✅ Criar workflows complexos de processamento  
✅ Gerenciar estados de solicitações distribuídas  

### 📌 Materiais Necessários
📌 Sistema Lunysse com cache da aula anterior  
📌 Bibliotecas ReportLab (PDF) e openpyxl (Excel)  
📌 Celery ou FastAPI BackgroundTasks  
📌 Message broker (Redis/RabbitMQ)  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (20min)
**Metodologia Ativa - Arquitetura Distribuída:**  
"Como separar funcionalidades pesadas em serviços independentes? Como garantir comunicação eficiente entre microserviços mantendo baixo acoplamento?" Discussão sobre arquitetura de microserviços e suas vantagens.

---

### **Tópico 1: Arquitetura e Criação do Microserviço (70min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Design de Arquitetura:**  
Planejamento da arquitetura distribuída, criação de projeto separado para relatórios, definição de contratos de comunicação entre serviços.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar microserviço independente de relatórios  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Distribuído:**  
Criar projeto lunysse-reports separado, implementar estrutura FastAPI independente, definir modelos de dados específicos para relatórios.

**Parte do Projeto Construída:** Microserviço de relatórios estruturado e independente

---

### **Tópico 2: Comunicação Entre Serviços (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Integração de Serviços:**  
Implementação de cliente HTTP para comunicação com API principal, autenticação entre serviços, tratamento de falhas e retry policies.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar comunicação robusta entre serviços  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação Distribuída:**  
Criar LunysseAPIClient no microserviço, implementar autenticação service-to-service, configurar circuit breaker para resiliência.

**Parte do Projeto Construída:** Comunicação robusta entre microserviços implementada

---

### **Tópico 3: Geração de Relatórios PDF e Excel (70min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Desenvolvimento de Funcionalidades:**  
Implementação de geradores PDF com ReportLab, criação de planilhas Excel com openpyxl, templates dinâmicos para diferentes tipos de relatórios.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar geração completa de relatórios  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Problemas Complexos:**  
Criar ReportGenerator com métodos para PDF e Excel, implementar templates para relatórios de pacientes, agendamentos e estatísticas ML.

**Parte do Projeto Construída:** Sistema completo de geração de relatórios PDF/Excel

---

### **Tópico 4: Processamento Assíncrono e Workflows (20min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Gerenciamento de Estados:**  
Implementação de fila de processamento, estados de relatórios (pending, processing, completed, failed), notificações de conclusão.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar workflow completo de relatórios  
📝 **Tarefa:**  
- **Metodologia Ativa - Orquestração de Processos:**  
Criar sistema de filas com Celery, implementar estados de relatórios, integrar notificações via email quando relatório estiver pronto.

**Parte do Projeto Construída:** Workflow completo de processamento assíncrono

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Avaliação Arquitetural:**  
Análise da arquitetura distribuída criada, discussão sobre vantagens e desafios dos microserviços, estratégias de monitoramento distribuído.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Preparação para Testes:**  
Identificar cenários de teste para sistema distribuído, pesquisar ferramentas de teste de integração e end-to-end.

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Padrões de arquitetura de microserviços  
- Documentação ReportLab e openpyxl  
- Exemplos de comunicação entre serviços  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Qualidade da arquitetura do microserviço  
✅ Eficiência da comunicação entre serviços  
✅ Funcionalidade dos geradores de relatórios  
✅ Robustez do workflow assíncrono  

### **Avaliação Somativa (Entregáveis):**
✅ Microserviço de relatórios independente e funcional  
✅ Comunicação robusta entre serviços implementada  
✅ Geração de PDFs e Excel funcionando  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Arquitetura bem projetada, comunicação resiliente, relatórios profissionais, workflow completo  
- **Bom (7-8):** Microserviço funcional, comunicação adequada, relatórios básicos gerados  
- **Satisfatório (6-7):** Serviço separado criado, comunicação básica funcionando  
- **Insatisfatório (<6):** Dificuldades na separação de serviços ou comunicação  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Arquitetura de microserviços  
- Comunicação entre serviços distribuídos  
- Processamento assíncrono avançado  

🎯 **Aplicação Prática:**  
- Sistema Lunysse com arquitetura distribuída  
- Relatórios profissionais em PDF/Excel  
- Workflows complexos implementados  

🎯 **Competências Profissionais:**  
- Design de sistemas distribuídos  
- Gerenciamento de estados complexos  
- Integração de serviços independentes  

### **Conexão com o Projeto:**  
Esta aula evolui o sistema Lunysse para arquitetura de microserviços, separando responsabilidades e criando base para escalabilidade horizontal e manutenibilidade.

### **Preparação para Próxima Aula:**  
O sistema distribuído será validado com testes de integração e end-to-end, garantindo qualidade e confiabilidade da arquitetura implementada.