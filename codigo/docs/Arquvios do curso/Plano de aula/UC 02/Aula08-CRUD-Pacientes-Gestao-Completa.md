# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – CRUD de Pacientes - Gestão Completa

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 08  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Implementação do router patients.py com operações CRUD completas  
- Endpoints para listar, criar, atualizar e buscar pacientes  
- Sistema de anotações e histórico de sessões  
- Proteção de rotas com autenticação JWT  
- Funcionalidades orientadas a objetos para gestão de pacientes  

### 🎯 Objetivo Geral
Desenvolver operações CRUD completas para gestão de pacientes, implementando funcionalidades orientadas a objetos para gestão completa de pacientes e sessões em sistema psicológico.

### 💡 Habilidades e Competências
✅ Implementar operações CRUD completas e seguras  
✅ Desenvolver funcionalidades orientadas a objetos para gestão  
✅ Aplicar proteção de rotas com autenticação  
✅ Estruturar sistema de anotações e histórico médico  

### 📌 Materiais Necessários
📌 Sistema de autenticação da aula anterior  
📌 Modelos Patient e User implementados  
📌 Schemas Pydantic para validação  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Análise de Requisitos:**  
Discussão sobre gestão de pacientes: "Como um psicólogo precisa gerenciar seus pacientes? Quais informações são essenciais? Como garantir privacidade e acesso controlado?"

---

### **Tópico 1: Estrutura do Router e Proteção de Rotas (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Arquitetura Segura:**  
Estruturação do router patients.py com dependency injection, proteção JWT e organização orientada a objetos para operações de pacientes.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar estrutura base do CRUD protegido  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Orientado a Objetos:**  
Implementar router patients.py com importações, dependencies de autenticação e estrutura base para operações CRUD.

**Parte do Projeto Construída:** Router patients.py estruturado com proteção JWT

---

### **Tópico 2: Operações de Listagem e Busca (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding:**  
Implementação de endpoints GET para listar pacientes do psicólogo logado e buscar paciente específico com validações de propriedade.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar listagem e busca segura de pacientes  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação Orientada a Dados:**  
Criar endpoints GET /patients/ e GET /patients/{id} com filtros por psicólogo, paginação e validações de acesso.

**Parte do Projeto Construída:** Endpoints de listagem e busca funcionais

---

### **Tópico 3: Criação e Atualização de Pacientes (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Desenvolvimento Incremental:**  
Implementação de endpoints POST e PUT para criar e atualizar pacientes, com validações específicas e cálculo automático de idade.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar criação e atualização de pacientes  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação Orientada a Regras:**  
Criar endpoints POST /patients/ e PUT /patients/{id} com validações de dados, cálculo de idade e associação ao psicólogo.

**Parte do Projeto Construída:** CRUD completo de pacientes (Create, Read, Update)

---

### **Tópico 4: Sistema de Anotações e Histórico de Sessões (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Funcionalidades Avançadas:**  
Implementação de endpoints para histórico de sessões do paciente e sistema de anotações médicas com controle de acesso.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar sistema de anotações e histórico  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento de Funcionalidades Médicas:**  
Criar endpoints GET /patients/{id}/sessions e POST /patients/{id}/notes para gestão completa do histórico médico.

**Parte do Projeto Construída:** Sistema completo de gestão de pacientes com histórico

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Reflexão sobre Funcionalidades:**  
Análise de como as funcionalidades orientadas a objetos facilitam a gestão de pacientes e como isso se conecta com relatórios futuros.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio de Integração:**  
Pensar em como integrar o CRUD de pacientes com sistema de agendamentos. Como garantir que apenas pacientes cadastrados possam ter consultas?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação FastAPI CRUD  
- Padrões de desenvolvimento orientado a objetos  
- Boas práticas de sistemas médicos  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Implementação correta das operações CRUD  
✅ Aplicação adequada de proteção de rotas  
✅ Desenvolvimento de funcionalidades orientadas a objetos  
✅ Implementação do sistema de anotações e histórico  

### **Avaliação Somativa (Entregáveis):**
✅ Router patients.py completo e funcional  
✅ Todas as operações CRUD testadas e validadas  
✅ Sistema de anotações e histórico implementado  

### **Critérios de Qualidade:**
- **Excelente (9-10):** CRUD completo, seguro, bem estruturado com funcionalidades avançadas de histórico  
- **Bom (7-8):** Operações CRUD funcionais com pequenos ajustes na estrutura  
- **Satisfatório (6-7):** Implementação básica mas com melhorias necessárias nas funcionalidades  
- **Insatisfatório (<6):** Problemas nas operações CRUD ou falhas de segurança  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de implementação CRUD completa em FastAPI  
- Compreensão de proteção de rotas com JWT  
- Conhecimento de funcionalidades orientadas a objetos  

🎯 **Aplicação Prática:**  
- Capacidade de desenvolver sistemas de gestão completos  
- Habilidade para implementar funcionalidades médicas específicas  
- Competência em estruturação de dados para relatórios  

🎯 **Competências Profissionais:**  
- Desenvolvimento orientado ao domínio médico  
- Consciência sobre privacidade e acesso controlado  
- Estruturação de código para funcionalidades avançadas  

### **Conexão com o Projeto:**  
Esta aula implementa o núcleo de gestão de pacientes do sistema Lunysse, permitindo que psicólogos gerenciem completamente seus pacientes, mantenham histórico de sessões e preparem dados para relatórios e análises futuras.

### **Preparação para Próxima Aula:**  
O CRUD de pacientes será integrado na próxima aula com o sistema central de agendamentos, criando a funcionalidade principal do sistema: marcar, gerenciar e acompanhar consultas psicológicas.