@echo off

:: ----------------------------
:: Set up environment variables
:: ----------------------------
:setup_env_variables
:: Change this variable to your local SCADE installation path if required
set SCADE_INSTALL=C:\Program Files\ANSYS Inc\v252\SCADE
set PYTHONPATH=%SCADE_INSTALL%\SCADE A661\PythonLib;%SCADE_INSTALL%\SCADE\APIs\Python\lib
set VENV=.venv
echo Using SCADE installation: %SCADE_INSTALL%
if not exist "%SCADE_INSTALL%\" (echo Invalid SCADE installation path, exiting && goto :end)
echo Using Python Path: %PYTHONPATH%
echo Using Python venv: %VENV%

:: -------------------------------
:: Build the binary DF if required
:: -------------------------------
:build_df
if not exist "graphics\DF\UA_1.bin" (
    echo Building the binary DF, this may take a while...
    "%SCADE_INSTALL%\SCADE A661\DFGEN68\bin\dfgen.exe" ^
        -n "%SCADE_INSTALL%\SCADE Display\config\a661_description\a661.xml" ^
        -outdir "graphics\DF" -o "UA_1" "graphics\UADF.sgfx"
    if ERRORLEVEL 1 (echo Failed to build binary DF, exiting && goto :end)
)

:: ---------------------------------
:: Set up Python virtual environment
:: ---------------------------------
:setup_venv
if not exist %VENV% (
    echo Creating Python virtual environment, this may take a while...
    "%SCADE_INSTALL%\contrib\Python310\python.exe" -m venv %VENV%
    call .\%VENV%\Scripts\activate.bat
) else (
    echo Activating Python virtual environment: %VENV%
    call .\%VENV%\Scripts\activate.bat
)

:: -------------------------
:: Start the Python UA logic
:: -------------------------
:start_ua
echo Starting UA prototype...
python "logic\UA.py"

:end