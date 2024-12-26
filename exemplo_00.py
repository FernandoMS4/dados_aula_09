from loguru import logger # type: ignore

logger.add("meu_app.log")

def soma(x:int, y:int)->int:
    return x + y

logger.info(soma(45,123))