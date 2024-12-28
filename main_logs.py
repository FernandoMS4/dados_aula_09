from loguru import logger
from functools import wraps
import time

# logger.add(
#     sink=stderr,
#     format="{time} {level} {message} {file}",
#     level="INFO"
# )

logger.add(
    "my_info_logs.log",
    format="{time} {level} {message} {file}",
    level="INFO"
)
logger.add(
    "my_critical_logs.log",
    format="{time} {level} {message} {file}",
    level="ERROR"
)

def checa_logs(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs{kwargs}")
        try:
            result = func(*args,**kwargs)
            logger.info(f"Função '{func.__name__} retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise
    return wrapper

def timer_dec(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        logger.info(f"Função {func.__name__} executada em {start_time - end_time:.4f} segundos")
        return result
    return wrapper