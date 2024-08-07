import logging

logger = logging.getLogger(__name__)

def logger_config(module):
    """
    Configures logging for the given module name with a specified level.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(module)
