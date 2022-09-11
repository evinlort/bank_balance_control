import logging
import sys

logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - (%(filename)s, %(funcName)s): %(lineno)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
