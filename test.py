#!/usr/bin/env python
# encoding=UTF-8

import os
import time
import mlogger


#路径配置
ROOT_DIR = os.getcwd()

LOG_LEVEL_DEF = 10

LOG_CONFIG_MAP = {
    'main': {
        'name':'main',
        'level': LOG_LEVEL_DEF,
        'filepath': os.path.join(ROOT_DIR, 'log', 'test'),
    }
}
#全局logger
LOGGER = mlogger.getReLogger(LOG_CONFIG_MAP['main']['name'], LOG_CONFIG_MAP['main']['filepath'], 
    LOG_CONFIG_MAP['main']['level'])


for x in xrange(5):
    LOGGER.info('Hello!')
    LOGGER.error('World!')
    time.sleep(1)
