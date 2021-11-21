import logging
import inspect

class QLogger:

    def __init__(self,logLevel=logging.DEBUG) -> None:
        self.logLevel   = logLevel
        self.logFormat  = "|%(asctime)s|%(levelname)8s|> %(message)-50s <|%(name)s"

    # def where_am_i(self):
    #     prev_frame = inspect.currentframe().f_back.f_back
    #     if len(prev_frame.f_locals) == 0 :
    #         # if f_back in function
    #         def_name = inspect.getframeinfo(prev_frame).function
    #         return def_name

    #     else:
    #         # if f_back in class
    #         the_class = prev_frame.f_locals["self"].__class__.__name__
    #         the_method = prev_frame.f_code.co_name
    #         return f"{the_class}.{the_method}"

    #         #print(f"class:{the_class}, method:{the_method}")
    # def get_formatter(self):

    #     # wherein = self.where_am_i()
    #     prev_frame = inspect.currentframe().f_back.f_back.f_back.f_back
    #     if len(prev_frame.f_locals) == 0 :
    #         # if f_back in function
    #         def_name = inspect.getframeinfo(prev_frame).function
    #         wherein = def_name
    #     else:
    #         the_class = prev_frame.f_locals["self"].__class__.__name__
    #         the_method = prev_frame.f_code.co_name
    #         wherein =  f"{the_class}.{the_method}"

    #     logformat = f"{self.logFormat}({wherein})"
    #     return logformat

    def get_logger_stream(self, logName):
        logger = logging.getLogger(logName)

        formatter = logging.Formatter(self.logFormat)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.setLevel(self.logLevel)
        logger.addHandler(stream_handler)

        return logger