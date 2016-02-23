import time
import socket
from configReader import ConfigReader
import configWriter
from monitorLog import monitorLog

'''
		Declares constants.
'''
class Constants:

    #LOGDIR = ConfigReader.getValue("Constants", "LogDir")
    #FILENAME = ConfigReader.getValue("Constants", "Filename")
    #SOCKET = ConfigReader.getValue("Constants", "Socket")
    RUNTIME = "Runtime" #this will be measured in miliseconds
    FAILCOUNT = "Failure Count"
    COUNT = "Counter"
# Use constants for metric type
    METRIC_TYPE = "Metric Type"
    METRIC_NAME = "Metric Name"
    HOST = "Host"
    SERVICE = "Service"
    TIME = "Timestamp"
    SEVERITY = "Severity"
    METRIC_VALUE = "Metric Value"
    SEPARATOR = " : "
    DELIMITER = "\n"

    def __init__(self, configFile):
        self.configReader = ConfigReader(configFile)

    def setLogDir(self, logdir):
        configWriter.CreateConfigFile("Constants", "LogDir", logdir)

    def getLogDir(self):
        try:
            logdir = self.configReader.getValue("Constants", "LogDir")
        except Exception as error:
            monitorLog.logError("Cannot get LogDir", error)
            raise error("Cannot get LogDir")
        return logdir

    def getFilename(self):
        try:
            filename = self.configReader.getValue("Constants", "Filename")
        except Exception as error:
            monitorLog.logError("Cannot get filename", error)
            raise error("Cannot get filename")
        return filename

    def getSocket(self):
        try:
            socket = self.configReader.getValue("Constants", "Socket")
        except Exception as error:
            monitorLog.logError("Cannot get socket", error)
            raise error("Cannot get socket")
        return socket

    '''
        Get hostname.
    '''
    @staticmethod
    def getHostname():
        try:
            hostname = socket.gethostname()
        except Exception as error:
            monitorLog.logError("Cannot get hostname", error)
            raise error("Cannot get hostname")
        return hostname
    '''
    @staticmethod
    def toStringCommon (service):
        return Constants.HOST + Constants.SEPARATOR + Constants.getHostname() + Constants.DELIMITER + Constants.SERVICE + Constants.SEPARATOR + service + Constants.DELIMITER

    @staticmethod
    def appendTimestamp (string):
        return string + Constants.TIME + Constants.SEPARATOR + `time.time()` + Constants.DELIMITER

    @staticmethod
    def toStringRuntime (name, mType, runtime, severity):
        return Constants.appendSeverity ( Constants.appendTimestamp ( Constants.prependMetricInfo ( name, mType, Constants.METRIC_VALUE + Constants.SEPARATOR + `runtime` + Constants.DELIMITER ) ), severity )

    @staticmethod
    def toStringCount (name, mType, count, severity):
        return Constants.appendSeverity ( Constants.appendTimestamp ( Constants.prependMetricInfo ( name, mType, Constants.METRIC_VALUE + Constants.SEPARATOR + `count` + Constants.DELIMITER) ), severity )

    @staticmethod
    def prependMetricInfo(name, mType, string):
        return Constants.METRIC_NAME + Constants.SEPARATOR + name + Constants.DELIMITER + Constants.METRIC_TYPE + Constants.SEPARATOR + mType + Constants.DELIMITER + string

    @staticmethod
    def appendSeverity(string, severity):
        return string + Constants.SEVERITY + Constants.SEPARATOR + `severity` + Constants.DELIMITER
    '''
    @staticmethod
    def createDictCommon (service):
        commonDict = {
            Constants.HOST : Constants.getHostname(),
            Constants.SERVICE : service
        }
        return commonDict

    @staticmethod
    def addTimeStamp (customDict):
        customDict.update({Constants.TIME : time.time()})
        return customDict

    @staticmethod
    def toDictRuntime (name, mType, runtime, severity):
        customDict = { Constants.METRIC_VALUE : runtime }
        return Constants.addSeveriety ( Constants.addTimeStamp (
            Constants.addMetricInfo ( name, mType, customDict ) ), severity)

    @staticmethod
    def toDictCount (name, mType, count, severity):
        customDict = { Constants.METRIC_VALUE : count }
        return Constants.addSeveriety ( Constants.addTimeStamp (
            Constants.addMetricInfo ( name, mType, customDict ) ), severity)


    @staticmethod
    def addMetricInfo (name, mType, customDict):
        metricDict = {
            Constants.METRIC_NAME : name,
            Constants.METRIC_TYPE : mType
        }
        customDict.update(metricDict)
        return customDict

    @staticmethod
    def addSeveriety (customDict, severity):
        severityDict = {Constants.SEVERITY : severity}
        customDict.update(severityDict)
        return customDict

    @staticmethod
    def addKeyValue (key, value, customDict = {}):
        pair = {key : value}
        customDict.update(pair)
        return customDict
