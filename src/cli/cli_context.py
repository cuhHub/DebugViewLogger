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
import click
from dataclasses import dataclass
from typing import Callable
from functools import wraps

from debug_view_logger import DebugViewLogger

# // Main
def pass_context(function: Callable):
    """
    Decorator to pass CLI context to functions.

    Args:
        function (Callable): The function to decorate.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs, context = get_context())
    
    return wrapper

@dataclass
class CLIContext:
    """
    Context object for the CLI.
    """

    debug_view_logger: DebugViewLogger

def setup_context(context: click.Context, debug_view_logger: DebugViewLogger):
    """
    Sets up the click context.

    Args:
        context (click.Context): The click context.
        debug_view_logger (DebugViewLogger): The debug view logger to add to context.
    """

    context.ensure_object(dict)

    context.obj["context"] = CLIContext(
        debug_view_logger = debug_view_logger
    )
    
def get_context() -> CLIContext:
    """
    Returns the CLI context.

    Returns:
        CLIContext: The CLI context.
    """

    return click.get_current_context().obj["context"]