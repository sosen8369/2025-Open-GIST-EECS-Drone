@echo off
set "VENV1_NAME=mediapipe (0.10.11)"
echo Create virtual environment %VENV1_NAME%

echo.
python -m venv "%VENV1_NAME%"
call "%VENV1_NAME%"\Scripts\activate.bat

pip install opencv-python==4.9.0.80 numpy==1.26.4 mediapipe==0.10.11 CodingRider keyboard
call "%VENV1_NAME%"\Scripts\deactivate.bat
echo %VENV1_NAME% Completed

echo.
set "VENV2_NAME=tensorflow (2.12.0)"
echo Create virtual environment %VENV2_NAME%.

echo.
python -m venv "%VENV2_NAME%"
call "%VENV2_NAME%"\Scripts\activate.bat

pip install opencv-python==4.9.0.80 numpy==1.23.5 tensorflow==2.12.0 CodingRider keyboard
call "%VENV2_NAME%"\Scripts\deactivate.bat
echo %VENV2_NAME% Completed

echo.
echo All tasks completed
pause