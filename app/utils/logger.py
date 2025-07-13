import logging

def get_logger(name: str = "GESTAO_FUNCIONARIOS"):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def log_event(logger, endpoint, status, message, **context):
    extra = {"endpoint": endpoint, "status": status, **context}
    logger.info(f"{message}", extra=extra)
