# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Machine Learning - Análise de Risco de Pacientes

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 12  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Desenvolvimento do router ml_analysis.py para análises inteligentes  
- Implementação do ml_service.py com algoritmo de risco personalizado  
- Cálculo de scores e classificação de níveis de risco  
- Aplicação de conceitos de POO em algoritmos de ML  
- Sistema inteligente para suporte à decisão clínica  

### 🎯 Objetivo Geral
Implementar algoritmo de ML para análise de risco baseada em frequência e padrões, aplicando conceitos de POO e ML para desenvolver sistema inteligente de análise de risco em consultórios psicológicos.

### 💡 Habilidades e Competências
✅ Implementar algoritmos de Machine Learning personalizados  
✅ Aplicar conceitos de POO em sistemas inteligentes  
✅ Desenvolver análises preditivas para suporte clínico  
✅ Criar sistemas de classificação e scoring automatizado  

### 📌 Materiais Necessários
📌 Sistema de relatórios da aula anterior funcionando  
📌 Biblioteca NumPy instalada para cálculos  
📌 Conhecimento básico de algoritmos e estatística  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Problema Clínico:**  
Análise do desafio: "Como identificar pacientes em risco de abandono do tratamento? Quais padrões comportamentais podem indicar necessidade de intervenção preventiva?"

---

### **Tópico 1: Fundamentos de ML Aplicado à Saúde Mental (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Conceituação Aplicada:**  
Explicação de algoritmos de classificação, scoring e análise de padrões aplicados especificamente ao contexto de saúde mental e abandono de tratamento.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Compreender ML aplicado à psicologia  
📝 **Tarefa:**  
- **Metodologia Ativa - Análise de Casos:**  
Identificar variáveis relevantes para análise de risco: frequência de consultas, cancelamentos, ausências, padrões temporais.

**Parte do Projeto Construída:** Definição de variáveis e métricas para algoritmo ML

---

### **Tópico 2: Estrutura do Router ML e Arquitetura (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Arquitetura Inteligente:**  
Estruturação do router ml_analysis.py com endpoints para análise individual e coletiva de pacientes, aplicando padrões orientados a objetos.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Criar estrutura base para análises ML  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Orientado a IA:**  
Implementar router ml_analysis.py com endpoints GET /ml/risk-analysis e GET /ml/risk-analysis/{patient_id} usando POO.

**Parte do Projeto Construída:** Router ml_analysis.py estruturado com padrões OO

---

### **Tópico 3: Algoritmo de Análise de Risco Personalizado (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding ML:**  
Implementação do ml_service.py com algoritmo personalizado que analisa frequência, cancelamentos, ausências e calcula score de risco.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Desenvolver algoritmo de risco personalizado  
📝 **Tarefa:**  
- **Metodologia Ativa - Programação de Algoritmos:**  
Criar ml_service.py com funções para calcular score de risco baseado em múltiplas variáveis comportamentais e temporais.

**Parte do Projeto Construída:** Algoritmo ML personalizado para análise de risco

---

### **Tópico 4: Classificação e Sistema de Alertas (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Sistema de Decisão:**  
Implementação de sistema de classificação (baixo/moderado/alto risco) e geração de alertas automáticos para psicólogos.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Implementar classificação e alertas inteligentes  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento de IA Aplicada:**  
Expandir ml_service.py com classificação de níveis de risco, razões principais e sistema de alertas para intervenção preventiva.

**Parte do Projeto Construída:** Sistema completo de ML com classificação e alertas

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Ética em IA:**  
Reflexão sobre ética no uso de ML em saúde mental, limitações dos algoritmos e importância do julgamento clínico humano.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio de Validação:**  
Pensar em como testar e validar o algoritmo ML. Quais testes são necessários para garantir confiabilidade do sistema?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Fundamentos de Machine Learning aplicado à saúde  
- Documentação NumPy para cálculos científicos  
- Ética em IA e sistemas de suporte à decisão clínica  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Compreensão de conceitos ML aplicados à saúde mental  
✅ Implementação correta do algoritmo de risco personalizado  
✅ Aplicação adequada de POO em sistemas inteligentes  
✅ Desenvolvimento de sistema de classificação e alertas  

### **Avaliação Somativa (Entregáveis):**
✅ Router ml_analysis.py completo e funcional  
✅ Serviço ml_service.py com algoritmo ML implementado  
✅ Sistema de classificação de risco testado e validado  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Algoritmo ML robusto, classificação precisa, sistema de alertas eficiente, código orientado a objetos  
- **Bom (7-8):** Algoritmo funcional com classificação adequada e pequenos ajustes necessários  
- **Satisfatório (6-7):** Implementação básica mas com melhorias necessárias no algoritmo  
- **Insatisfatório (<6):** Problemas no algoritmo ML ou classificação incorreta  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de implementação de algoritmos ML personalizados  
- Compreensão de análise preditiva em saúde mental  
- Conhecimento de sistemas de classificação e scoring  

🎯 **Aplicação Prática:**  
- Capacidade de desenvolver IA aplicada à saúde  
- Habilidade para criar sistemas de suporte à decisão clínica  
- Competência em análise de padrões comportamentais  

🎯 **Competências Profissionais:**  
- Desenvolvimento de soluções inteligentes para saúde  
- Consciência ética sobre uso de IA em contextos sensíveis  
- Integração de tecnologia com prática clínica responsável  

### **Conexão com o Projeto:**  
Esta aula implementa a camada de inteligência artificial do sistema Lunysse, criando ferramenta de suporte à decisão que ajuda psicólogos a identificar pacientes em risco e tomar ações preventivas baseadas em dados.

### **Preparação para Próxima Aula:**  
O sistema ML será validado na próxima aula através de testes automatizados, criação de dados de teste específicos e implementação de validações que garantam confiabilidade do algoritmo de análise de risco.