import os
from dotenv import load_dotenv
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
# =============================
# CONFIGURAÇÃO DA API
# =============================
load_dotenv()
 
def get_email_client():
    """Retorna o cliente configurado para envio de e-mail."""
    api_key = os.getenv("BREVO_API_KEY")  # SEMPRE usar variável de ambiente!
    if not api_key:
        raise ValueError("A variável de ambiente BREVO_API_KEY não está definida.")
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = api_key
    return sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )
# =============================
# FUNÇÃO GENÉRICA DE ENVIO
# =============================
def send_email(to_email: str, subject: str, html_content: str,
               sender_email=None, sender_name="Lunysse"):
    if sender_email is None:
        sender_email = os.getenv("EMAIL_SENDER")
    """Função genérica para envio de e-mails transacionais."""
    if not to_email:
        raise ValueError("E-mail do destinatário está vazio.")
    api_instance = get_email_client()
    email_data = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": to_email}],
        subject=subject,
        html_content=html_content,
        sender={"email": sender_email, "name": sender_name},
    )
    try:
        api_instance.send_transac_email(email_data)
        print(f"E-mail enviado para {to_email}")
        return True
    except ApiException as e:
        print(f"Erro ao enviar e-mail para {to_email}: {e}")
        return False
 
# =============================
# EMAIL: CONFIRMAÇÃO DE AGENDAMENTO
# =============================
 
def send_email_appointment(client_email: str, client_name: str, date: str, time: str):
    email = os.getenv("EMAIL_DOMAIN")
    html = f"""
        <h3>Olá {client_name},</h3>
        <p>Sua consulta foi agendada com sucesso.</p>
        <p><strong>Data:</strong> {date}</p>
        <p><strong>Horário:</strong> {time}</p>
        <p>Obrigado por utilizar nossa plataforma.</p>
    """
 
    return send_email(
        to_email=client_email,
        subject="Confirmação de Agendamento",
        html_content=html,
        sender_email=email,
        sender_name="Sistema de Agendamentos"
    )
 
 
# =============================
# EMAIL: SOLICITAÇÃO ACEITA
# =============================
 
def send_email_request_accepted(patient_email: str, patient_name: str, psychologist_name: str):
    email = os.getenv("EMAIL_DOMAIN")
    html = f"""
        <h3>Olá {patient_name},</h3>
        <p>Sua solicitação foi aceita pelo psicólogo <strong>{psychologist_name}</strong>.</p>
        <p>Em breve ele entrará em contato para combinar o melhor horário.</p>
        <p>Obrigado por utilizar nossa plataforma.</p>
    """
 
    return send_email(
        to_email=patient_email,
        subject="Sua Solicitação Foi Aceita",
        html_content=html,
        sender_email=email,
        sender_name="Sistema de Agendamentos"
    )
# =============================
# EMAIL: SOLICITAÇÃO REJEITADA
# =============================    
def send_email_request_reject(patient_email: str, patient_name: str, psychologist_name: str):
    email = os.getenv("EMAIL_DOMAIN")
    html = f"""
        <h3>Olá {patient_name},</h3>
        <p>Sua solicitação foi recusada pelo psicólogo <strong>{psychologist_name}</strong>.</p>
        <p Este psicólogo não aceitou sua solicitação, você pode escolher outro psicologo para enviar uma nova solicitação ou tentar novamente a slicitação com o mesmo psicólogo.</p>
        <p>Obrigado por utilizar nossa plataforma.</p>
    """
 
    return send_email(
        to_email=patient_email,
        subject="Sua Solicitação Foi Negada",
        html_content=html,
        sender_email=email,
        sender_name="Sistema de Agendamentos"
    )
# =============================
# EMAIL: SOLICITAÇÃO para psicologo
# =============================    
def send_email_new_request_to_psychologist(psychologist_email: str, psychologist_name: str, patient_name: str):
    email = os.getenv("EMAIL_DOMAIN")
    html = f"""
        <h3>Olá psicologo {psychologist_name},</h3>
        <p>Você possui uma nova solicitação de paciente no sistema, o  <strong>{patient_name}</strong> deseja ser atendido por você.</p>
        <p>Você pode acessar o sistema pelo link abaixo e aceitar ou recusar o paciente.</p>
        <button
            onclick="window.location.href='https://lunysse.vercel.app/login'"
            style="
                background-color: #4A4AFF;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
            ">Entrar</button>
        <p>Obrigado por utilizar nossa plataforma.</p>
    """
    return send_email(
        to_email=psychologist_email,
        subject="Nova solicitação de paciente no sistema",
        html_content=html,
        sender_email=email,
        sender_name="Sistema de Agendamentos"
    )
# =============================
# EMAIL: CONSULTA REAGENDADA
# =============================

def send_email_appointment_rescheduled(client_email: str, client_name: str, date: str, time: str):
    email = os.getenv("EMAIL_DOMAIN")
    html = f"""
        <h3>Olá {client_name},</h3>
        <p>Sua consulta foi <strong>reagendada com sucesso</strong>.</p>
        <p><strong>Nova Data:</strong> {date}</p>
        <p><strong>Novo Horário:</strong> {time}</p>
        <p>Caso não tenha solicitado essa alteração, entre em contato pelo sistema.</p>
        <p>Obrigado por utilizar nossa plataforma.</p>
    """

    return send_email(
        to_email=client_email,
        subject="Consulta Reagendada",
        html_content=html,
        sender_email=email,
        sender_name="Sistema de Agendamentos"
    )
# =============================
# EMAIL: CONSULTA CANCELADA
# =============================

def send_email_appointment_canceled(client_email: str, client_name: str, psychologist_name: str):
    email = os.getenv("EMAIL_DOMAIN")
    html = f"""
        <h3>Olá {client_name},</h3>
        <p>Sua consulta com <strong>{psychologist_name}</strong> foi <strong>cancelada</strong>.</p>
        <p>Se desejar, você pode acessar o sistema para marcar uma nova consulta.</p>
        <button
            onclick="window.location.href='https://lunysse.vercel.app/home'"
            style="
                background-color: #4A4AFF;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
            ">Agendar Nova Consulta</button>
        <p>Obrigado por utilizar nossa plataforma.</p>
    """

    return send_email(
        to_email=client_email,
        subject="Consulta Cancelada",
        html_content=html,
        sender_email=email,
        sender_name="Sistema de Agendamentos"
    )
 