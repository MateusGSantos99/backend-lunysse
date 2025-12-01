import logging
import sys
from datetime import datetime

def setup_logging():
    """Configura logging estruturado para a aplicação"""
    
    # Formato do log
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configuração básica
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(f"logs/app_{datetime.now().strftime('%Y%m%d')}.log")
        ]
    )
    
    # Logger específico para a aplicação
    logger = logging.getLogger("lunysse_api")
    
    return logger