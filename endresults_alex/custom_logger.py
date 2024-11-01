import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - (%(name)s) - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("Hoi dit is een bericht")