import string
import random

def generate_short_code(length: int = 6) -> str:
    """
    Gera um código aleatório alfanumérico de tamanho definido.
    Exemplo: 'aZ97Bx'
    """
    # ascii_letters (a-z, A-Z) + digits (0-9)
    characters = string.ascii_letters + string.digits
    
    # Gera uma string escolhendo caracteres aleatórios
    return ''.join(random.choice(characters) for _ in range(length))