import requests
import json
import sys

BASE_URL = "http://localhost:8000"

class TestRunner:
    def __init__(self):
        self.token = None
        self.headers = {}
        self.user = None
        
    def login(self):
        print("🔐 Fazendo login...")
        login_data = {"email": "ana@test.com", "password": "123456"}
        
        try:
            response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
            if response.status_code == 200:
                data = response.json()
                self.token = data["access_token"]
                self.user = data["user"]
                self.headers = {"Authorization": f"Bearer {self.token}"}
                print(f"✅ Login: {self.user['name']}")
                return True
            else:
                print(f"❌ Login falhou: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Servidor não está rodando")
            return False
    
    def test_auth(self):
        print("\n🔑 TESTANDO AUTENTICAÇÃO")
        
        # Teste login inválido
        response = requests.post(f"{BASE_URL}/auth/login", json={"email": "invalid", "password": "wrong"})
        print(f"Login inválido: {'✅' if response.status_code == 401 else '❌'}")
        
        # Teste token válido
        response = requests.get(f"{BASE_URL}/patients/", headers=self.headers)
        print(f"Token válido: {'✅' if response.status_code == 200 else '❌'}")
    
    def test_patients(self):
        print("\n👥 TESTANDO PACIENTES")
        
        # Listar pacientes
        response = requests.get(f"{BASE_URL}/patients/", headers=self.headers)
        if response.status_code == 200:
            patients = response.json()
            print(f"✅ Listagem: {len(patients)} pacientes")
            
            if patients:
                patient_id = patients[0]["id"]
                # Detalhes do paciente
                response = requests.get(f"{BASE_URL}/patients/{patient_id}", headers=self.headers)
                print(f"Detalhes: {'✅' if response.status_code == 200 else '❌'}")
        else:
            print("❌ Erro na listagem")
    
    def test_psychologists(self):
        print("\n🧠 TESTANDO PSICÓLOGOS")
        
        response = requests.get(f"{BASE_URL}/psychologists/")
        if response.status_code == 200:
            psychs = response.json()
            print(f"✅ Listagem: {len(psychs)} psicólogos")
        else:
            print("❌ Erro na listagem")
    
    def test_appointments(self):
        print("\n📅 TESTANDO AGENDAMENTOS")
        
        # Listar agendamentos
        response = requests.get(f"{BASE_URL}/appointments/", headers=self.headers)
        if response.status_code == 200:
            appointments = response.json()
            print(f"✅ Listagem: {len(appointments)} agendamentos")
            
            if appointments:
                apt_id = appointments[0]["id"]
                # Detalhes do agendamento
                response = requests.get(f"{BASE_URL}/appointments/{apt_id}", headers=self.headers)
                print(f"Detalhes: {'✅' if response.status_code == 200 else '❌'}")
        else:
            print("❌ Erro na listagem")
    
    def test_requests(self):
        print("\n📋 TESTANDO SOLICITAÇÕES")
        
        response = requests.get(f"{BASE_URL}/requests/", headers=self.headers)
        if response.status_code == 200:
            requests_data = response.json()
            print(f"✅ Listagem: {len(requests_data)} solicitações")
        else:
            print("❌ Erro na listagem")
    
    def test_reports(self):
        print("\n📊 TESTANDO RELATÓRIOS")
        
        response = requests.get(f"{BASE_URL}/reports/{self.user['id']}", headers=self.headers)
        if response.status_code == 200:
            report = response.json()
            stats = report["stats"]
            print(f"✅ Relatório gerado:")
            print(f"   Pacientes ativos: {stats['active_patients']}")
            print(f"   Total sessões: {stats['total_sessions']}")
            print(f"   Taxa comparecimento: {stats['attendance_rate']}%")
        else:
            print("❌ Erro no relatório")
    
    def test_ml_analysis(self):
        print("\n🤖 TESTANDO ANÁLISE ML")
        
        # Análise geral
        response = requests.get(f"{BASE_URL}/ml/risk-analysis", headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            summary = data["summary"]
            patients = data["patients"]
            
            print(f"✅ Análise geral:")
            print(f"   Total: {summary['total_patients']}")
            print(f"   Alto risco: {summary['high_risk']}")
            print(f"   Moderado: {summary['moderate_risk']}")
            print(f"   Baixo: {summary['low_risk']}")
            
            # Análise individual
            if patients:
                patient_id = patients[0]["id"]
                response = requests.get(f"{BASE_URL}/ml/risk-analysis/{patient_id}", headers=self.headers)
                if response.status_code == 200:
                    patient_data = response.json()
                    print(f"✅ Análise individual:")
                    print(f"   {patient_data['patient']}: {patient_data['risk']}")
                    print(f"   Score: {patient_data['risk_score']}")
                else:
                    print("❌ Erro análise individual")
        else:
            print("❌ Erro análise geral")
    
    def run_all_tests(self):
        print("🧪 INICIANDO TESTES COMPLETOS DO SISTEMA LUNYSSE")
        print("=" * 50)
        
        if not self.login():
            print("❌ Não foi possível fazer login. Encerrando testes.")
            return False
        
        self.test_auth()
        self.test_patients()
        self.test_psychologists()
        self.test_appointments()
        self.test_requests()
        self.test_reports()
        self.test_ml_analysis()
        
        print("\n" + "=" * 50)
        print("✅ TESTES CONCLUÍDOS")
        return True

if __name__ == "__main__":
    runner = TestRunner()
    success = runner.run_all_tests()
    sys.exit(0 if success else 1)