import logging, sys

# https://docs.python.org/3/library/logging.html#logrecord-attributes
# https://stackoverflow.com/questions/54423838/python-logging-to-console
def custom_logger() -> logging.Logger:
    logger = logging.getLogger('custom_logger')
    format = logging.Formatter('[%(asctime)s] | [%(filename)s] | [%(levelname)s] | [%(message)s]')

    handler = logging.StreamHandler(sys.stdout)                             
    handler.setLevel(logging.DEBUG)                                        
    handler.setFormatter(format)                                     
    logger.addHandler(handler)   
    logger.setLevel(logging.DEBUG)     

    return logger