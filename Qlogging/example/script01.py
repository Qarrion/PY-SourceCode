from Qlogging.example import mylogger
my_logger = mylogger.MyLogger()
stream_logger = my_logger.mylogger_stream(__name__)
class Myclass():
    def myfuction(self):
        stream_logger.debug("hey")


myclass = Myclass()
myclass.myfuction()
