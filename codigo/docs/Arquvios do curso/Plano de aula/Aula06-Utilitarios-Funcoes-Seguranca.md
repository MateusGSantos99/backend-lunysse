# PLANO DE TRABALHO DOCENTE 

## MODELO PEDAGÓGICO SENAC 

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga Horária Total:** 60 horas  
**Carga Horária da UC:** 96 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## PLANO DE AULA – Utilitários e Funções de Segurança

📌 **Disciplina:** Desenvolvimento de Sistemas com Machine Learning  
👨🏫 **Mentor(a):** Jeremias de Oliveira Nunes  
📆 **Data:** Aula nº 06  
⏰ **Duração:** 4 horas  

---

## 📖 Planejamento

### 📌 Conteúdo Formativo
- Implementação de hash e verificação de senhas com bcrypt  
- Criação e verificação de tokens JWT para autenticação  
- Função para cálculo de idade e utilidades auxiliares  
- Configuração segura de variáveis de ambiente  
- Boas práticas de segurança em sistemas de saúde  

### 🎯 Objetivo Geral
Desenvolver funções auxiliares para JWT, hash de senhas e cálculos, implementando mecanismos de segurança essenciais para proteção de dados e autenticação em sistemas de saúde.

### 💡 Habilidades e Competências
✅ Implementar sistemas de autenticação seguros com JWT  
✅ Aplicar criptografia de senhas com algoritmos robustos  
✅ Desenvolver funções auxiliares para validação e cálculos  
✅ Configurar segurança de dados sensíveis em sistemas médicos  

### 📌 Materiais Necessários
📌 Bibliotecas bcrypt e python-jose instaladas  
📌 Conhecimento de criptografia básica  
📌 Compreensão de tokens de autenticação  

---

## 🎓 Estratégias de Ensino e Aprendizagem

### Introdução e Contextualização (30min)
**Metodologia Ativa - Análise de Vulnerabilidades:**  
Discussão sobre segurança em sistemas de saúde: "Por que a proteção de dados médicos é crítica? Quais são as principais vulnerabilidades e como preveni-las?"

---

### **Tópico 1: Criptografia de Senhas com Bcrypt (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Demonstração de Segurança:**  
Explicação de algoritmos de hash, salt, e por que bcrypt é superior a MD5/SHA para senhas. Demonstração de ataques de força bruta.

#### 📌 Atividade Prática 1:
🎯 **Objetivo:** Implementar sistema seguro de senhas  
📝 **Tarefa:**  
- **Metodologia Ativa - Segurança Hands-on:**  
Criar funções `get_password_hash()` e `verify_password()` usando bcrypt, testando diferentes níveis de complexidade.

**Parte do Projeto Construída:** Sistema de hash de senhas seguro (utils.py)

---

### **Tópico 2: Autenticação JWT - Tokens Seguros (75min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Live Coding Seguro:**  
Implementação de criação e verificação de tokens JWT, configuração de chaves secretas e tempo de expiração para sistemas médicos.

#### 📌 Atividade Prática 2:
🎯 **Objetivo:** Criar sistema de autenticação JWT  
📝 **Tarefa:**  
- **Metodologia Ativa - Desenvolvimento Seguro:**  
Implementar `create_access_token()` e funções de verificação JWT, configurando SECRET_KEY e algoritmos seguros.

**Parte do Projeto Construída:** Sistema JWT completo para autenticação

---

### **Tópico 3: Funções Auxiliares e Validações (45min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Programação Utilitária:**  
Criação de funções auxiliares: cálculo de idade, validações de dados médicos e outras utilidades específicas do domínio.

#### 📌 Atividade Prática 3:
🎯 **Objetivo:** Desenvolver funções auxiliares do sistema  
📝 **Tarefa:**  
- **Metodologia Ativa - Resolução de Problemas:**  
Implementar `calculate_age()`, validações de email, telefone e outras funções específicas para o sistema de agendamento.

**Parte do Projeto Construída:** Conjunto de funções auxiliares (utils.py completo)

---

### **Tópico 4: Configuração Segura e Variáveis de Ambiente (60min)**
#### 📌 Demonstração Prática:
**Metodologia Ativa - Configuração de Produção:**  
Configuração segura de variáveis sensíveis, uso do .env, e boas práticas para deploy de sistemas médicos.

#### 📌 Atividade Prática 4:
🎯 **Objetivo:** Configurar segurança de ambiente  
📝 **Tarefa:**  
- **Metodologia Ativa - Segurança Operacional:**  
Criar arquivo .env, configurar SECRET_KEY forte, definir tempos de expiração e validar configurações de segurança.

**Parte do Projeto Construída:** Configuração segura de ambiente (.env e validações)

---

### Encerramento e Reflexão (30min)
#### 📌 Discussão em grupo:
**Metodologia Ativa - Análise de Segurança:**  
Reflexão sobre LGPD, proteção de dados médicos e responsabilidades éticas no desenvolvimento de sistemas de saúde.

#### 📌 Desafio para a próxima aula:
**Metodologia Ativa - Desafio de Autenticação:**  
Pensar em como integrar essas funções de segurança em endpoints de login e registro. Como validar credenciais de forma segura?

---

### 📌 Objetos de Aprendizagem
📝 **Materiais Didáticos Utilizados:**  
- Documentação bcrypt e python-jose  
- Guia OWASP de segurança em aplicações  
- Boas práticas LGPD para sistemas médicos  

---

## 🎯 Avaliação

### **Avaliação Formativa (Durante a aula):**
✅ Implementação correta de hash de senhas com bcrypt  
✅ Criação e verificação de tokens JWT funcionais  
✅ Desenvolvimento de funções auxiliares adequadas  
✅ Configuração segura de variáveis de ambiente  

### **Avaliação Somativa (Entregáveis):**
✅ Arquivo utils.py completo e funcional  
✅ Sistema de autenticação JWT implementado  
✅ Configuração .env segura e validada  

### **Critérios de Qualidade:**
- **Excelente (9-10):** Implementação segura completa, boas práticas aplicadas, código robusto contra vulnerabilidades  
- **Bom (7-8):** Funcionalidades implementadas corretamente com pequenos ajustes de segurança  
- **Satisfatório (6-7):** Implementação básica mas com melhorias necessárias na segurança  
- **Insatisfatório (<6):** Vulnerabilidades de segurança ou implementação inadequada  

---

## 🎓 Conclusão

### **Aprendizado Esperado:**
🎯 **Conhecimento Técnico:**  
- Domínio de criptografia de senhas com bcrypt  
- Compreensão de autenticação JWT e tokens seguros  
- Conhecimento de configuração segura de ambientes  

🎯 **Aplicação Prática:**  
- Capacidade de implementar autenticação segura em sistemas reais  
- Habilidade para proteger dados sensíveis adequadamente  
- Competência em desenvolver funções auxiliares robustas  

🎯 **Competências Profissionais:**  
- Consciência sobre segurança em sistemas de saúde  
- Aplicação de boas práticas de desenvolvimento seguro  
- Responsabilidade ética com dados médicos sensíveis  

### **Conexão com o Projeto:**  
Esta aula estabelece a camada de segurança fundamental do sistema Lunysse, criando as bases para autenticação segura de psicólogos e pacientes, proteção de dados sensíveis e conformidade com regulamentações de saúde.

### **Preparação para Próxima Aula:**  
As funções de segurança implementadas serão utilizadas na próxima aula para criar o sistema completo de autenticação com endpoints de login e registro, integrando JWT, validação de credenciais e proteção de rotas.