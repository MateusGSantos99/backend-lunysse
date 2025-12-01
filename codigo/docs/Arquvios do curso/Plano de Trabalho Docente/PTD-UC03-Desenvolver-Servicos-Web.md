# 📘 PLANO DE TRABALHO DOCENTE  

## MODELO PEDAGÓGICO SENAC  

**Curso:** Desenvolvimento de Sistemas com Machine Learning  
**Carga horária:** 96 horas  
**Carga Horária da UC:** 36 horas  

**Docente:** Jeremias de Oliveira Nunes  

---

## SITUAÇÃO DE APRENDIZAGEM: Desenvolver Serviços Web com FastAPI  

**Número de aulas:** 9 aulas  
**Carga horária prevista:** 36 horas (4h por aula)  

### Contexto + Cenário  
Com o sistema Lunysse já desenvolvido na UC anterior, surge a necessidade de integrá-lo com serviços externos, criar interfaces de consumo, implementar versionamento de APIs e expandir funcionalidades através de microserviços. Esta UC prepara o aluno para evoluir o sistema existente com integração de serviços web externos, APIs de terceiros, frontend consumidor e arquitetura distribuída.

### Problema  
Como evoluir o sistema Lunysse existente integrando serviços web externos (CEP, SMS, email), criando interfaces de consumo (frontend web/mobile), implementando versionamento de API, cache distribuído e arquitetura de microserviços para escalabilidade e manutenibilidade?

### Desafios  
- Integrar APIs externas (ViaCEP, WhatsApp Business, SendGrid) no sistema existente  
- Desenvolver frontend web responsivo que consome a API Lunysse  
- Implementar versionamento de API (v1, v2) com backward compatibility  
- Criar sistema de cache distribuído com Redis  
- Desenvolver microserviços complementares (notificações, relatórios)  
- Implementar monitoramento e observabilidade da API  
- Criar testes de integração e end-to-end  
- Deploy em ambiente de produção com CI/CD  

### Indicadores  
**Indicador 1:** Cria estruturas de código de serviço web utilizando linguagem de back-end de acordo com os requisitos do projeto  
**Indicador 2:** Realiza integração do código back-end com serviços de terceiros conforme os requisitos do projeto e as regras de consumo de dados via web  
**Indicador 3:** Consome serviços web e manipula registros utilizando linguagem de back-end e front-end de acordo com os requisitos do projeto e as funcionalidades das linguagens  
**Indicador 4:** Projeta e estrutura banco de dados para manipulação das informações e produção de relatórios  

---

## Elementos de Competência  

| Conhecimentos | Habilidades | Atitudes/Valores |
|---------------|-------------|------------------|
| • Web services: histórico e conceito<br>• Programação orientada a serviços<br>• Protocolo HTTP: requisições, respostas, códigos de status<br>• Padrão REST: conceitos, operações CRUD<br>• Representações JSON e XML<br>• FastAPI: roteamento, validação, documentação<br>• SQLAlchemy ORM e modelagem de dados<br>• Autenticação JWT e segurança<br>• Versionamento com Git<br>• Integração com serviços externos | • Interpretar requisitos de projetos<br>• Estruturar APIs REST profissionais<br>• Implementar autenticação segura<br>• Modelar e manipular banco de dados<br>• Integrar Machine Learning em APIs<br>• Consumir serviços web externos<br>• Aplicar versionamento ao código<br>• Documentar APIs automaticamente<br>• Testar e validar serviços web | • Colaboração no desenvolvimento em equipe<br>• Responsabilidade com dados sensíveis<br>• Comprometimento com qualidade<br>• Iniciativa na proposição de soluções<br>• Respeito aos direitos de propriedade intelectual<br>• Ética no tratamento de dados médicos<br>• Busca por excelência técnica<br>• Pensamento sistêmico |

---

## Sugestões de Atividades de Aprendizagem  

### 🎓 Aula 1 – Revisão e Versionamento da API Existente  
**Objetivo**  
Revisar sistema Lunysse desenvolvido e implementar versionamento de API profissional

**Atividades**  
- Revisão completa do sistema Lunysse da UC anterior  
- Implementação de versionamento de API (v1, v2)  
- Configuração de CORS para integração frontend  
- Otimização de performance e refatoração  

**Indicador trabalhado**  
✔️ Cria estruturas de código de serviço web utilizando linguagem de back-end de acordo com os requisitos do projeto  

**Descrição alinhada ao indicador**  
O aluno estrutura o projeto FastAPI seguindo padrões profissionais, implementa endpoints básicos e compreende os fundamentos de serviços web REST  

---

### 🎓 Aula 2 – Integração com APIs Externas  
**Objetivo**  
Integrar serviços web externos para enriquecer funcionalidades do sistema

**Atividades**  
- Integração com API ViaCEP para endereços  
- Configuração de cliente HTTP com httpx/requests  
- Implementação de tratamento de erros e timeout  
- Cache de respostas externas para otimização  

**Indicador trabalhado**  
✔️ Projeta e estrutura banco de dados para manipulação das informações e produção de relatórios  

**Descrição alinhada ao indicador**  
O aluno projeta estrutura de banco adequada ao domínio médico, implementa relacionamentos complexos e prepara base para relatórios  

---

### 🎓 Aula 3 – Sistema de Notificações Externas  
**Objetivo**  
Implementar sistema de notificações via email e SMS usando serviços externos

**Atividades**  
- Integração com SendGrid para emails  
- Configuração de templates de email responsivos  
- Implementação de fila de notificações assíncronas  
- Sistema de logs e monitoramento de entregas  

**Indicador trabalhado**  
✔️ Cria estruturas de código de serviço web utilizando linguagem de back-end de acordo com os requisitos do projeto  

**Descrição alinhada ao indicador**  
O aluno implementa validação profissional de dados, cria schemas robustos e estabelece contratos claros da API  

---

### 🎓 Aula 4 – Frontend Web Consumidor da API  
**Objetivo**  
Desenvolver interface web que consome a API Lunysse usando HTML, CSS e JavaScript

**Atividades**  
- Desenvolvimento de SPA (Single Page Application)  
- Implementação de autenticação JWT no frontend  
- Consumo de endpoints da API com fetch/axios  
- Interface responsiva para agendamentos e relatórios  

**Indicador trabalhado**  
✔️ Cria estruturas de código de serviço web utilizando linguagem de back-end de acordo com os requisitos do projeto  

**Descrição alinhada ao indicador**  
O aluno implementa segurança robusta na API, controla acesso por perfis de usuário e protege dados sensíveis adequadamente  

---

### 🎓 Aula 5 – Cache Distribuído e Performance  
**Objetivo**  
Implementar sistema de cache com Redis para otimizar performance da API

**Atividades**  
- Configuração e integração do Redis  
- Implementação de cache para consultas frequentes  
- Estratégias de invalidação de cache  
- Monitoramento de performance e métricas  

**Indicador trabalhado**  
✔️ Consome serviços web e manipula registros utilizando linguagem de back-end de acordo com os requisitos do projeto  

**Descrição alinhada ao indicador**  
O aluno desenvolve funcionalidades core do sistema, implementa manipulação completa de registros e valida regras de negócio  

---

### 🎓 Aula 6 – Microserviço de Relatórios  
**Objetivo**  
Desenvolver microserviço independente para geração de relatórios complexos

**Atividades**  
- Criação de microserviço separado para relatórios  
- Comunicação entre serviços via HTTP/gRPC  
- Geração de PDFs e planilhas Excel  
- Processamento assíncrono de relatórios pesados  

**Indicador trabalhado**  
✔️ Consome serviços web e manipula registros utilizando linguagem de back-end de acordo com os requisitos do projeto  

**Descrição alinhada ao indicador**  
O aluno implementa workflows complexos, gerencia estados de solicitações e integra diferentes entidades do sistema  

---

### 🎓 Aula 7 – Testes de Integração e End-to-End  
**Objetivo**  
Implementar suite completa de testes para validação do sistema integrado

**Atividades**  
- Testes de integração com APIs externas  
- Testes end-to-end do fluxo completo  
- Mocks e stubs para serviços externos  
- Automação de testes com pytest e coverage  

**Indicador trabalhado**  
✔️ Projeta e estrutura banco de dados para manipulação das informações e produção de relatórios  

**Descrição alinhada ao indicador**  
O aluno utiliza estrutura de dados para gerar relatórios complexos, implementa análises estatísticas e produz informações gerenciais  

---

### 🎓 Aula 8 – Monitoramento e Observabilidade  
**Objetivo**  
Implementar sistema completo de monitoramento e observabilidade da API

**Atividades**  
- Configuração de logs estruturados com Loguru  
- Implementação de métricas com Prometheus  
- Sistema de alertas e notificações  
- Dashboard de monitoramento em tempo real  

**Indicador trabalhado**  
✔️ Realiza integração do código back-end com serviços de terceiros conforme os requisitos do projeto  

**Descrição alinhada ao indicador**  
O aluno integra serviços de ML na API, implementa análises preditivas e combina diferentes tecnologias em solução única  

---

### 🎓 Aula 9 – Deploy e CI/CD Pipeline  
**Objetivo**  
Implementar pipeline de deploy automatizado e colocar sistema em produção

**Atividades**  
- Configuração de CI/CD com GitHub Actions  
- Deploy automatizado em cloud (Railway, Heroku)  
- Configuração de ambiente de produção  
- Monitoramento pós-deploy e rollback com Git  
- Preparação para deploy e produção  

**Indicador trabalhado**  
✔️ Cria estruturas de código de serviço web utilizando linguagem de back-end de acordo com os requisitos do projeto  

**Descrição alinhada ao indicador**  
O aluno finaliza projeto com qualidade profissional, implementa testes robustos e prepara sistema para ambiente de produção  

---

## Estratégias de Avaliação para esta Situação de Aprendizagem  

### Procedimentos de Avaliação  
- **Avaliação diagnóstica:** Verificação de conhecimentos prévios em Python, HTTP e conceitos de API  
- **Avaliação formativa:** Implementação incremental do sistema Lunysse, peer review de código, testes funcionais  
- **Avaliação somativa:** Sistema Lunysse completo e funcional com todos os requisitos implementados  

### Instrumentos de Avaliação  
- **Ficha de observação** para acompanhar desenvolvimento das funcionalidades  
- **Estudo de caso** com cenários reais de uso do sistema  
- **Autoavaliação** do progresso no desenvolvimento da API  
- **Avaliação entre pares** através de code review  
- **Projetos e entregas práticas** com sistema funcional e documentado  

---

## Orientações específicas para esta Situação de Aprendizagem  

- **Estabelecer ambiente colaborativo:** Incentivar desenvolvimento em pares e revisão de código entre alunos  
- **Foco na aplicação prática:** Cada conceito deve ser imediatamente aplicado no sistema Lunysse  
- **Suporte individualizado:** Acompanhar dificuldades específicas no desenvolvimento de APIs  
- **Incentivo à reflexão crítica:** Promover análise de arquitetura, performance e segurança  
- **Monitoramento contínuo:** Verificar progresso através de entregas incrementais do sistema  

---

## Recursos Didáticos  

### RD Padrão  
- Computadores com Python, FastAPI e SQLite instalados  
- Postman ou Insomnia para testes de API  
- VSCode com extensões para desenvolvimento Python  
- Git para versionamento de código  
- Documentação oficial FastAPI e SQLAlchemy  

### RD Complementar  
- Swagger UI integrado para documentação interativa  
- GitHub para repositórios e colaboração  
- Jupyter Notebook para experimentação ML  
- Datasets médicos simulados para testes  
- Ferramentas de monitoramento de API  