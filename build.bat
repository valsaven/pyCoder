pip3 install pyinstaller

if exist .\dist rmdir .\dist /q /s

pyinstaller --onefile main.py

copy .\th06r.ico .\dist\

xcopy /E /I .\Bin .\dist\Bin

mkdir .\dist\in
mkdir .\dist\out
