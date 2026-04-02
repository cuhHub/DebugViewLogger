# DebugViewLogger

## 📚 | Overview
A tool to capture and write DebugView logs to files. Useful for saving logs emitted from Stormworks addons/mods via `debug.log`, etc.

This will only work on Windows as DebugView logs are a Windows-native thing.

## 🔗 | Links
- GitHub: https://github.com/cuhHub/DebugViewLogger.

## ⚙️ | Installing
### GitHub Releases
- Go to latest release.
- Download the app ZIP.
- Extract it to a directory of your choosing.
- Open CMD in the directory, and run `DebugViewLogger --help`.
- *Optional: Add the directory to path so you can run `DebugViewLogger` anywhere.*

### From Source
- `git clone` this repo.
- Run `pip install -r requirements.txt` to install required Python packages.
- `cd` into `src`, and run `py main.py --help` to see all commands.

⚠️ | Requires Python 3.13+. Untested on earlier versions!

## ❔ | Usage
⚠️ | This is a console application, not a GUI. Double-clicking and running it therefore will not work - you must use it via a terminal!

- Run `DebugViewLogger --help` to see all commands.
- Run `DebugViewLogger start` to start capturing logs.

## ⚙️ | Advanced Usage
You can configure a few settings too using the following arguments that ***must*** be before `start`:
- Set custom log directory: `DebugViewLogger --log-dir "(path)" start`
- Set custom log size (in MB): `DebugViewLogger --max-log-size 500 start`
- Set max number of log files: `DebugViewLogger --max-logs 5 start`

Example: Log to "../my_logs", max of 10 log files, and each log file can, at max, be 2500 MB.
```
DebugViewLogger --log-dir "../my_logs" --max-log-size 2500 --max-logs 10 start

OR

DebugViewLogger -l "../my_logs" -m 2500 -n 10 start
```

## ✨ | Credit
- [**DebugView++**](https://github.com/CobaltFusion/DebugViewPP): Console version of this app is used for capturing logs.
- **Cuh4** ([GitHub](https://github.com/Cuh4))