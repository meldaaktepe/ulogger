"""."""
from core import ColoredFormatter, LogMessages
import logging

class ConsoleLogger(LogMessages):
    """."""
    def __init__(self):
        self.logger = logging.getLogger("reporter.console_logger")
        self.logger.setLevel(logging.DEBUG)

        # Create console handler
        if not self.logger.handlers:
            self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)

        formatter = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")
        self.console_handler.setFormatter(formatter)

        self.logger.addHandler(self.console_handler)

        super().__init__(self.logger)
