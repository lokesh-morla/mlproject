from src.exception import CustomException
import sys
import logging

try:
    a = 1/0
except Exception as e:
    logging.info("Divided by zero")
    raise CustomException(e, sys)
