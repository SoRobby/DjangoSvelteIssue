import logging
import os


class ColorizeFilter(logging.Filter):
    """
    A custom logging filter that applies different ANSI color codes to messages
    based on their logging level.

    Attributes:
        COLORS (dict): A mapping of log level names to their respective ANSI color codes.
        RESET (str): ANSI escape code to reset the color to terminal's default.
    """

    # Define a dictionary mapping logging level names to ANSI color codes
    COLORS = {
        "DEBUG": "\033[96m",        # Cyan
        "INFO": "\033[94m",         # Blue
        "WARNING": "\033[93m",      # Yellow
        "ERROR": "\033[91m",        # Light red
        "CRITICAL": "\033[31m",     # Dark red
    }

    # ANSI escape code to reset the color to terminal's default
    RESET = "\033[0m"

    def filter(self, record):
        """
        Modify the record's message to prepend it with an ANSI color code based
        on the record's levelname. If the levelname is not found in the COLORS
        dictionary, the RESET color is used as a default.

        Args:
            record (logging.LogRecord): The log record to be processed.

        Returns:
            bool: True always, allowing the log message to be processed by
                  further filters/handlers.
        """
        levelname = record.levelname
        record.msg = f"{self.COLORS.get(levelname, self.RESET)}{record.msg}{self.RESET}"
        return True
