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
import subprocess
from pathlib import Path
from abc import abstractmethod, ABC

from log import logger
from shared import APP_PATH

# // Main
class DebugViewCapture(ABC):
    """
    Captures DebugView logs.
    """
    
    DEBUG_VIEW_CONSOLE_EXECUTABLE_NAME = "_dbg_view_console.exe"
    
    DEBUG_VIEW_CONSOLE_EXECUTABLE_PATHS = (
        Path(__file__).parent / DEBUG_VIEW_CONSOLE_EXECUTABLE_NAME, # non-pyinstaller context
        APP_PATH / DEBUG_VIEW_CONSOLE_EXECUTABLE_NAME # fallback, pyinstaller context
    )
    
    def __init__(self):
        """
        Initializes DebugViewCapture instances.
        """

        self.executable_path = self.get_executable_path()
        self.process: subprocess.Popen = None
        
    def get_executable_path(self) -> Path:
        """
        Returns the debug view console executable path.

        Raises:
            FileNotFoundError: If the executable is not found.
            
        Returns:
            Path: The executable path.
        """
        
        for path in self.DEBUG_VIEW_CONSOLE_EXECUTABLE_PATHS:
            if path.exists():
                return path
        
        raise FileNotFoundError("DebugView console executable not found.")
    
    @abstractmethod
    def on_log(self, log: str):
        """
        Called when a log is captured.

        Args:
            log (str): The captured log.
        """
        
        pass
    
    def _handle_log(self, log: str):
        """
        Handles a log.
        
        Args:
            log (str): The log to handle.
        """
        
        self.on_log(log.rstrip("\r\n"))
    
    def _get_command_line_arguments(self) -> tuple[str]:
        """
        Returns the command line arguments for the process.
        
        Returns:
            tuple[str]: The command line arguments.
        """
        
        return (
            "-c", # console
            "-l", # prefix line number
            "-s", # prefix system time
            "-p", # prefix process id
            "-n", # prefix process name,
            "-t" # tab-separated output
        )
    
    def start(self):
        """
        Starts capturing logs.
        
        Raises:
            FileNotFoundError: If the executable is not found.
            AttributeError: If the process is already running.
        """
        
        if self.process is not None:
            raise AttributeError("Process is already running.")
        
        command_line = [self.executable_path, *self._get_command_line_arguments()]
        
        logger.info(f"DebugViewCapture: Starting process using: {command_line}")
        
        self.process = subprocess.Popen(
            command_line,
            stdout = subprocess.PIPE,
            stderr = subprocess.STDOUT,
            text = True,
            encoding = "utf-8",
            errors = "replace"
        )
        
        logger.info(f"DebugViewCapture: Process started, PID: {self.process.pid}")
        
        for line in self.process.stdout:
            self._handle_log(line)
            
    def stop(self):
        """
        Stops capturing logs.
        
        Raises:
            AttributeError: If the process is not running.
        """
        
        if self.process is None:
            raise AttributeError("Process is not running.")
        
        self.process.terminate()
        logger.info("DebugViewCapture: Process terminated")