@echo off
rem ---------------------------------------------------------------------------
rem  Build Submission Helper into dist\SubmissionHelper
rem
rem    SubmissionHelper.exe      GUI, no console window
rem    SubmissionHelper-cli.exe  console version for headless / command line
rem
rem  Needs uv (https://docs.astral.sh/uv/). Creates .venv with Python 3.10 if
rem  it doesn't exist, installs requirements + PyInstaller, builds, and copies
rem  the runtime folders (oiio, ocio, ffmpeg) and install.json / default.json
rem  next to the exe.
rem ---------------------------------------------------------------------------
setlocal
cd /d "%~dp0"

set "DIST=dist\SubmissionHelper"
set "PY=.venv\Scripts\python.exe"

where uv >nul 2>nul
if errorlevel 1 (
    echo ERROR: uv not found. Install it from https://docs.astral.sh/uv/
    goto :fail
)

if not exist "%PY%" (
    echo Creating .venv with Python 3.10 ...
    uv venv --python 3.10 || goto :fail
)

echo Installing requirements and PyInstaller ...
uv pip install --python "%PY%" -r requirements.txt pyinstaller || goto :fail

echo Building ...
"%PY%" -m PyInstaller --noconfirm --clean submission_helper.spec || goto :fail

echo Copying runtime files next to the exe ...
for %%D in (oiio ocio ffmpeg) do (
    if exist "%%D\" (
        robocopy "%%D" "%DIST%\%%D" /E /NFL /NDL /NJH /NJS /NP >nul
        if errorlevel 8 goto :fail
    )
)
for %%F in (install.json default.json) do (
    if exist "%%F" copy /Y "%%F" "%DIST%\" >nul
)

echo.
echo Done:
echo   %DIST%\SubmissionHelper.exe      (GUI)
echo   %DIST%\SubmissionHelper-cli.exe  (command line)
if exist install.json echo NOTE: install.json was copied; check it for API keys before sharing the build.
endlocal
exit /b 0

:fail
echo.
echo BUILD FAILED
endlocal
exit /b 1
