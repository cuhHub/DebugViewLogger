"""
----------------------------------------------
DebugViewLogger - A tool for capturing and writing DebugView logs to a file.
https://github.com/cuhHub/DebugViewLogger
----------------------------------------------

Copyright (C) 2026 cuhHub

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# // Imports
import logging
from logging.handlers import RotatingFileHandler

from shared import DATA_PATH

# // Main
LOG_DIR = DATA_PATH / "logs"
LOG_DIR.mkdir(exist_ok = True)

MAX_LOG_SIZE_GB = 10
MAX_LOGS = 5

def setup_logger(logger: logging.Logger):
    """
    Sets up the provided logger.

    Args:
        logger (logging.Logger): The logger to set up.
    """
    
    logger.setLevel(logging.DEBUG)

    log_path = LOG_DIR / f"{logger.name}.log"

    file_handler = RotatingFileHandler(
        log_path,
        maxBytes = MAX_LOG_SIZE_GB * 1024 * 1024 * 1024,
        backupCount = MAX_LOGS
    )
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

logger = logging.getLogger("DebugViewLogger")
setup_logger(logger)