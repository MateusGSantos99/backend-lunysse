# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Monitoramento e Observabilidade

📌 **Disciplina:** Desenvolver Serviços Web  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 8  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Configuração de logs estruturados com Loguru  
- Implementação de métricas com Prometheus  
- Sistema de alertas e notificações  
- Dashboard de monitoramento em tempo real  
- Integração de observabilidade com análises ML  

### 🎯 Objetivo Geral
Implementar sistema completo de monitoramento e observabilidade da API, integrando serviços de terceiros para análises preditivas e combinando diferentes tecnologias em solução única

### 💡 Habilidades e Competências
✅ Configurar sistemas de logging estruturado  
✅ Implementar métricas e monitoramento de performance  
✅ Integrar ferramentas de observabilidade externas  
✅ Criar dashboards para análises preditivas  

### 📌 Materiais Necessários
📌 Sistema Lunysse testado da aula anterior  
📌 Loguru para logging estruturado  
📌 Prometheus e Grafana  
📌 Ferramentas de APM (Application Performance Monitoring)  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (20min)
**Metodologia Ativa - Análise de Produção:**  
"Como saber se o sistema está funcionando bem em produção? Como detectar problemas antes que afetem os usuários? Como usar dados de monitoramento para melhorar análises de ML?" Discussão sobre observabilidade em sistemas críticos.

---

### **Tópico 1: Logs Estruturados e Observabilidade (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Instrumentação Guiada:**  
Configuração do Loguru, estruturação de logs JSON, correlação de logs entre microserviços, integração com análises ML para detecção de padrões.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Implementar logging estruturado integrado com ML  
📝 **Tarefa:**  
- **Metodologia Ativa - Instrumentação Inteligente:**  
Configurar Loguru com formato JSON, implementar correlation IDs, criar logs específicos para análises ML de comportamento de usuários.

**Parte do Projeto Construída:** Sistema de logging estruturado com integração ML

---

### **Tópico 2: Métricas e Prometheus (70min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Monitoramento Ativo:**  
Configuração do Prometheus, criação de métricas customizadas, instrumentação de endpoints, métricas específicas para análises preditivas.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar métricas completas com foco em ML  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Orientado a Métricas:**  
Implementar métricas de performance, uso de cache, análises ML, criar endpoints /metrics, configurar coleta automática.

**Parte do Projeto Construída:** Sistema de métricas Prometheus com análises ML

---

### **Tópico 3: Dashboards e Visualização Inteligente (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Visualização de Dados:**  
Configuração do Grafana, criação de dashboards para sistema distribuído, painéis específicos para análises ML e predições.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Criar dashboards integrados com análises preditivas  
📝 **Tarefa:**  
- **Metodologia Ativa - Análise Visual Inteligente:**  
Criar dashboards para monitoramento geral, painel específico para análises ML de risco, alertas baseados em predições.

**Parte do Projeto Construída:** Dashboards completos com análises preditivas

---

### **Tópico 4: Alertas e Integração com Serviços Externos (30min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Automação de Alertas:**  
Configuração de alertas inteligentes, integração com Slack/Discord, alertas baseados em análises ML, escalação automática.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar sistema de alertas inteligente  
📝 **Tarefa:**  
- **Metodologia Ativa - Resposta Automatizada:**  
Configurar alertas para métricas críticas, integrar com serviços de notificação externos, criar alertas baseados em predições ML.

**Parte do Projeto Construída:** Sistema de alertas integrado com análises preditivas

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Análise de Observabilidade:**  
Avaliação da visibilidade obtida do sistema, discussão sobre correlação entre métricas e análises ML, estratégias de melhoria contínua.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Preparação para Deploy:**  
Pesquisar plataformas de deploy (Railway, Heroku, AWS) e estratégias de CI/CD para sistemas distribuídos.

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação Prometheus e Grafana  
- Exemplos de dashboards para sistemas de saúde  
- Boas práticas de observabilidade  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Qualidade da configuração de logs estruturados  
✅ Eficiência das métricas implementadas  
✅ Funcionalidade dos dashboards criados  
✅ Integração adequada com análises ML  

### **Avaliação Somativa (Entregáveis):**
✅ Sistema de logging estruturado funcionando  
✅ Métricas Prometheus coletando dados  
✅ Dashboards Grafana operacionais  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Observabilidade completa, dashboards profissionais, alertas inteligentes, integração ML eficiente  
- **Bom (7-8):** Monitoramento funcional, dashboards adequados, métricas coletadas  
- **Satisfatório (6-7):** Logs e métricas básicas implementadas  
- **Insatisfatório (<6):** Dificuldades na implementação ou configuração inadequada  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Observabilidade de sistemas distribuídos  
- Integração de monitoramento com ML  
- Dashboards e alertas inteligentes  

🎯 **Aplicação Prática:**  
- Sistema Lunysse completamente observável  
- Análises preditivas integradas ao monitoramento  
- Detecção proativa de problemas  

🎯 **Competências Profissionais:**  
- Operação de sistemas em produção  
- Análise de dados de monitoramento  
- Integração de tecnologias diversas  

### **Conexão com o Projeto:**  
Esta aula prepara o sistema Lunysse para produção com observabilidade completa, integrando análises ML ao monitoramento para detecção inteligente de padrões e problemas.

### **Preparação para Próxima Aula:**  
O sistema monitorado será deployado em ambiente de produção com pipeline CI/CD automatizado, completando o ciclo de desenvolvimento profissional.