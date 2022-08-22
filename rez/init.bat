@echo off

set rez_dir=Z:\path\to\rez

set REZ_CONFIG_FILE=%rez_dir%\config\rezconfig.py

set REZ_PACKAGES_PATH=~/packages;%rez_dir%\packages\int;%rez_dir%\packages\ext;%rez_dir%\packages\python

if not exist "C:\rez_cache" mkdir C:\rez_cache

set PATH=%rez_dir%\win\Scripts\rez;%PATH%
