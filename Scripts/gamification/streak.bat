@echo off
REM Streak Fix Tool for Windows
REM Makes it easy to update streaks accounting for scheduled study days

cd /d "%~dp0"
python streak_fix.py
pause
