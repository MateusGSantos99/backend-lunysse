# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Sistema de Notificações Externas

📌 **Disciplina:** Desenvolver Serviços Web  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 3  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Integração com SendGrid para envio de emails  
- Configuração de templates de email responsivos  
- Implementação de fila de notificações assíncronas  
- Sistema de logs e monitoramento de entregas  
- Estruturas de dados para controle de notificações  

### 🎯 Objetivo Geral
Implementar sistema completo de notificações via email usando serviços externos, criando estruturas robustas de código e schemas para gerenciamento de comunicação com pacientes

### 💡 Habilidades e Competências
✅ Integrar serviços de email externos de forma segura  
✅ Criar estruturas de dados para controle de notificações  
✅ Implementar processamento assíncrono de tarefas  
✅ Desenvolver sistema de logs e monitoramento  

### 📌 Materiais Necessários
📌 Conta SendGrid configurada  
📌 Sistema Lunysse com integração ViaCEP da aula anterior  
📌 Biblioteca Celery ou FastAPI BackgroundTasks  
📌 Templates HTML para emails  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (20min)
**Metodologia Ativa - Problematização:**  
"Como notificar pacientes sobre agendamentos de forma automática e profissional? Como garantir que emails sejam entregues e monitorar falhas?" Discussão sobre comunicação automatizada em sistemas de saúde.

---

### **Tópico 1: Estruturação de Dados para Notificações (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Modelagem de Dados:**  
Criação de modelos Notification e EmailTemplate, schemas Pydantic para validação, estruturas para controle de status de entrega.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar estrutura completa de dados para notificações  
📝 **Tarefa:**  
- **Metodologia Ativa - Design de Estruturas:**  
Implementar modelos Notification (id, type, recipient, status, created_at) e EmailTemplate (id, name, subject, body_html), criar schemas Pydantic correspondentes.

**Parte do Projeto Construída:** Estrutura de dados robusta para sistema de notificações

---

### **Tópico 2: Integração com SendGrid (70min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding:**  
Configuração da API SendGrid, implementação de serviço de email com templates dinâmicos, tratamento de erros e validação de respostas.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar serviço completo de envio de emails  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação em Pares:**  
Criar EmailService com métodos send_appointment_confirmation, send_reminder, configurar templates HTML responsivos e integração SendGrid.

**Parte do Projeto Construída:** Serviço de email funcional com SendGrid

---

### **Tópico 3: Sistema de Fila Assíncrona (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Implementação Guiada:**  
Configuração de BackgroundTasks do FastAPI, implementação de fila de notificações, processamento assíncrono para não bloquear API.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar processamento assíncrono de notificações  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Problemas:**  
Criar NotificationService com fila assíncrona, integrar com endpoints de agendamento para envio automático de confirmações.

**Parte do Projeto Construída:** Sistema de fila assíncrona para notificações

---

### **Tópico 4: Logs e Monitoramento de Entregas (30min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Implementação de Monitoramento:**  
Sistema de logs estruturados, webhook do SendGrid para status de entrega, dashboard de monitoramento de emails.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar monitoramento completo de entregas  
📝 **Tarefa:**  
- **Metodologia Ativa - Controle de Qualidade:**  
Criar endpoint para webhook SendGrid, implementar logs de entrega, criar endpoint para consultar status de notificações.

**Parte do Projeto Construída:** Sistema completo de monitoramento de notificações

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Avaliação de Resultados:**  
Análise da robustez do sistema de notificações, discussão sobre LGPD e privacidade em comunicações médicas, estratégias de fallback.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Preparação Ativa:**  
Pesquisar frameworks frontend (React, Vue, Vanilla JS) e planejar estrutura de SPA que consumirá a API Lunysse.

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação SendGrid API  
- Templates HTML responsivos para emails  
- Exemplos de sistemas de notificação  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Qualidade da estruturação de dados para notificações  
✅ Implementação robusta da integração SendGrid  
✅ Eficiência do sistema de fila assíncrona  
✅ Completude do sistema de monitoramento  

### **Avaliação Somativa (Entregáveis):**
✅ Modelos e schemas de notificação implementados  
✅ Serviço de email funcional com templates  
✅ Sistema de fila assíncrona operacional  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Sistema completo, templates profissionais, monitoramento robusto, processamento assíncrono eficiente  
- **Bom (7-8):** Integração funcional, templates adequados, sistema básico de monitoramento  
- **Satisfatório (6-7):** Envio de emails funcionando, estruturas básicas implementadas  
- **Insatisfatório (<6):** Dificuldades na integração ou estruturação do sistema  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Integração com serviços de email externos  
- Estruturação de dados para notificações  
- Processamento assíncrono de tarefas  

🎯 **Aplicação Prática:**  
- Sistema Lunysse com notificações automáticas  
- Templates profissionais de email  
- Monitoramento de entregas implementado  

🎯 **Competências Profissionais:**  
- Criação de estruturas robustas de código  
- Integração segura com serviços externos  
- Implementação de sistemas de monitoramento  

### **Conexão com o Projeto:**  
Esta aula adiciona capacidade de comunicação automatizada ao sistema Lunysse, melhorando a experiência do usuário e criando estruturas que serão consumidas pelo frontend.

### **Preparação para Próxima Aula:**  
As estruturas de notificação e APIs criadas serão consumidas por um frontend web responsivo, implementando interface completa para usuários finais.