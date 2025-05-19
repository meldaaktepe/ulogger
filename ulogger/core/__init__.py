"""Reporter Class."""
# from datetime import datetime
import logging

class Log_Levels:
    """Log Level Enum."""
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    HEADER = 21
    SUCCESS = 22
    FAIL = 23


# Colors
class LogColors:
    """Consoele Colors."""
    HEADER = "\033[35m"  # Magenta
    DEBUG = "\033[34m"  # BLUE
    INFO = "\033[32m"  # GREEN
    WARNING = "\033[33m" # Yellow
    ERROR = "\033[31m"  #  Red
    CRITICAL = "\033[41m"  # Red Background

    SUCCESS = "\033[92m"  # Bright GREEN
    FAIL = "\033[91m"  # Bright Red
    WHITE = "\033[37m"  # Bright WHITE
    CYAN = "\033[36m"  # CYAN

    ENDC = "\033[0m"  # END


class ColoredFormatter(logging.Formatter):
    """Custom formatter to add colors to log messages."""

    def format(self, record):
        log_format_colors = {
            Log_Levels.HEADER: LogColors.HEADER,
            Log_Levels.SUCCESS: LogColors.SUCCESS,
            Log_Levels.FAIL: LogColors.FAIL,
            Log_Levels.INFO: LogColors.INFO,
            Log_Levels.DEBUG: LogColors.DEBUG,
            Log_Levels.WARNING: LogColors.WARNING,
            logging.ERROR: LogColors.ERROR,
            Log_Levels.CRITICAL: LogColors.CRITICAL
        }

        if record.levelno == Log_Levels.HEADER:
            date_str = f"{LogColors.HEADER}{self.formatTime(record)}{LogColors.ENDC}"
            record.msg = f"{LogColors.HEADER}{record.msg}{LogColors.ENDC}"
            return f"{date_str} {record.msg}"

        date_str = f"{log_format_colors[record.levelno]}{self.formatTime(record)}{LogColors.ENDC}"
        record.levelname = f"{log_format_colors[record.levelno]}{record.levelname}{LogColors.ENDC}"
        record.msg = f"{log_format_colors[record.levelno]}{record.msg}{LogColors.ENDC}"
        return f"{date_str} - {record.levelname} - {record.msg}"

class LogMessages:
    """."""
    def __init__(self, logger):
        self.logger = logger

    def info(self, message):
        self.logger.info(message)

    def header(self, message):
        self.logger.log(Log_Levels.HEADER, message)

    def success(self, message):
        self.logger.log(Log_Levels.SUCCESS, message)

    def fail(self, message):
        self.logger.log(Log_Levels.FAIL, message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
