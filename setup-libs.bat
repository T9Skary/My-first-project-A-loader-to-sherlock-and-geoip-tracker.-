@echo off
echo Setting up libraries for the OSINT Tools...
echo Installing Python dependencies...
cd %USERPROFILE%\Python\pythoncore-3.14-64\Scripts
python3 -m pip install sherlock
cd sherlock
python3 -m pip install .
python3 -m pip install -r requirements.txt
cd ..
python3 -m pip install phoneinfoga
cd phoneinfoga
python3 -m pip install .
python3 -m pip install -r requirements.txt
cd ..
python3 -m pip install holehe
cd holehe
python3 -m pip install .
python3 -m pip install -r requirements.txt
cd ..
echo All installed, test the osint.exe
echo Source code on https://github.com/T9Skary/My-first-project-A-loader-to-sherlock-and-geoip-tracker.-     file: osint.c !
pause