del /f /s /q dist
rmdir /s /q dist
mkdir dist
ROBOCOPY "src/scripts/" "dist" *.py
mkdir "dist/config"
ROBOCOPY "src/config/" "dist/config" *.yml
7z a -r dist.zip dist/
release-it
pause