@echo off
chcp 65001 >nul
echo ========================================
echo Czech DOCX Anonymizer
echo ========================================
echo.

python "Czech DOCX Anonymizer3.py" %1

if errorlevel 1 (
    echo.
    echo CHYBA při zpracování!
    pause
)
