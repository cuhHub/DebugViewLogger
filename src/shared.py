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
import sys
from pathlib import Path

# // Main
def get_app_path(is_pyinstaller_context: bool) -> Path:
    """
    Returns the application path.

    Args:
        is_pyinstaller_context (bool): Whether the application is running in a PyInstaller context.

    Returns:
        Path: The application path.
    """
    
    if is_pyinstaller_context:
        return Path(sys.executable).parent
    
    return Path(__file__).parent

IS_PYINSTALLER_CONTEXT = getattr(sys, "frozen", False)

APP_PATH = get_app_path(IS_PYINSTALLER_CONTEXT)
DATA_PATH = APP_PATH / "data"
DATA_PATH.mkdir(exist_ok = True)

__version__ = "1.0.0"