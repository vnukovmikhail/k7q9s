import logging

class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: '\033[90m',
        logging.INFO: '\033[96m',
        logging.WARNING: '\033[93m',
        logging.ERROR: '\033[91m',
        logging.CRITICAL: '\033[1;91m',
    }

    RESET = "\033[0m"

    def format(self, record):
        color = self.COLORS.get(record.levelno, self.RESET)
        message = super().format(record)
        return f"{color}{message}{self.RESET}"

def get_logger(name='app'):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_formatter = ColorFormatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger