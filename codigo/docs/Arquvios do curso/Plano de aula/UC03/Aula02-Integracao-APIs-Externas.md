# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Integração com APIs Externas

📌 **Disciplina:** Desenvolver Serviços Web  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 2  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Integração com API ViaCEP para consulta de endereços  
- Configuração de cliente HTTP com httpx/requests  
- Implementação de tratamento de erros e timeout  
- Cache de respostas externas para otimização  
- Extensão do banco de dados para armazenar dados externos  

### 🎯 Objetivo Geral
Integrar serviços web externos para enriquecer funcionalidades do sistema Lunysse, implementando consulta de CEP e estruturando banco de dados para armazenar informações externas

### 💡 Habilidades e Competências
✅ Consumir APIs REST externas de forma robusta  
✅ Implementar tratamento de erros e timeouts adequados  
✅ Estruturar banco de dados para dados externos  
✅ Aplicar cache para otimização de performance  

### 📌 Materiais Necessários
📌 Sistema Lunysse versionado da aula anterior  
📌 Documentação da API ViaCEP  
📌 Biblioteca httpx ou requests  
📌 Ferramenta de teste de API (Postman/Insomnia)  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (20min)
**Metodologia Ativa - Problematização:**  
"Como enriquecer os dados de pacientes automaticamente? Como garantir que falhas em serviços externos não quebrem nosso sistema?" Discussão sobre integração robusta com APIs externas.

---

### **Tópico 1: Análise e Estruturação do Banco para Dados Externos (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Modelagem Colaborativa:**  
Análise da necessidade de armazenar dados de endereço completos, criação de modelo Address e relacionamento com Patient.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Estender modelo de dados para endereços completos  
📝 **Tarefa:**  
- **Metodologia Ativa - Design de Banco de Dados:**  
Criar modelo Address com campos (cep, logradouro, bairro, cidade, uf, complemento) e relacionar com Patient, implementar migration.

**Parte do Projeto Construída:** Estrutura de banco estendida para dados de endereço

---

### **Tópico 2: Implementação do Cliente HTTP (70min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding:**  
Configuração do httpx, implementação de cliente HTTP com timeout, retry e tratamento de erros para consumir API ViaCEP.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Criar serviço robusto de consulta de CEP  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação em Pares:**  
Implementar serviço external_services.py com classe ViaCEPService, incluindo validação de CEP, tratamento de erros HTTP e timeout.

**Parte do Projeto Construída:** Serviço de integração com ViaCEP funcional

---

### **Tópico 3: Integração com Endpoints Existentes (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Integração Guiada:**  
Modificação dos endpoints de pacientes para consumir ViaCEP automaticamente ao receber CEP, atualização de schemas Pydantic.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Integrar consulta de CEP no cadastro de pacientes  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Problemas:**  
Modificar endpoint POST /patients/ para consultar CEP automaticamente, atualizar schemas e implementar validação de endereço.

**Parte do Projeto Construída:** Cadastro de pacientes com consulta automática de CEP

---

### **Tópico 4: Cache e Otimização (30min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Otimização Prática:**  
Implementação de cache em memória para CEPs consultados, estratégias de invalidação e monitoramento de hit rate.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar cache para otimizar consultas repetidas  
📝 **Tarefa:**  
- **Metodologia Ativa - Melhoria de Performance:**  
Adicionar cache em memória no serviço ViaCEP, implementar TTL e métricas de cache hit/miss.

**Parte do Projeto Construída:** Sistema de cache para consultas externas

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Análise de Resultados:**  
Discussão sobre robustez da integração, impacto no banco de dados, estratégias de fallback para falhas de API externa.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Preparação Ativa:**  
Pesquisar APIs de notificação (SendGrid, Twilio) e documentar estruturas de dados necessárias para sistema de notificações.

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação API ViaCEP  
- Exemplos de integração HTTP robusta  
- Padrões de tratamento de erro em APIs  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Qualidade da modelagem de dados para endereços  
✅ Implementação robusta do cliente HTTP  
✅ Integração eficiente com endpoints existentes  
✅ Estratégias adequadas de cache e otimização  

### **Avaliação Somativa (Entregáveis):**
✅ Modelo Address implementado e relacionado  
✅ Serviço ViaCEP funcional com tratamento de erros  
✅ Cadastro de pacientes com consulta automática de CEP  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Integração robusta, banco bem estruturado, cache implementado, tratamento completo de erros  
- **Bom (7-8):** Integração funcional, modelo adequado, tratamento básico de erros  
- **Satisfatório (6-7):** Integração básica funcionando, estrutura de dados criada  
- **Insatisfatório (<6):** Dificuldades na integração ou estruturação do banco  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Integração robusta com APIs externas  
- Estruturação de banco para dados externos  
- Técnicas de cache e otimização  

🎯 **Aplicação Prática:**  
- Sistema Lunysse enriquecido com dados de endereço  
- Consulta automática de CEP no cadastro  
- Base para futuras integrações externas  

🎯 **Competências Profissionais:**  
- Consumo seguro de APIs externas  
- Modelagem de dados para integração  
- Otimização de performance com cache  

### **Conexão com o Projeto:**  
Esta aula expande o sistema Lunysse com capacidades de integração externa, preparando a base para futuras integrações com serviços de notificação e outros APIs.

### **Preparação para Próxima Aula:**  
A estrutura de integração criada será expandida para implementar sistema de notificações via email usando SendGrid, incluindo templates e filas assíncronas.