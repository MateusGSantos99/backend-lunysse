# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Testes de Integração e End-to-End

📌 **Disciplina:** Desenvolver Serviços Web  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 7  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Testes de integração com APIs externas  
- Testes end-to-end do fluxo completo  
- Mocks e stubs para serviços externos  
- Automação de testes com pytest e coverage  
- Validação de estruturas de dados e relatórios  

### 🎯 Objetivo Geral
Implementar suite completa de testes para validação do sistema integrado, garantindo qualidade na manipulação de dados e geração de relatórios complexos

### 💡 Habilidades e Competências
✅ Desenvolver testes de integração robustos  
✅ Implementar testes end-to-end automatizados  
✅ Criar mocks eficientes para serviços externos  
✅ Validar estruturas de dados e relatórios gerados  

### 📌 Materiais Necessários
📌 Sistema Lunysse com microserviços da aula anterior  
📌 Pytest e bibliotecas de teste  
📌 Ferramentas de mock (responses, httpx-mock)  
📌 Coverage para análise de cobertura  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (20min)
**Metodologia Ativa - Análise de Qualidade:**  
"Como garantir que um sistema distribuído funcione corretamente em produção? Como validar que relatórios complexos são gerados com dados precisos?" Discussão sobre importância de testes em sistemas críticos de saúde.

---

### **Tópico 1: Estruturação de Testes e Validação de Dados (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Design de Testes:**  
Estruturação de testes para validação de banco de dados, criação de fixtures para dados de teste, validação de integridade referencial e relatórios.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Criar base sólida de testes para estruturas de dados  
📝 **Tarefa:**  
- **Metodologia Ativa - Validação Sistemática:**  
Implementar fixtures de dados médicos, criar testes para validação de modelos SQLAlchemy, testar geração de relatórios com dados consistentes.

**Parte do Projeto Construída:** Base de testes para validação de estruturas de dados

---

### **Tópico 2: Testes de Integração com APIs Externas (70min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Teste de Integração:**  
Criação de mocks para ViaCEP e SendGrid, testes de timeout e falhas de rede, validação de cache e fallbacks.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Implementar testes robustos de integração externa  
📝 **Tarefa:**  
- **Metodologia Ativa - Simulação de Cenários:**  
Criar mocks para APIs externas, testar cenários de falha e recuperação, validar comportamento do cache em diferentes situações.

**Parte do Projeto Construída:** Suite de testes de integração com APIs externas

---

### **Tópico 3: Testes End-to-End do Sistema Distribuído (70min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Teste de Fluxo Completo:**  
Testes de fluxo completo desde autenticação até geração de relatórios, validação de comunicação entre microserviços, testes de performance.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Implementar testes end-to-end completos  
📝 **Tarefa:**  
- **Metodologia Ativa - Validação de Fluxos:**  
Criar testes que simulem jornada completa do usuário, validar geração de relatórios PDF/Excel, testar comunicação entre serviços.

**Parte do Projeto Construída:** Testes end-to-end do sistema completo

---

### **Tópico 4: Automação e Coverage (20min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Automação de Qualidade:**  
Configuração de pytest com coverage, relatórios de cobertura, integração com CI/CD, métricas de qualidade.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Automatizar execução e análise de testes  
📝 **Tarefa:**  
- **Metodologia Ativa - Garantia de Qualidade:**  
Configurar pytest.ini, implementar relatórios de coverage, criar scripts de automação para execução completa dos testes.

**Parte do Projeto Construída:** Sistema automatizado de testes com métricas

---

### Encerramento e Reflexão (20min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Análise de Cobertura:**  
Análise dos resultados de coverage, discussão sobre gaps de teste identificados, estratégias para manutenção de qualidade contínua.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Preparação para Produção:**  
Pesquisar ferramentas de monitoramento (Prometheus, Grafana) e estratégias de observabilidade para sistemas distribuídos.

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação pytest e coverage  
- Exemplos de testes de sistemas distribuídos  
- Boas práticas de teste em APIs  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Qualidade da estruturação dos testes  
✅ Eficiência dos mocks e stubs criados  
✅ Cobertura adequada dos cenários de teste  
✅ Validação correta de estruturas de dados  

### **Avaliação Somativa (Entregáveis):**
✅ Suite completa de testes implementada  
✅ Testes de integração com APIs externas funcionando  
✅ Testes end-to-end validando fluxos completos  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Cobertura >90%, testes robustos, cenários de falha cobertos, relatórios validados  
- **Bom (7-8):** Cobertura >80%, testes funcionais, integração testada  
- **Satisfatório (6-7):** Testes básicos implementados, cobertura >70%  
- **Insatisfatório (<6):** Dificuldades na implementação ou cobertura insuficiente  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Testes de integração e end-to-end  
- Mocking de serviços externos  
- Análise de cobertura de código  

🎯 **Aplicação Prática:**  
- Sistema Lunysse com qualidade garantida  
- Validação automática de relatórios  
- Confiabilidade em ambiente distribuído  

🎯 **Competências Profissionais:**  
- Garantia de qualidade em sistemas críticos  
- Automação de processos de validação  
- Manutenção de código confiável  

### **Conexão com o Projeto:**  
Esta aula garante a qualidade e confiabilidade do sistema Lunysse distribuído, validando especialmente a geração correta de relatórios e análises estatísticas.

### **Preparação para Próxima Aula:**  
O sistema testado e validado será instrumentado com monitoramento e observabilidade para acompanhamento em tempo real da saúde dos serviços.