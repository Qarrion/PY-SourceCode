from concurrent import futures
import logging
import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


"""Producer and Comsumer"""
