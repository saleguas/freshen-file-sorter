rmdir /s /q "dist"
mkdir dist
ROBOCOPY "src/scripts/" "dist" *.py
mkdir "dist/config"
ROBOCOPY "src/config/" "dist/config" *.yml