# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Testes, Validações e Seed Data

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 13  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Criação do seed_data.py com dados de teste realistas  
- Desenvolvimento de testes unitários (test_api.py, test_ml.py)  
- Validações de endpoints e regras de negócio  
- Implementação de testes de segurança e autenticação  
- Boas práticas de qualidade e confiabilidade de software  

### 🎯 Objetivo Geral
Implementar testes da API e sistema de dados iniciais para desenvolvimento, aplicando testes e validações como parte das boas práticas de segurança e qualidade em sistemas críticos de saúde.

### 💡 Habilidades e Competências
✅ Implementar testes automatizados para garantia de qualidade  
✅ Desenvolver dados de teste realistas para validação  
✅ Aplicar testes de segurança e validação de regras de negócio  
✅ Estruturar ambiente de desenvolvimento confiável e seguro  

### 📌 Materiais Necessários
📌 Sistema completo implementado (todas as funcionalidades)  
📌 Biblioteca pytest para testes automatizados  
📌 Conhecimento de testes unitários e de integração  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Análise de Qualidade:**  
Discussão sobre importância: "Por que testes são críticos em sistemas de saúde? Como garantir que o sistema funcione corretamente em todas as situações?"

---

### **Tópico 1: Sistema de Dados de Teste - Seed Data (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Criação de Cenários:**  
Desenvolvimento do seed_data.py com dados realistas: psicólogos, pacientes, consultas e solicitações que representem cenários reais de uso.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar base de dados de teste completa  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento de Dados Realistas:**  
Implementar seed_data.py com usuários de teste, pacientes com histórico variado, consultas em diferentes status e solicitações pendentes.

**Parte do Projeto Construída:** Sistema seed_data.py com dados de teste completos

---

### **Tópico 2: Testes de API - Endpoints e Autenticação (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Testes de Segurança:**  
Implementação do test_api.py com testes de todos os endpoints, validação de autenticação JWT e verificação de permissões de acesso.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar testes de API e segurança  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Orientado a Testes:**  
Criar test_api.py com testes para login, registro, CRUD de pacientes, agendamentos e validação de tokens JWT.

**Parte do Projeto Construída:** Suite de testes de API com validações de segurança

---

### **Tópico 3: Testes de Machine Learning - Validação de Algoritmos (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Validação de IA:**  
Desenvolvimento do test_ml.py com testes específicos para algoritmo de análise de risco, validação de scores e classificações.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Validar algoritmos de ML e análises  
📝 **Tarefa:**  
- **Metodologia Ativa - Testes de Algoritmos:**  
Implementar test_ml.py com testes para cálculo de risco, classificação de pacientes e validação de métricas estatísticas.

**Parte do Projeto Construída:** Testes específicos para validação de algoritmos ML

---

### **Tópico 4: Validações de Regras de Negócio e Integração (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Testes de Integração:**  
Implementação de testes de regras de negócio: validações de agendamento, conflitos de horário, permissões de acesso e integridade de dados.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Validar regras de negócio e integrações  
📝 **Tarefa:**  
- **Metodologia Ativa - Testes de Qualidade:**  
Expandir testes com validações de regras específicas do domínio médico, testes de integração entre módulos e cenários de erro.

**Parte do Projeto Construída:** Suite completa de testes com validações de negócio

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Cultura de Qualidade:**  
Reflexão sobre como testes automatizados garantem confiabilidade em sistemas críticos e a importância da cultura de qualidade no desenvolvimento.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio de Documentação:**  
Pensar em como documentar o sistema de forma clara e completa. Que informações são essenciais para outros desenvolvedores e usuários?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação pytest para testes Python  
- Boas práticas de testes em sistemas críticos  
- Guia de validação de algoritmos ML  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Criação adequada de dados de teste realistas  
✅ Implementação correta de testes de API e segurança  
✅ Desenvolvimento de testes específicos para ML  
✅ Validação apropriada de regras de negócio  

### **Avaliação Somativa (Entregáveis):**
✅ Arquivo seed_data.py completo e funcional  
✅ Suite test_api.py com cobertura de endpoints  
✅ Arquivo test_ml.py com validação de algoritmos  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Testes abrangentes, dados realistas, validações robustas de segurança e ML  
- **Bom (7-8):** Testes funcionais com boa cobertura e pequenos ajustes necessários  
- **Satisfatório (6-7):** Implementação básica mas com melhorias necessárias na cobertura  
- **Insatisfatório (<6):** Problemas nos testes ou validações inadequadas  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de testes automatizados com pytest  
- Compreensão de validação de algoritmos ML  
- Conhecimento de testes de segurança e autenticação  

🎯 **Aplicação Prática:**  
- Capacidade de desenvolver suites de teste completas  
- Habilidade para validar sistemas críticos de saúde  
- Competência em garantia de qualidade de software  

🎯 **Competências Profissionais:**  
- Cultura de qualidade e confiabilidade  
- Desenvolvimento orientado a testes (TDD)  
- Consciência sobre importância de validação em sistemas críticos  

### **Conexão com o Projeto:**  
Esta aula estabelece a camada de qualidade e confiabilidade do sistema Lunysse, garantindo que todas as funcionalidades funcionem corretamente e que o sistema seja seguro e confiável para uso em consultórios psicológicos.

### **Preparação para Próxima Aula:**  
Os testes implementados validarão o sistema durante a próxima aula de documentação, garantindo que todas as funcionalidades estejam funcionando corretamente antes da criação da documentação técnica completa.