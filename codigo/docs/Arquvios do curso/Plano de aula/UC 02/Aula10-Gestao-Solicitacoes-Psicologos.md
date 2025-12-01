# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Gestão de Solicitações e Psicólogos

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 10  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Implementação do router requests.py para solicitações  
- Router psychologists.py para listagem de profissionais  
- Workflow de aprovação e rejeição de solicitações  
- Sistema de notificações e controle de status  
- Funcionalidades orientadas a objetos para gestão administrativa  

### 🎯 Objetivo Geral
Desenvolver sistema de solicitações de novos pacientes e listagem de psicólogos, implementando funcionalidades orientadas a objetos para gestão de solicitações e profissionais do sistema psicológico.

### 💡 Habilidades e Competências
✅ Implementar workflows de aprovação e controle de status  
✅ Desenvolver funcionalidades administrativas orientadas a objetos  
✅ Criar sistema de listagem e busca de profissionais  
✅ Estruturar processos de negócio para gestão de solicitações  

### 📌 Materiais Necessários
📌 Modelos Request, User e Patient implementados  
📌 Sistema de autenticação funcionando  
📌 Conhecimento de workflows e estados de processo  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Análise de Processo:**  
Mapeamento do fluxo: "Como novos pacientes solicitam atendimento? Como psicólogos gerenciam essas solicitações? Qual o workflow ideal para aprovação e controle?"

---

### **Tópico 1: Router de Psicólogos - Listagem de Profissionais (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Desenvolvimento de Catálogo:**  
Implementação do router psychologists.py para listagem pública de psicólogos disponíveis, com informações profissionais e especialidades.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar sistema de listagem de profissionais  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação Orientada a Serviços:**  
Implementar router psychologists.py com endpoint GET /psychologists/ para listar profissionais ativos com especialidades e informações públicas.

**Parte do Projeto Construída:** Router psychologists.py com listagem de profissionais

---

### **Tópico 2: Estrutura de Solicitações - Router e Modelos (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Modelagem de Workflow:**  
Estruturação do router requests.py com operações para criar, listar e gerenciar solicitações de novos pacientes.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar estrutura base de solicitações  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Orientado a Estados:**  
Criar router requests.py com endpoints base e estrutura para gerenciamento de solicitações com diferentes status.

**Parte do Projeto Construída:** Router requests.py estruturado com operações base

---

### **Tópico 3: Criação e Listagem de Solicitações (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding de Processo:**  
Implementação de endpoints para criar novas solicitações (público) e listar solicitações (psicólogos), com validações e filtros.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar criação e listagem de solicitações  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação de Processos:**  
Criar endpoints POST /requests/ (público) e GET /requests/ (psicólogos) com validações de dados e filtros por status.

**Parte do Projeto Construída:** Sistema de criação e listagem de solicitações

---

### **Tópico 4: Workflow de Aprovação e Rejeição (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Implementação de Estados:**  
Desenvolvimento do workflow completo: aprovar solicitações (criando paciente), rejeitar com motivo e atualizar status com controle de permissões.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar workflow completo de aprovação  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento de Workflow:**  
Criar endpoints PUT /requests/{id} para aprovar/rejeitar, com lógica de criação automática de paciente e controle de estados.

**Parte do Projeto Construída:** Workflow completo de gestão de solicitações

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Análise de Processos:**  
Reflexão sobre como workflows bem estruturados facilitam gestão administrativa e como isso se conecta com relatórios de produtividade.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio de Análise:**  
Pensar em quais dados são importantes para relatórios gerenciais. Como medir produtividade de psicólogos e satisfação de pacientes?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Padrões de workflow e estados de processo  
- Documentação FastAPI para operações complexas  
- Boas práticas de sistemas administrativos  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Implementação correta da listagem de psicólogos  
✅ Estruturação adequada do sistema de solicitações  
✅ Desenvolvimento do workflow de aprovação/rejeição  
✅ Aplicação de controle de estados e permissões  

### **Avaliação Somativa (Entregáveis):**
✅ Router psychologists.py funcional  
✅ Router requests.py completo com workflow  
✅ Sistema de aprovação/rejeição testado  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Workflows completos, controle de estados robusto, funcionalidades administrativas bem estruturadas  
- **Bom (7-8):** Funcionalidades implementadas corretamente com pequenos ajustes no workflow  
- **Satisfatório (6-7):** Implementação básica mas com melhorias necessárias no controle de estados  
- **Insatisfatório (<6):** Problemas no workflow ou falhas no controle de permissões  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de implementação de workflows e controle de estados  
- Compreensão de sistemas administrativos orientados a objetos  
- Conhecimento de processos de aprovação e gestão  

🎯 **Aplicação Prática:**  
- Capacidade de desenvolver sistemas de gestão administrativa  
- Habilidade para implementar workflows complexos  
- Competência em controle de estados e permissões  

🎯 **Competências Profissionais:**  
- Pensamento em processos de negócio  
- Desenvolvimento orientado a workflows  
- Estruturação de sistemas administrativos eficientes  

### **Conexão com o Projeto:**  
Esta aula implementa a camada administrativa do sistema Lunysse, permitindo gestão eficiente de solicitações de novos pacientes, controle de workflow de aprovação e listagem organizada de profissionais disponíveis.

### **Preparação para Próxima Aula:**  
Os dados de solicitações, psicólogos e pacientes serão utilizados na próxima aula para implementar sistema completo de relatórios e estatísticas, gerando insights valiosos para gestão do consultório psicológico.