import logging

def setup_logger():
    logger = logging.getLogger("CarRegValuation")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("test_log.log", mode="w")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger