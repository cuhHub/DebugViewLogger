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
from pathlib import Path

from .cli_context import (
    setup_context,
    pass_context,
    CLIContext
)

from debug_view_logger import DebugViewLogger
import log
from shared import __version__

# // Main
@click.group()
@click.version_option(__version__, "-v")
@click.help_option("--help", "-h")
@click.option(
    "--log-dir", "-l",
    type = click.Path(exists = False, file_okay = False, dir_okay = True, writable = True, path_type = Path),
    required = False,
    help = "Overrides what directory to write logs to."
)
@click.option(
    "--max-log-size", "-m",
    type = click.INT,
    required = False,
    help = "Overrides what the maximum log size in MB is."
)
@click.option(
    "--max-logs", "-n",
    type = click.INT,
    required = False,
    help = "Overrides what the maximum number of log files is."
)
@click.pass_context
def cli(
    context: click.Context,
    log_dir: Path | None,
    max_log_size: int | None,
    max_logs: int | None
):
    """
    A tool for capturing and writing DebugView logs to a file.
    """
    
    if log_dir is not None:
        log.log_dir = log_dir
        
    if max_log_size is not None:
        log.max_log_size_mb = max_log_size
    
    if max_logs is not None:
        log.max_logs = max_logs
    
    log.setup_logger(log.logger)
    
    click.echo("-------------------------")
    click.echo("DebugViewLogger - A tool for capturing and writing DebugView logs to a file.")
    click.echo("https://github.com/cuhHub/DebugViewLogger")
    click.echo(f"Settings: {max_log_size}MB logs, max {max_logs} log files, log to {log_dir}")
    click.echo("-------------------------")

    setup_context(context, DebugViewLogger())

@cli.command()
@pass_context
def start(context: CLIContext):
    """
    Starts capturing and writing logs.
    """
    
    click.echo(f"Logs will be written to {log.log_dir}.")
    click.echo("Use CTRL + C to terminate.")

    context.debug_view_logger.start()