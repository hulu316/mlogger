#!/usr/bin/env python
# encoding=UTF-8

import logging
from logging import Filter, Logger
from logging import FATAL, WARNING, INFO, DEBUG, NOTSET
from logging.handlers import TimedRotatingFileHandler


class UpLevelFilter(Filter):
    def __init__(self, level):
        Filter.__init__(self)
        self.level = level

    def filter(self, record):
        return record.levelno <= self.level


class ReLogger(Logger):
    def __init__(self, name, level=NOTSET):
        Logger.__init__(self, name, level)

    def build(self, filePath, formatter):
        commonFileName = "%s.log" % filePath
        errorFileName = "%s.err.log" % filePath

        commonHandler = TimedRotatingFileHandler(commonFileName, when='d')
        commonHandler.setLevel(DEBUG)
        commonHandler.setFormatter(formatter)
        commonHandler.addFilter(UpLevelFilter(INFO))
        self.addHandler(commonHandler)

        errorHandler = TimedRotatingFileHandler(errorFileName, when='d')
        errorHandler.setLevel(WARNING)
        errorHandler.setFormatter(formatter)
        errorHandler.addFilter(UpLevelFilter(FATAL))
        self.addHandler(errorHandler)


LOG_FORMATTER = logging.Formatter('[%(levelname)s] [%(asctime)s] '
    '[%(message)s] [%(module)s %(filename)s %(lineno)d]')

def getReLogger(name, filePath, level=NOTSET, formatter=LOG_FORMATTER):
    if name:
        Logger.manager.setLoggerClass(ReLogger)
        logger = Logger.manager.getLogger(name)
        logger.build(filePath, formatter)
        logger.setLevel(level)
        return logger

