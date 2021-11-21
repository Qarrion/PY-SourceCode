import logging
import inspect

class MyLogger:
    def mylogger_file(self,logLevel=logging.DEBUG):
        # set class/method name from where its colled
        logger_name = inspect.stack()[1][3]
        # create looger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # create console handler or file hanflder and set the log level
        file_handler = logging.FileHandler("automation.log")
        # create formatter - how you want your logs to be formatted
        formatter_file = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')
        # add formatter to colsole or file handler
        file_handler.setFormatter(formatter_file)
        # add console handler to logger
        logger.addHandler(file_handler)
        # application code - log msg
        return logger

mylog = MyLogger()

#log = mylog.mylogger_file()
#log.debug("test2")