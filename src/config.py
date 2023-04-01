import logging
import sys

logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - (%(filename)s, %(funcName)s): %(lineno)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

file_handler = logging.FileHandler("logs/api.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
