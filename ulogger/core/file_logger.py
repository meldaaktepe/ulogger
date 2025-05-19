"""."""
from core import LogMessages
import logging

class FileLogger(LogMessages):
    """."""
    def __init__(self):
        self.logger = logging.getLogger("reporter.file_logger")
        self.logger.setLevel(logging.DEBUG)

        # Create file handler
        if not self.logger.handlers:
            self.file_handler = logging.FileHandler("app.log")
        self.file_handler.setLevel(logging.DEBUG)

        # formatter = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        self.file_handler.setFormatter(formatter)

        self.logger.addHandler(self.file_handler)

        super().__init__(self.logger)
