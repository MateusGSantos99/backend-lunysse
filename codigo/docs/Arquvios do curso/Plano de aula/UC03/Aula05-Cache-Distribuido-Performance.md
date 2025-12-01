# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Cache Distribuído e Performance

📌 **Disciplina:** Desenvolver Serviços Web  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 5  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Configuração e integração do Redis  
- Implementação de cache para consultas frequentes  
- Estratégias de invalidação de cache  
- Monitoramento de performance e métricas  
- Otimização de manipulação de registros com cache  

### 🎯 Objetivo Geral
Implementar sistema de cache distribuído com Redis para otimizar performance da API Lunysse, melhorando manipulação de registros e validação de regras de negócio

### 💡 Habilidades e Competências
✅ Configurar e integrar Redis em aplicações FastAPI  
✅ Implementar estratégias eficientes de cache  
✅ Desenvolver sistemas de invalidação inteligente  
✅ Monitorar e otimizar performance de aplicações web  

### 📌 Materiais Necessários
📌 Sistema Lunysse com frontend da aula anterior  
📌 Redis Server instalado  
📌 Biblioteca redis-py ou aioredis  
📌 Ferramentas de monitoramento (Redis CLI, Redis Insight)  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (20min)
**Metodologia Ativa - Análise de Performance:**  
"Como melhorar o tempo de resposta da API quando há muitos usuários simultâneos? Como reduzir carga no banco de dados sem perder consistência?" Discussão sobre gargalos de performance e soluções de cache.

---

### **Tópico 1: Configuração e Integração do Redis (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Setup Guiado:**  
Instalação do Redis, configuração no FastAPI, criação de cliente Redis, estruturação de chaves e namespaces para organização.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Configurar Redis integrado ao sistema Lunysse  
📝 **Tarefa:**  
- **Metodologia Ativa - Configuração Colaborativa:**  
Instalar Redis, criar serviço CacheService com conexão configurável, implementar health check do Redis na API.

**Parte do Projeto Construída:** Redis integrado e configurado no sistema

---

### **Tópico 2: Implementação de Cache para Consultas Críticas (80min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Otimização Prática:**  
Identificação de endpoints com alta frequência de acesso, implementação de cache para listagem de pacientes, agendamentos e relatórios.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar cache em endpoints críticos  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Orientado a Performance:**  
Criar decoradores de cache, implementar cache em GET /patients/, /appointments/, /reports/, configurar TTL apropriado para cada tipo de dados.

**Parte do Projeto Construída:** Sistema de cache funcional em endpoints críticos

---

### **Tópico 3: Estratégias de Invalidação Inteligente (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Gerenciamento de Consistência:**  
Implementação de invalidação automática em operações CRUD, cache tags para invalidação em grupo, estratégias de refresh proativo.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar invalidação automática de cache  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Consistência:**  
Criar sistema de invalidação em POST/PUT/DELETE, implementar cache tags por entidade, configurar refresh automático para dados críticos.

**Parte do Projeto Construída:** Sistema de invalidação inteligente implementado

---

### **Tópico 4: Monitoramento e Métricas de Performance (20min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Análise de Métricas:**  
Implementação de métricas de hit/miss ratio, tempo de resposta, monitoramento de uso de memória Redis, dashboard de performance.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar monitoramento completo de cache  
📝 **Tarefa:**  
- **Metodologia Ativa - Otimização Baseada em Dados:**  
Criar endpoint /metrics com estatísticas de cache, implementar logs de performance, configurar alertas para baixo hit ratio.

**Parte do Projeto Construída:** Sistema de monitoramento de performance implementado

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Avaliação de Resultados:**  
Análise dos ganhos de performance obtidos, discussão sobre trade-offs entre consistência e performance, estratégias para diferentes cenários.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Preparação Arquitetural:**  
Pesquisar arquiteturas de microserviços e ferramentas de comunicação entre serviços (HTTP, gRPC, message queues).

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação Redis oficial  
- Exemplos de estratégias de cache  
- Ferramentas de monitoramento Redis  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Qualidade da configuração e integração Redis  
✅ Eficiência das estratégias de cache implementadas  
✅ Adequação das políticas de invalidação  
✅ Completude do sistema de monitoramento  

### **Avaliação Somativa (Entregáveis):**
✅ Redis integrado e configurado corretamente  
✅ Cache implementado em endpoints críticos  
✅ Sistema de invalidação automática funcionando  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Cache otimizado, invalidação inteligente, monitoramento completo, ganhos significativos de performance  
- **Bom (7-8):** Cache funcional, invalidação básica, métricas implementadas  
- **Satisfatório (6-7):** Cache básico funcionando, configuração adequada  
- **Insatisfatório (<6):** Dificuldades na implementação ou configuração incorreta  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de Redis e cache distribuído  
- Estratégias de otimização de performance  
- Monitoramento de sistemas web  

🎯 **Aplicação Prática:**  
- Sistema Lunysse otimizado com cache  
- Redução significativa no tempo de resposta  
- Base para escalabilidade horizontal  

🎯 **Competências Profissionais:**  
- Otimização de performance em produção  
- Análise de gargalos de sistema  
- Implementação de soluções escaláveis  

### **Conexão com o Projeto:**  
Esta aula otimiza o sistema Lunysse para suportar maior carga de usuários, preparando-o para ambiente de produção e estabelecendo base para arquitetura de microserviços.

### **Preparação para Próxima Aula:**  
O sistema otimizado será expandido com microserviço independente para relatórios, implementando comunicação entre serviços e processamento assíncrono.