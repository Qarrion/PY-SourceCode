import logging
"""
    # logging.debug("디버그")
    # logging.info("정보")
    # logging.warning("경고")
    # logging.error("오류")
    # logging.critical("심각")
"""

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("file.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.WARNING)
root_logger.warning("test")