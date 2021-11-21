from Qlogging import QLogger

qlogger = QLogger.QLogger().get_logger_stream(__name__)


class Myclass2:
    def myfunction2(self):
        qlogger.debug("myfunction in cls")
        qlogger.info("myfunction in cls")
        qlogger.warning("myfunction in cls")
        qlogger.error("myfunction in cls")
        qlogger.critical("myfunction in cls")

def Myfunction2():
    qlogger.debug("myfunction in fun")
    qlogger.info("myfunction in fun")
    qlogger.warning("myfunction in fun")
    qlogger.error("myfunction in fun")
    qlogger.critical("myfunction in fun")