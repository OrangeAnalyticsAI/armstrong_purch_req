@echo off
echo Checking Python installation...

python --version > nul 2>&1
if errorlevel 1 (
    echo Python not found. Opening Microsoft Store to install Python...
    start ms-windows-store://pdp/?ProductId=9PJPW5LDXLZ5
    echo Please run this installer again after installing Python
    pause
    exit
)

echo Creating app directory...
mkdir "%USERPROFILE%\Armstrong_App" 2> nul
cd "%USERPROFILE%\Armstrong_App"

echo Creating directories...
mkdir "static" 2> nul
mkdir "templates" 2> nul

echo Copying app files...
copy "O:\Program Files\ArmstrongApp\app.py" "app.py"
copy "O:\Program Files\ArmstrongApp\requirements.txt" "requirements.txt"
copy "O:\Program Files\ArmstrongApp\static\style.css" "static\style.css"
copy "O:\Program Files\ArmstrongApp\templates\index.html" "templates\index.html"

echo Creating run script...
echo @echo off > run_app.bat
echo python -m pip install -r requirements.txt --user >> run_app.bat
echo python app.py >> run_app.bat

echo Creating desktop shortcut...
powershell -Command "& {$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Armstrong Purchase Req.lnk'); $Shortcut.TargetPath = '%USERPROFILE%\Armstrong_App\run_app.bat'; $Shortcut.Save()}"

echo Installation complete!
echo A shortcut has been created on your desktop.
pause 