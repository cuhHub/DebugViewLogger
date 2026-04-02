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

from .cli_context import (
    setup_context,
    pass_context,
    CLIContext
)

from debug_view_logger import DebugViewLogger
from logger import logger, LOG_DIR
from shared import __version__

# // Main
@click.group()
@click.version_option(__version__, "-v")
@click.help_option("--help", "-h")
@click.pass_context
def cli(context: click.Context):
    """
    A tool for capturing and writing DebugView logs to a file.
    """
    
    logger.info("DebugViewLogger - A tool for capturing and writing DebugView logs to a file.")
    setup_context(context, DebugViewLogger())

@cli.command()
@pass_context
def start(context: CLIContext):
    """
    Starts capturing logs.
    """
    
    logger.info(f"Logs will be written to {LOG_DIR}.")
    logger.info("Use CTRL + C to terminate.")

    context.debug_view_logger.start()