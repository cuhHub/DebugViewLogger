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
from logger import logger
from libs.capture import DebugViewCapture

# // Main
__all__ = ["DebugViewLogger"]

class DebugViewLogger(DebugViewCapture):
    """
    Logs captured DebugView logs.
    """
    
    def __init__(self):
        """
        Initializes DebugViewLogger instances.
        """

        super().__init__()
        
    def on_log(self, log: str):
        """
        Called when a log is captured.

        Args:
            log (str): The captured log.
        """
    
        logger.info(f"DebugView Log: {log}")