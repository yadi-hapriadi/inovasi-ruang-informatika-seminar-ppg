@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>&1
if %errorlevel%==0 goto usepy
where python >nul 2>&1
if %errorlevel%==0 goto usepython
echo Python 3 belum ditemukan.
echo Pasang Python 3 dari https://www.python.org/downloads/ lalu jalankan file ini kembali.
echo Saat pemasangan, aktifkan pilihan Add Python to PATH.
pause
exit /b 1
:usepy
echo Menjalankan Ruang Informatika SMA di localhost...
py -3 start_localhost.py
if errorlevel 1 pause
goto end
:usepython
echo Menjalankan Ruang Informatika SMA di localhost...
python start_localhost.py
if errorlevel 1 pause
:end
endlocal
