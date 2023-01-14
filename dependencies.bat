@echo off
chcp 65001
setlocal

python -c "import sys; print(sys.version)" 2>nul
if %errorlevel% neq 0 (
    echo Python não está instalado. Por favor, instale antes de continuar.
    start https://www.python.org/downloads/
    exit /b
)

echo Python está instalado. Instalando dependências...
pip install numpy pandas

echo Dependências instaladas. Executando script...
python meu_script.py

endlocal
