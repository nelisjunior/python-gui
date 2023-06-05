@echo off

set /p user_name=Digite o nome desejado para o arquivo httpd.conf: 
set "dir_path=D:\localhost\Apache24\conf"

echo.
echo Listando arquivos no diretório %dir_path%:
echo.

rem Mudar para o diretório especificado
cd /d "%dir_path%"

rem Listar os arquivos no diretório com índices
setlocal enabledelayedexpansion
set "index=1"
for %%F in (*) do (
    echo !index!. %%F
    set /a "index+=1"
)

echo.

set /p chosen_index=Digite o índice do arquivo que deseja renomear: 

rem Verificar se o arquivo correspondente ao índice escolhido existe
setlocal enabledelayedexpansion
set "current_index=1"
for %%F in (*) do (
    if "!current_index!"=="%chosen_index%" (
        ren "%%F" "%user_name%"
        echo Arquivo %%F renomeado para %user_name% com sucesso!
    )
    set /a "current_index+=1"
)

endlocal

pause
