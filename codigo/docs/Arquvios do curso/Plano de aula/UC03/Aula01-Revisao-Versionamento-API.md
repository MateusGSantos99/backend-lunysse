# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Revisão e Versionamento da API Existente

📌 **Disciplina:** Desenvolver Serviços Web  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 1  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Revisão completa do sistema Lunysse desenvolvido na UC anterior  
- Conceitos e implementação de versionamento de APIs  
- Configuração de CORS para integração com frontend  
- Técnicas de refatoração e otimização de performance  
- Backward compatibility e migração de versões  

### 🎯 Objetivo Geral
Revisar o sistema Lunysse desenvolvido na UC anterior e implementar versionamento profissional de API com foco em escalabilidade e manutenibilidade

### 💡 Habilidades e Competências
✅ Analisar e revisar código existente de forma crítica  
✅ Implementar versionamento de API seguindo padrões de mercado  
✅ Configurar CORS para integração segura com frontends  
✅ Aplicar técnicas de refatoração para melhorar qualidade do código  

### 📌 Materiais Necessários
📌 Sistema Lunysse desenvolvido na UC anterior  
📌 Postman/Insomnia para testes de API  
📌 Git para controle de versão  
📌 Documentação de versionamento de APIs  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Problematização:**  
"Como garantir que mudanças na API não quebrem sistemas que já a utilizam? Como permitir evolução contínua mantendo compatibilidade?" Discussão sobre a importância do versionamento em APIs de produção.

---

### **Tópico 1: Revisão Crítica do Sistema Lunysse (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Code Review Colaborativo:**  
Análise detalhada do código desenvolvido na UC anterior, identificação de pontos de melhoria, discussão sobre arquitetura e padrões implementados.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Documentar estado atual e identificar melhorias  
📝 **Tarefa:**  
- **Metodologia Ativa - Análise Colaborativa:**  
Cada equipe analisa um módulo do sistema (auth, patients, appointments, etc.) e documenta funcionalidades, dependências e pontos de melhoria.

**Parte do Projeto Construída:** Documentação técnica do estado atual do sistema

---

### **Tópico 2: Implementação de Versionamento de API (80min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding:**  
Implementação de versionamento usando prefixos de rota (/api/v1/, /api/v2/), headers de versão e estratégias de deprecação.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar sistema de versionamento completo  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação em Pares:**  
Refatorar estrutura de rotas para suportar versionamento, criar v1 (atual) e v2 (melhorada) de endpoints críticos.

**Parte do Projeto Construída:** Sistema de versionamento funcional com v1 e v2

---

### **Tópico 3: Configuração de CORS e Segurança (50min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração Interativa:**  
Configuração de CORS no FastAPI, políticas de origem, headers permitidos, e integração segura com diferentes tipos de frontend.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Configurar CORS para integração frontend  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Problemas:**  
Implementar configuração CORS flexível que permita desenvolvimento local e produção, testando com diferentes origens.

**Parte do Projeto Construída:** Configuração CORS robusta e segura

---

### **Tópico 4: Refatoração e Otimização (30min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Refatoração Guiada:**  
Técnicas de refatoração: extração de funções, eliminação de código duplicado, otimização de queries, melhoria de nomenclatura.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Aplicar melhorias identificadas na revisão  
📝 **Tarefa:**  
- **Metodologia Ativa - Melhoria Contínua:**  
Implementar refatorações prioritárias identificadas na análise inicial, focando em performance e legibilidade.

**Parte do Projeto Construída:** Código refatorado e otimizado

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Retrospectiva:**  
Reflexão sobre melhorias implementadas, discussão sobre impacto do versionamento na manutenibilidade, próximos passos de evolução.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Preparação Ativa:**  
Pesquisar APIs públicas que utilizam versionamento (GitHub, Twitter, Stripe) e documentar estratégias utilizadas.

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Código do sistema Lunysse da UC anterior  
- Documentação de boas práticas de versionamento  
- Exemplos de APIs versionadas do mercado  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Qualidade da análise crítica do código existente  
✅ Compreensão dos conceitos de versionamento  
✅ Implementação correta da estrutura versionada  
✅ Configuração adequada de CORS e segurança  

### **Avaliação Somativa (Entregáveis):**
✅ Documentação técnica do estado atual do sistema  
✅ Sistema de versionamento v1/v2 implementado  
✅ Configuração CORS funcional e testada  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Análise profunda, versionamento completo, CORS configurado perfeitamente  
- **Bom (7-8):** Boa análise, versionamento funcional, CORS básico implementado  
- **Satisfatório (6-7):** Análise básica realizada, conceitos de versionamento compreendidos  
- **Insatisfatório (<6):** Dificuldades na análise ou implementação do versionamento  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de versionamento de APIs  
- Compreensão de CORS e segurança web  
- Técnicas de refatoração e otimização  

🎯 **Aplicação Prática:**  
- Sistema Lunysse versionado e otimizado  
- Configuração para integração frontend  
- Base sólida para evoluções futuras  

🎯 **Competências Profissionais:**  
- Análise crítica de código  
- Planejamento de evolução de sistemas  
- Manutenibilidade e escalabilidade  

### **Conexão com o Projeto:**  
Esta aula prepara o sistema Lunysse para as integrações e evoluções que serão implementadas nas próximas aulas, estabelecendo uma base sólida e versionada.

### **Preparação para Próxima Aula:**  
O sistema versionado será expandido com integração de APIs externas, começando pela integração com a API ViaCEP para enriquecimento de dados de endereço.