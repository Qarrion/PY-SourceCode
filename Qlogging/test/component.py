
# %%
# https://www.daleseo.com/python-logging-config/

import logging

#* 포멧 객체
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#* 콘솔 출력 관련
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

#%%
#* 파일 저장 관련
file_handler = logging.FileHandler("file.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

#* 로거 객체 (ROOT)
root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.WARNING)


#%%
    # logging.debug("디버그")
    # logging.info("정보")
    # logging.warning("경고")
    # logging.error("오류")
    # logging.critical("심각")

root_logger.debug("test")
root_logger.info("test")
root_logger.warning("test")
root_logger.error("test")

# %%

import logging
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("file.log")
file_handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.WARNING)
root_logger.warning("test")