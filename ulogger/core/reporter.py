"""Reporter Class."""
from core import Log_Levels
from core.console_logger import ConsoleLogger
from core.file_logger import FileLogger
import logging


class Reporter:
    """."""
    _logger_instance = None  # Singleton instance

    def __new__(cls):
        if cls._logger_instance is None:
            # Initialize logger only once
            cls._logger_instance = super(Reporter, cls).__new__(cls)
        return cls._logger_instance

    def __init__(self):
        if not hasattr(self, "reporter"):
            logging.addLevelName(Log_Levels.HEADER, "HEADER")
            logging.addLevelName(Log_Levels.SUCCESS, "SUCCESS")
            logging.addLevelName(Log_Levels.FAIL, "FAIL")

            self.reporter = logging.getLogger("reporter")

            # Add handlers to the logger

            self.print = ConsoleLogger()
            self.save = FileLogger()
