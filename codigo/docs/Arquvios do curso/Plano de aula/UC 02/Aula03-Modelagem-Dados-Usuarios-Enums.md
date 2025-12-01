# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Modelagem de Dados - Usuários e Enums

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 03  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Modelagem orientada a objetos com SQLAlchemy  
- Implementação de Enums para tipagem forte  
- Criação do modelo User com diferentes tipos  
- Definição de constraints e validações  
- Relacionamentos entre entidades do sistema  

### 🎯 Objetivo Geral
Criar modelos SQLAlchemy para usuários, tipos e status do sistema, aplicando conceitos de POO na modelagem de dados e definindo classes com relacionamentos entre entidades.

### 💡 Habilidades e Competências
✅ Aplicar programação orientada a objetos na modelagem de dados  
✅ Implementar tipagem forte com Enums Python  
✅ Definir constraints e validações em modelos SQLAlchemy  
✅ Estruturar relacionamentos entre entidades do sistema  

### 📌 Materiais Necessários
📌 Configuração de banco da aula anterior  
📌 Conhecimento de POO e classes Python  
📌 Compreensão de relacionamentos de banco de dados  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Mapeamento Mental:**  
Análise do domínio: "Quais são as entidades principais de um sistema de agendamento psicológico e como elas se relacionam? Como garantir integridade e tipagem dos dados?"

---

### **Tópico 1: Fundamentos de Modelagem OO com SQLAlchemy (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração Conceitual:**  
Explicação de como classes Python se mapeiam para tabelas SQL, conceitos de herança, encapsulamento e polimorfismo aplicados à modelagem de dados.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Compreender mapeamento objeto-relacional  
📝 **Tarefa:**  
- **Metodologia Ativa - Brainstorming Estruturado:**  
Identificar entidades do sistema Lunysse, seus atributos e relacionamentos através de diagrama colaborativo.

**Parte do Projeto Construída:** Diagrama conceitual das entidades principais

---

### **Tópico 2: Implementação de Enums para Tipagem Forte (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding:**  
Criação dos Enums UserType, AppointmentStatus e RequestStatus, explicando vantagens da tipagem forte e controle de valores válidos.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar Enums do sistema  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação em Pares:**  
Criar arquivo models.py, implementar os três Enums principais com valores apropriados para o domínio médico.

**Parte do Projeto Construída:** Enums de tipagem (UserType, AppointmentStatus, RequestStatus)

---

### **Tópico 3: Modelo User - Psicólogos e Pacientes (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Desenvolvimento Incremental:**  
Implementação passo a passo do modelo User, definindo campos, tipos, constraints e diferenciação entre psicólogos e pacientes.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Criar modelo User completo  
📝 **Tarefa:**  
- **Metodologia Ativa - Aprendizagem Baseada em Problemas:**  
Implementar classe User com campos específicos (email, senha, tipo, especialidade, CRP), aplicando validações e constraints.

**Parte do Projeto Construída:** Modelo User funcional com diferenciação de tipos

---

### **Tópico 4: Relacionamentos e Constraints Avançadas (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Resolução de Casos:**  
Definição de relacionamentos futuros, foreign keys, índices e constraints para garantir integridade referencial.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar constraints e preparar relacionamentos  
📝 **Tarefa:**  
- **Metodologia Ativa - Prática Orientada:**  
Adicionar índices, unique constraints, validações de email e preparar estrutura para relacionamentos com outras entidades.

**Parte do Projeto Construída:** Modelo User com constraints e estrutura para relacionamentos

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Análise Crítica:**  
Reflexão sobre como a modelagem orientada a objetos facilita manutenção, extensibilidade e compreensão do sistema.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio de Modelagem:**  
Pensar na modelagem das entidades Patient, Appointment e Request. Como elas se relacionam com User?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação SQLAlchemy Models  
- Guia de boas práticas de modelagem  
- Exemplos de sistemas médicos  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Compreensão de conceitos de POO aplicados à modelagem  
✅ Implementação correta dos Enums com tipagem forte  
✅ Criação adequada do modelo User com validações  
✅ Aplicação de constraints e preparação para relacionamentos  

### **Avaliação Somativa (Entregáveis):**
✅ Arquivo models.py com Enums funcionais  
✅ Modelo User completo e validado  
✅ Constraints e índices implementados corretamente  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Modelagem completa, POO bem aplicada, código limpo e bem documentado  
- **Bom (7-8):** Modelos funcionais com pequenos ajustes na estrutura OO  
- **Satisfatório (6-7):** Implementação básica mas com melhorias necessárias na modelagem  
- **Insatisfatório (<6):** Problemas na modelagem ou conceitos POO mal aplicados  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de modelagem OO com SQLAlchemy  
- Compreensão de Enums e tipagem forte em Python  
- Conhecimento de constraints e validações de dados  

🎯 **Aplicação Prática:**  
- Capacidade de modelar entidades complexas de sistemas reais  
- Habilidade para aplicar POO na camada de persistência  
- Competência em definir relacionamentos e integridade de dados  

🎯 **Competências Profissionais:**  
- Pensamento orientado a objetos aplicado a dados  
- Análise de domínio e modelagem conceitual  
- Estruturação de código maintível e extensível  

### **Conexão com o Projeto:**  
Esta aula estabelece as entidades fundamentais do sistema Lunysse, criando a base orientada a objetos que suportará toda a lógica de negócio: diferenciação entre psicólogos e pacientes, controle de status e tipos.

### **Preparação para Próxima Aula:**  
Os modelos User e Enums criados serão utilizados na próxima aula para implementar as entidades Patient, Appointment e Request, estabelecendo relacionamentos complexos entre todas as entidades do sistema.