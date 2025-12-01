# 📋 Documentação Completa das Rotas - API Lunysse

**Guia completo para implementação no Frontend**

## 🔧 Configuração Base

### URL Base
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

### Headers Padrão
```javascript
const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Bearer ${token}` // Quando autenticado
};
```

---

## 🔐 AUTENTICAÇÃO

### 1. Login
**POST** `/auth/login`

```javascript
// Request
const loginUser = async (email, password) => {
  const response = await fetch(`${API_BASE_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  return response.json();
};

// Exemplo de uso
const result = await loginUser('ana@test.com', '123456');
```

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "name": "Dra. Ana Costa",
    "email": "ana@test.com",
    "user_type": "psychologist",
    "specialty": "TCC"
  }
}
```

### 2. Registro
**POST** `/auth/register`

```javascript
const registerUser = async (userData) => {
  const response = await fetch(`${API_BASE_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userData)
  });
  return response.json();
};

// Exemplo
const newUser = {
  name: "João Silva",
  email: "joao@test.com",
  password: "123456",
  user_type: "patient", // ou "psychologist"
  specialty: null // apenas para psicólogos
};
```

---

## 👥 PACIENTES

### 1. Listar Pacientes
**GET** `/patients/`

```javascript
const getPatients = async (token) => {
  const response = await fetch(`${API_BASE_URL}/patients/`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

**Comportamento por tipo de usuário:**
- **Psicólogos**: Veem todos os seus pacientes
- **Pacientes**: Veem apenas seus próprios dados

**Response:**
```json
[
  {
    "id": 1,
    "name": "Maria Santos",
    "email": "maria@test.com",
    "age": 28,
    "phone": "(11) 99999-9999",
    "psychologist_id": 1,
    "created_at": "2024-01-15T10:30:00",
    "total_sessions": 5,
    "last_session": "2024-01-20T14:00:00",
    "status": "Ativo"
  }
]
```

### 2. Detalhes do Paciente
**GET** `/patients/{patient_id}`

```javascript
const getPatientDetails = async (patientId, token) => {
  const response = await fetch(`${API_BASE_URL}/patients/${patientId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

### 3. Criar Paciente (Apenas Psicólogos)
**POST** `/patients/`

```javascript
const createPatient = async (patientData, token) => {
  const response = await fetch(`${API_BASE_URL}/patients/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(patientData)
  });
  return response.json();
};

// Exemplo
const newPatient = {
  name: "Carlos Oliveira",
  email: "carlos@test.com",
  phone: "(11) 88888-8888",
  birth_date: "1990-05-15"
};
```

### 4. Atualizar Paciente (Apenas Psicólogos)
**PUT** `/patients/{patient_id}`

```javascript
const updatePatient = async (patientId, patientData, token) => {
  const response = await fetch(`${API_BASE_URL}/patients/${patientId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(patientData)
  });
  return response.json();
};
```

### 5. Sessões do Paciente
**GET** `/patients/{patient_id}/sessions`

```javascript
const getPatientSessions = async (patientId, token) => {
  const response = await fetch(`${API_BASE_URL}/patients/${patientId}/sessions`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

**Permissões:**
- **Psicólogos**: Podem ver sessões de seus pacientes
- **Pacientes**: Podem ver apenas suas próprias sessões

### 6. Adicionar Anotação (Apenas Psicólogos)
**POST** `/patients/{patient_id}/notes`

```javascript
const addPatientNote = async (patientId, note, token) => {
  const response = await fetch(`${API_BASE_URL}/patients/${patientId}/notes`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ note })
  });
  return response.json();
};
```

**Response:**
```json
{
  "id": 1,
  "message": "Anotação adicionada com sucesso",
  "note": "[25/01/2024 14:30] Paciente demonstrou melhora significativa"
}
```

---

## 📅 AGENDAMENTOS

### 1. Listar Agendamentos
**GET** `/appointments/`

```javascript
const getAppointments = async (token, filters = {}) => {
  const params = new URLSearchParams(filters);
  const response = await fetch(`${API_BASE_URL}/appointments/?${params}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};

// Filtros disponíveis
const filters = {
  status: 'agendado', // agendado, concluido, cancelado
  date_from: '2024-01-01',
  date_to: '2024-01-31',
  patient_id: 1
};
```

**Response:**
```json
[
  {
    "id": 1,
    "patient_id": 1,
    "patient_name": "Maria Santos",
    "psychologist_id": 1,
    "psychologist_name": "Dra. Ana Costa",
    "appointment_date": "2024-01-25T14:00:00",
    "status": "agendado",
    "notes": "Primeira consulta",
    "created_at": "2024-01-20T10:00:00"
  }
]
```

### 2. Criar Agendamento
**POST** `/appointments/`

```javascript
const createAppointment = async (appointmentData, token) => {
  const response = await fetch(`${API_BASE_URL}/appointments/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(appointmentData)
  });
  return response.json();
};

// Exemplo
const newAppointment = {
  patient_id: 1,
  psychologist_id: 1,
  appointment_date: "2024-01-25T14:00:00",
  notes: "Consulta de acompanhamento"
};
```

### 3. Atualizar Agendamento
**PUT** `/appointments/{appointment_id}`

```javascript
const updateAppointment = async (appointmentId, updateData, token) => {
  const response = await fetch(`${API_BASE_URL}/appointments/${appointmentId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(updateData)
  });
  return response.json();
};

// Exemplo - Reagendar
const updateData = {
  appointment_date: "2024-01-26T15:00:00",
  status: "reagendado"
};
```

### 4. Cancelar Agendamento
**DELETE** `/appointments/{appointment_id}`

```javascript
const cancelAppointment = async (appointmentId, token) => {
  const response = await fetch(`${API_BASE_URL}/appointments/${appointmentId}`, {
    method: 'DELETE',
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

### 5. Horários Disponíveis
**GET** `/appointments/available-slots`

```javascript
const getAvailableSlots = async (psychologistId, date, token) => {
  const params = new URLSearchParams({
    psychologist_id: psychologistId,
    date: date // YYYY-MM-DD
  });
  
  const response = await fetch(`${API_BASE_URL}/appointments/available-slots?${params}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

**Response:**
```json
{
  "date": "2024-01-25",
  "psychologist": "Dra. Ana Costa",
  "available_slots": [
    "09:00", "10:00", "11:00", "14:00", "15:00", "16:00"
  ]
}
```

---

## 🧠 PSICÓLOGOS

### 1. Listar Psicólogos
**GET** `/psychologists/`

```javascript
const getPsychologists = async () => {
  const response = await fetch(`${API_BASE_URL}/psychologists/`);
  return response.json();
};
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Dra. Ana Costa",
    "email": "ana@test.com",
    "specialty": "TCC",
    "active_patients": 12,
    "total_sessions": 156
  }
]
```

---

## 📋 SOLICITAÇÕES

### 1. Listar Solicitações
**GET** `/requests/`

```javascript
const getRequests = async (token, status = null) => {
  const params = status ? `?status=${status}` : '';
  const response = await fetch(`${API_BASE_URL}/requests/${params}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

**Comportamento por tipo de usuário:**
- **Psicólogos**: Veem solicitações direcionadas a eles
- **Pacientes**: Veem suas próprias solicitações

**Response:**
```json
[
  {
    "id": 1,
    "patient_name": "João Silva",
    "patient_email": "joao@test.com",
    "patient_phone": "(11) 77777-7777",
    "preferred_psychologist": 1,
    "description": "Ansiedade e depressão",
    "urgency": "media",
    "status": "pendente",
    "created_at": "2024-01-20T09:00:00"
  }
]
```

### 2. Criar Solicitação
**POST** `/requests/`

```javascript
const createRequest = async (requestData, token) => {
  const response = await fetch(`${API_BASE_URL}/requests/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(requestData)
  });
  return response.json();
};

// Exemplo
const newRequest = {
  patient_name: "Pedro Santos",
  patient_email: "pedro@test.com",
  patient_phone: "(11) 66666-6666",
  preferred_psychologist: "Dr. Carlos Mendes",
  reason: "Terapia familiar"
};
```

### 3. Atualizar Status da Solicitação
**PUT** `/requests/{request_id}`

```javascript
const updateRequestStatus = async (requestId, status, token) => {
  const response = await fetch(`${API_BASE_URL}/requests/${requestId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ status })
  });
  return response.json();
};

// Status: "pendente", "aprovada", "rejeitada"
```

---

## 📊 RELATÓRIOS

### 1. Relatório do Psicólogo
**GET** `/reports/{psychologist_id}`

```javascript
const getPsychologistReport = async (psychologistId, token) => {
  const response = await fetch(`${API_BASE_URL}/reports/${psychologistId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

**Response:**
```json
{
  "psychologist": {
    "id": 1,
    "name": "Dra. Ana Costa",
    "specialty": "TCC"
  },
  "stats": {
    "active_patients": 12,
    "total_sessions": 156,
    "sessions_this_month": 24,
    "attendance_rate": 85.5,
    "cancellation_rate": 14.5
  },
  "monthly_data": [
    {
      "month": "2024-01",
      "sessions": 24,
      "new_patients": 3,
      "attendance_rate": 87.5
    }
  ],
  "recent_sessions": [
    {
      "patient_name": "Maria Santos",
      "date": "2024-01-20T14:00:00",
      "status": "concluido"
    }
  ]
}
```

---

## 🤖 ANÁLISE DE MACHINE LEARNING

### 1. Análise Geral de Risco
**GET** `/ml/risk-analysis`

```javascript
const getRiskAnalysis = async (token) => {
  const response = await fetch(`${API_BASE_URL}/ml/risk-analysis`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

**Response:**
```json
{
  "summary": {
    "total_patients": 12,
    "high_risk": 2,
    "moderate_risk": 4,
    "low_risk": 6,
    "analysis_date": "2024-01-25T10:00:00"
  },
  "patients": [
    {
      "id": 1,
      "name": "Maria Santos",
      "risk_level": "baixo",
      "risk_score": 25,
      "main_reason": "Frequência regular de consultas"
    }
  ]
}
```

### 2. Análise Individual de Paciente
**GET** `/ml/risk-analysis/{patient_id}`

```javascript
const getPatientRiskAnalysis = async (patientId, token) => {
  const response = await fetch(`${API_BASE_URL}/ml/risk-analysis/${patientId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
};
```

**Response:**
```json
{
  "patient": "Maria Santos",
  "risk": "baixo",
  "risk_score": 25,
  "analysis": {
    "frequency_score": 85,
    "cancellation_rate": 10,
    "days_since_last": 7,
    "trend": "estável",
    "future_appointments": 2
  },
  "recommendations": [
    "Manter frequência atual",
    "Agendar próxima consulta"
  ],
  "stats": {
    "total_sessions": 8,
    "completed_sessions": 7,
    "cancelled_sessions": 1,
    "attendance_rate": 87.5
  }
}
```

---

## 🛠️ Implementação no Frontend

### 1. Classe de Serviço API

```javascript
class LunysseAPI {
  constructor(baseURL = 'http://localhost:8000') {
    this.baseURL = baseURL;
    this.token = localStorage.getItem('token');
  }

  setToken(token) {
    this.token = token;
    localStorage.setItem('token', token);
  }

  getHeaders(includeAuth = true) {
    const headers = { 'Content-Type': 'application/json' };
    if (includeAuth && this.token) {
      headers['Authorization'] = `Bearer ${this.token}`;
    }
    return headers;
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      headers: this.getHeaders(options.auth !== false),
      ...options
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  }

  // Métodos de autenticação
  async login(email, password) {
    const data = await this.request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
      auth: false
    });
    
    if (data.access_token) {
      this.setToken(data.access_token);
    }
    
    return data;
  }

  // Métodos de pacientes
  async getPatients() {
    return this.request('/patients/');
  }

  async createPatient(patientData) {
    return this.request('/patients/', {
      method: 'POST',
      body: JSON.stringify(patientData)
    });
  }

  // Métodos de agendamentos
  async getAppointments(filters = {}) {
    const params = new URLSearchParams(filters);
    return this.request(`/appointments/?${params}`);
  }

  async createAppointment(appointmentData) {
    return this.request('/appointments/', {
      method: 'POST',
      body: JSON.stringify(appointmentData)
    });
  }

  // Análise ML
  async getRiskAnalysis() {
    return this.request('/ml/risk-analysis');
  }
}

// Uso
const api = new LunysseAPI();
```

### 2. Hooks React (Exemplo)

```javascript
// useAuth.js
import { useState, useEffect } from 'react';

export const useAuth = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const login = async (email, password) => {
    try {
      const data = await api.login(email, password);
      setUser(data.user);
      return data;
    } catch (error) {
      throw error;
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
    api.token = null;
  };

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      // Verificar se token é válido
      api.getPatients()
        .then(() => setLoading(false))
        .catch(() => {
          logout();
          setLoading(false);
        });
    } else {
      setLoading(false);
    }
  }, []);

  return { user, login, logout, loading };
};
```

### 3. Tratamento de Erros

```javascript
const handleAPIError = (error) => {
  if (error.message.includes('401')) {
    // Token expirado - redirecionar para login
    localStorage.removeItem('token');
    window.location.href = '/login';
  } else if (error.message.includes('403')) {
    // Sem permissão
    alert('Você não tem permissão para esta ação');
  } else if (error.message.includes('404')) {
    // Recurso não encontrado
    alert('Recurso não encontrado');
  } else {
    // Erro genérico
    alert('Erro na comunicação com o servidor');
  }
};
```

---

## 📱 Exemplos de Componentes

### 1. Lista de Pacientes

```javascript
const PatientsList = () => {
  const [patients, setPatients] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPatients = async () => {
      try {
        const data = await api.getPatients();
        setPatients(data);
      } catch (error) {
        handleAPIError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchPatients();
  }, []);

  if (loading) return <div>Carregando...</div>;

  return (
    <div>
      {patients.map(patient => (
        <div key={patient.id}>
          <h3>{patient.name}</h3>
          <p>Idade: {patient.age}</p>
          <p>Sessões: {patient.total_sessions}</p>
        </div>
      ))}
    </div>
  );
};
```

### 2. Formulário de Agendamento

```javascript
const AppointmentForm = ({ onSuccess }) => {
  const [formData, setFormData] = useState({
    patient_id: '',
    appointment_date: '',
    notes: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.createAppointment(formData);
      onSuccess();
    } catch (error) {
      handleAPIError(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <select 
        value={formData.patient_id}
        onChange={(e) => setFormData({...formData, patient_id: e.target.value})}
      >
        <option value="">Selecione o paciente</option>
        {/* Opções dos pacientes */}
      </select>
      
      <input
        type="datetime-local"
        value={formData.appointment_date}
        onChange={(e) => setFormData({...formData, appointment_date: e.target.value})}
      />
      
      <textarea
        placeholder="Observações"
        value={formData.notes}
        onChange={(e) => setFormData({...formData, notes: e.target.value})}
      />
      
      <button type="submit">Agendar</button>
    </form>
  );
};
```

---

## 🔒 Códigos de Status HTTP

| Código | Significado | Ação no Frontend |
|--------|-------------|------------------|
| 200 | Sucesso | Processar dados normalmente |
| 201 | Criado | Mostrar mensagem de sucesso |
| 400 | Dados inválidos | Mostrar erros de validação |
| 401 | Não autenticado | Redirecionar para login |
| 403 | Sem permissão | Mostrar mensagem de erro |
| 404 | Não encontrado | Mostrar "não encontrado" |
| 500 | Erro interno | Mostrar erro genérico |

---

## 📋 Checklist de Implementação

### ✅ Autenticação
- [ ] Implementar login/logout
- [ ] Armazenar token no localStorage
- [ ] Interceptar respostas 401
- [ ] Renovar token automaticamente

### ✅ Pacientes
- [ ] Lista de pacientes
- [ ] Detalhes do paciente
- [ ] Formulário de cadastro
- [ ] Histórico de sessões

### ✅ Agendamentos
- [ ] Calendário de agendamentos
- [ ] Formulário de novo agendamento
- [ ] Horários disponíveis
- [ ] Reagendamento/cancelamento

### ✅ Relatórios
- [ ] Dashboard com estatísticas
- [ ] Gráficos de performance
- [ ] Análise de risco ML
- [ ] Exportação de dados

### ✅ UX/UI
- [ ] Loading states
- [ ] Tratamento de erros
- [ ] Validação de formulários
- [ ] Responsividade mobile

---

**💡 Esta documentação fornece tudo que você precisa para implementar um frontend completo consumindo a API Lunysse. Cada endpoint está documentado com exemplos práticos de código JavaScript/React.**