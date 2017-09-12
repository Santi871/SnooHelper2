import logging

try:
    import config
except ImportError:
    import config_env_vars as config


handler = logging.FileHandler(filename=config.logging_filename, encoding='utf-8')
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)


def get_logger(name, level=config.main_logging_level):
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
