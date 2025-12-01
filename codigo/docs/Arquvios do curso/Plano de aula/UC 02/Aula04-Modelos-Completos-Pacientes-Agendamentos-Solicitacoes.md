# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Modelos Completos - Pacientes, Agendamentos e Solicitações

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 04  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Implementação de modelos Patient, Appointment e Request  
- Configuração de ForeignKeys e relacionamentos complexos  
- Definição de campos obrigatórios e opcionais  
- Estruturas de dados SQL para relatórios e consultas  
- Integridade referencial e constraints avançadas  

### 🎯 Objetivo Geral
Completar a modelagem com todas as entidades do sistema de agendamento, definindo estruturas de dados SQL complexas com relacionamentos para suporte a relatórios e consultas.

### 💡 Habilidades e Competências
✅ Implementar relacionamentos complexos entre entidades SQL  
✅ Configurar ForeignKeys e integridade referencial  
✅ Estruturar dados para suporte a relatórios e análises  
✅ Definir campos obrigatórios e opcionais estrategicamente  

### 📌 Materiais Necessários
📌 Modelos User e Enums da aula anterior  
📌 Conhecimento de relacionamentos de banco de dados  
📌 Compreensão do domínio de agendamento médico  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Análise de Requisitos:**  
Revisão do sistema: "Como estruturar dados de pacientes, agendamentos e solicitações para permitir consultas eficientes, relatórios detalhados e análises de machine learning?"

---

### **Tópico 1: Modelo Patient - Gestão de Pacientes (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Modelagem Colaborativa:**  
Análise dos requisitos do modelo Patient: dados pessoais, relacionamento com psicólogos, histórico e campos para relatórios.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Implementar modelo Patient completo  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Incremental:**  
Criar classe Patient com campos (nome, email, telefone, data_nascimento, idade, status), ForeignKey para psicólogo e relacionamentos.

**Parte do Projeto Construída:** Modelo Patient com relacionamento User (psicólogo)

---

### **Tópico 2: Modelo Appointment - Core do Sistema (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding:**  
Implementação do modelo Appointment com relacionamentos múltiplos (paciente + psicólogo), campos de controle e estrutura para relatórios.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Criar modelo central de agendamentos  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação Orientada a Problemas:**  
Implementar classe Appointment com ForeignKeys duplas, campos de data/hora, status, descrição, duração, notas e relatório completo.

**Parte do Projeto Construída:** Modelo Appointment com relacionamentos Patient e User

---

### **Tópico 3: Modelo Request - Sistema de Solicitações (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Estudo de Caso:**  
Análise do workflow de solicitações: dados do solicitante, preferências, status de aprovação e campos para controle.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar sistema de solicitações  
📝 **Tarefa:**  
- **Metodologia Ativa - Aprendizagem Baseada em Projetos:**  
Criar classe Request com dados do paciente, preferências (psicólogo, datas, horários), status e controle de workflow.

**Parte do Projeto Construída:** Modelo Request com relacionamento User (psicólogo preferido)

---

### **Tópico 4: Relacionamentos e Otimização para Relatórios (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Otimização Colaborativa:**  
Configuração de relacionamentos bidirecionais, índices para consultas e estrutura otimizada para geração de relatórios e análises.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Otimizar estrutura para consultas e relatórios  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Performance:**  
Configurar relacionamentos bidirecionais, adicionar índices estratégicos e testar consultas para relatórios.

**Parte do Projeto Construída:** Estrutura completa otimizada para relatórios e consultas

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Análise de Arquitetura:**  
Reflexão sobre como a estrutura de dados impacta performance de consultas, geração de relatórios e análises de machine learning.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio de Validação:**  
Pensar em como validar e serializar esses dados complexos. Quais validações são necessárias para cada campo?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação SQLAlchemy Relationships  
- Guia de otimização de consultas SQL  
- Casos de uso de sistemas médicos  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Implementação correta dos três modelos principais  
✅ Configuração adequada de ForeignKeys e relacionamentos  
✅ Definição estratégica de campos obrigatórios e opcionais  
✅ Estruturação otimizada para consultas e relatórios  

### **Avaliação Somativa (Entregáveis):**
✅ Modelos Patient, Appointment e Request funcionais  
✅ Relacionamentos configurados corretamente  
✅ Estrutura otimizada para geração de relatórios  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Modelos completos, relacionamentos corretos, estrutura otimizada para consultas complexas  
- **Bom (7-8):** Modelos funcionais com relacionamentos adequados e pequenos ajustes necessários  
- **Satisfatório (6-7):** Implementação básica mas com melhorias necessárias na estrutura SQL  
- **Insatisfatório (<6):** Problemas nos relacionamentos ou estrutura inadequada para relatórios  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de relacionamentos complexos em SQLAlchemy  
- Compreensão de otimização para consultas e relatórios  
- Conhecimento de integridade referencial avançada  

🎯 **Aplicação Prática:**  
- Capacidade de modelar sistemas complexos com múltiplos relacionamentos  
- Habilidade para estruturar dados visando performance de consultas  
- Competência em definir campos estratégicos para análises  

🎯 **Competências Profissionais:**  
- Pensamento em arquitetura de dados para relatórios  
- Análise de performance e otimização de consultas SQL  
- Estruturação de dados para machine learning e análises  

### **Conexão com o Projeto:**  
Esta aula completa a camada de dados do sistema Lunysse, estabelecendo todas as entidades e relacionamentos necessários para suportar agendamentos, gestão de pacientes, solicitações e futura geração de relatórios e análises de ML.

### **Preparação para Próxima Aula:**  
Os modelos completos serão utilizados na próxima aula para criar schemas Pydantic de validação e serialização, estabelecendo a camada de validação de dados que protegerá a integridade das informações do sistema.