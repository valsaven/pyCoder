@echo off

echo(=== Check if 'dist' directory exists and remove it... ===)
if exist .\dist rmdir .\dist /q /s

echo(=== Compile main.py into a standalone executable... ===)
pyinstaller --onefile main.py

echo(=== Copy the icon to the 'dist' directory... ===)
copy .\th06r.ico .\dist\

echo(=== Copy the contents of the 'Bin' folder to 'dist\Bin'... ===)
xcopy /E /I .\Bin .\dist\Bin

echo(=== Create 'in' and 'out' directories inside 'dist' if they don't exist... ===)
if not exist .\dist\in mkdir .\dist\in
if not exist .\dist\out mkdir .\dist\out

echo(=== Remove main.spec file... ===)
del main.spec

echo(=== Completed! ===)
