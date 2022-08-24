@echo off

set python39="C:\Program Files\Python39\python.exe"
REM check for python 3.9
if not exist %python39% (
    echo Missing python-3.9 at %python39%
    pause
    EXIT /B
)

REM check if rez is already installed
if exist "C:\rez\Scripts\rez\.rez_production_install" (
    echo Rez is already installed!
    pause
    EXIT /B
)

set install_script="Z:\path\to\rez\config\rez-src-2.104.9\install.py"
echo Installing rez locally, this can take a while...
%python39% %install_script% -v "C:\rez"

pause
