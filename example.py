import logging, logging.config

# set up logging
logging.config.fileConfig("logging_config.ini")
logger = logging.getLogger('sLogger')
print(__name__)
# log something
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
