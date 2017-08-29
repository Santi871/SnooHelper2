import logging
import config


logging_filename = 'snoohelper_log.txt'
handler = logging.FileHandler(filename=logging_filename, encoding='utf-8')
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)


def get_logger(name, level=config.main_logging_level):
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
