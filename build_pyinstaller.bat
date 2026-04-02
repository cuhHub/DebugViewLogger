@ECHO OFF

:: Clean-state
set dist_path=dist\DebugViewLogger
rmdir %dist_path% /S /Q

:: Build for exe distribution
pip install pyinstaller --upgrade

pyinstaller ^
    -n DebugViewLogger ^
    --icon "imgs/icon-48x48.ico" ^
    src\main.py

:: Copy requirements
copy "README.md" %dist_path%
copy "LICENSE" %dist_path%
copy "src\libs\capture\_dbg_view_console.exe" %dist_path%

:: Package into .zip
powershell Compress-Archive -Path "dist\DebugViewLogger" -DestinationPath "dist\DebugViewLogger.zip" -Force