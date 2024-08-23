import logging

def log_message(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - (%(name)s) - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)