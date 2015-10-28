import unittest
import re
import os
from logger.logHandler import LogHandler
from logger.common.Constants import Constants
from logger.common import configWriter
from logger.common.configReader import ConfigReader
#import pdb

class TestLogHandler(unittest.TestCase):

  SERVICE = "demo_service"
  EXPECTED_STRING = "Region : demo_region\nZone : demo_zone\nHost : demo_host\n"
  FILENAME = "metric.log"
  MSG = "demo_msg"
  NAME = "demo_name"
  MTYPE = "demo_metricType"
  COUNT = 20
  TIME = 20.25
  socket = 6000

  def setUp(self):
    #pdb.set_trace()
    TestLogHandler.socket = TestLogHandler.socket + 1
    configWriter.CreateConfigFile("config.cfg", "Constants", "Socket", "tcp://127.0.0.1:"+`TestLogHandler.socket`)
    configWriter.CreateConfigFile("config.cfg", "Constants", "LogDir", ".")
    configWriter.CreateConfigFile("config.cfg", "Constants", "Filename", "metric.log")

  def test_dirIfNotExists(self):
   # pdb.set_trace()
    logHandler = LogHandler(TestLogHandler.SERVICE, "config.cfg")
    self.assertTrue(os.path.exists(os.path.join(os.path.join(Constants.getLogDir(), Constants.getHostname()),TestLogHandler.SERVICE)))

  def test_dirIfExists(self):
    new_logHandler = LogHandler(TestLogHandler.SERVICE, "config.cfg")
    self.assertTrue(os.path.exists(os.path.join(os.path.join(Constants.getLogDir(), Constants.getHostname()),TestLogHandler.SERVICE)))

  @unittest.skip("skip")
  def test_filepath(self):
    self.assertTrue(os.path.exists(Constants.getLogDir() + "/" + TestLogHandler.SERVICE + "/" + TestLogHandler.FILENAME))

  @unittest.skip("skip")
  def test_appendLog(self):
    self.logHandler.appendLog(TestLogHandler.MSG)
    fileHandler = open(Constants.getLogDir() + "/" + TestLogHandler.SERVICE + "/" + TestLogHandler.FILENAME, 'r')
    self.assertNotEqual(re.search(TestLogHandler.MSG, fileHandler.read()), None)

  @unittest.skip("skip")
  def test_appendCountLog(self):
    self.logHandler.appendCountLog(TestLogHandler.NAME, TestLogHandler.MTYPE, TestLogHandler.COUNT)
    fileHandler = open(Constants.getLogDir() + "/" + TestLogHandler.SERVICE + "/" + TestLogHandler.FILENAME, 'r')
    testString = fileHandler.read()
    self.assertNotEqual(re.search(TestLogHandler.NAME, testString), None)
    self.assertNotEqual(re.search(TestLogHandler.MTYPE, testString), None)
    self.assertNotEqual(re.search(`TestLogHandler.COUNT`, testString), None)

  @unittest.skip("skip")
  def test_appendTimeLog(self):
    self.logHandler.appendTimeLog(TestLogHandler.NAME, TestLogHandler.MTYPE, TestLogHandler.TIME)
    fileHandler = open(Constants.getLogDir() + "/" + TestLogHandler.SERVICE + "/" + TestLogHandler.FILENAME, 'r')
    testString = fileHandler.read()
    self.assertNotEqual(re.search(TestLogHandler.NAME, testString), None)
    self.assertNotEqual(re.search(TestLogHandler.MTYPE, testString), None)
    self.assertNotEqual(re.search(`TestLogHandler.TIME`, testString), None)

if __name__ == '__main__':
  unittest.main()

