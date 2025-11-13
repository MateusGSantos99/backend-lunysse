# Importações necessárias
import os  # Para acessar variáveis de ambiente do sistema
from datetime import datetime, date, timezone, timedelta  # Para manipular datas e tempos
from passlib.context import CryptContext  # Biblioteca para hash e verificação de senhas
from jose import JWTError, jwt  # Biblioteca para criação e validação de tokens JWT
from dotenv import load_dotenv  # Para carregar variáveis de ambiente do arquivo .env

# ============================================================
# CARREGAMENTO E CONFIGURAÇÃO DE VARIÁVEIS DE AMBIENTE
# ============================================================

# Carrega as variáveis definidas no arquivo .env para o ambiente
load_dotenv()

# Recupera a chave secreta usada para assinar tokens JWT
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    # Garante que a aplicação não inicie sem uma chave segura
    raise ValueError("SECRET_KEY deve ser definida nas variáveis de ambiente")

# Define o algoritmo de criptografia a ser usado no JWT (padrão: HS256)
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Recupera o tempo de expiração do token em minutos, com tratamento de erros
try:
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
except (ValueError, TypeError):
    # Caso o valor no .env esteja incorreto, define o padrão como 30 minutos
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ============================================================
# CONFIGURAÇÃO DO HASH DE SENHA (Bcrypt)
# ============================================================

# Define o contexto de criptografia usando o algoritmo bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ------------------------------------------------------------
# Função para verificar se a senha informada corresponde ao hash armazenado
# ------------------------------------------------------------
def verify_password(plain_password, hashed_password):
    """
    Compara a senha em texto puro (plain_password) com o hash armazenado.
    Retorna True se coincidem, False caso contrário.
    """
    return pwd_context.verify(plain_password, hashed_password)

# ------------------------------------------------------------
# Função para gerar o hash seguro da senha do usuário
# ------------------------------------------------------------
def get_password_hash(password):
    """
    Recebe a senha em texto puro e retorna seu hash criptografado com bcrypt.
    """
    return pwd_context.hash(password)

# ============================================================
# CRIAÇÃO DE TOKEN JWT (Autenticação)
# ============================================================

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Cria um token JWT com base nos dados do usuário.
    - 'data' contém as informações (claims) que serão codificadas no token.
    - 'expires_delta' define quanto tempo o token será válido.
    """
    to_encode = data.copy()  # Copia os dados do usuário
    
    # Define o tempo de expiração do token
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Caso nenhum tempo seja definido, o padrão é 15 minutos
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    # Adiciona a data de expiração ao dicionário de dados
    to_encode.update({"exp": expire})
    
    # Codifica os dados em um token JWT usando a SECRET_KEY e o algoritmo definido
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    # Retorna o token gerado
    return encoded_jwt

# ============================================================
# FUNÇÃO PARA CALCULAR IDADE A PARTIR DA DATA DE NASCIMENTO
# ============================================================

def calculate_age(birth_date: date) -> int:
    """
    Calcula a idade atual com base na data de nascimento (birth_date).
    Considera o mês e o dia para corrigir se o aniversário ainda não ocorreu no ano atual.
    """
    today = date.today()
    age = today.year - birth_date.year
    
    # Se o aniversário ainda não chegou este ano, subtrai 1 da idade
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    
    return age
