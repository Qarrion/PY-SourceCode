#%%
#https://www.daleseo.com/python-logging/
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("logging msg")


#%%
import logging

logging.basicConfig(level=logging.DEBUG, format="'%(asctime)s - %(message)s'")


def main():
    logging.debug("디버그")
    logging.info("정보")
    logging.warning("경고")
    logging.error("오류")
    logging.critical("심각")


if __name__ == "__main__":
    main()


# %%

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="'%(asctime)s - %(message)s'"
    )
logging.debug("logging with format")

