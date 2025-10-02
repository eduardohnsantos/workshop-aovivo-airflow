from time import sleep

from loguru import logger

logger.add("execution.log", format="{time} - {message}", level="INFO", rotation="1 day")

def primeira_atividade():
    logger.info("Primeira atividade iniciada")
    sleep(1)

def segunda_atividade():
    logger.info("Segunda atividade iniciada")
    sleep(1)

def terceira_atividade():
    logger.info("Terceira atividade iniciada")
    sleep(1)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline finalizada")

if __name__ == "__main__":
   while True: 
        pipeline()
        sleep(10)