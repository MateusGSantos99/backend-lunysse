import re
from typing import Optional
from pydantic import validator

class SecurityValidators:
    """Validadores de segurança para entrada de dados"""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Valida formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_password_strength(password: str) -> tuple[bool, str]:
        """Valida força da senha"""
        if len(password) < 8:
            return False, "Senha deve ter pelo menos 8 caracteres"
        
        if not re.search(r'[A-Z]', password):
            return False, "Senha deve conter pelo menos uma letra maiúscula"
        
        if not re.search(r'[a-z]', password):
            return False, "Senha deve conter pelo menos uma letra minúscula"
        
        if not re.search(r'\d', password):
            return False, "Senha deve conter pelo menos um número"
        
        return True, "Senha válida"
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Valida formato de telefone brasileiro"""
        pattern = r'^\(\d{2}\)\s\d{4,5}-\d{4}$|^\d{10,11}$'
        return bool(re.match(pattern, phone.replace(' ', '')))
    
    @staticmethod
    def sanitize_input(text: str) -> str:
        """Remove caracteres potencialmente perigosos"""
        if not text:
            return ""
        
        # Remove tags HTML básicas
        text = re.sub(r'<[^>]+>', '', text)
        
        # Remove caracteres de controle
        text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
        
        return text.strip()