#%%
#https://www.daleseo.com/python-logging/
import logging

#logging.basicConfig(level=logging.DEBUG, format="'%(asctime)s - %(message)s'")
logging.basicConfig(level=logging.DEBUG)
# %%

def main():
    logging.debug("test msg")
# %%
main()
# %%


mylogger = logging.getLogger("my")
mylogger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_hander = logging.StreamHandler()
stream_hander.setFormatter(formatter)
mylogger.addHandler(stream_hander)

file_handler = logging.FileHandler('my.log')
mylogger.addHandler(file_handler)

mylogger.info("server start!!!")

# 출처: https://hamait.tistory.com/880 [HAMA 블로그]
# %%
