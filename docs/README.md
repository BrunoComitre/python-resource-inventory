# Python

***

## 01
Se você estiver no Windows e usando o PowerShell, execute os seguintes comandos para instalar o Oh My Posh:

PS C:\> Install-Module oh-my-posh -Scope CurrentUser
PS C:\> Add-Content $PROFILE "`nSet-PoshPrompt -Theme tonybaloney"

## 02

python3 -m pip inst










all --user pylint black poetry pipenv bandit mypy flake8

Depois pegar o gist: Settings_user.md e atualizar o vscode (copiar e colar)

## 03

Adicionar ao ./vscode/settings.json, no final do arquivo essas linhas:

    "python.linting.enabled": true,
    "python.linting.banditEnabled": true,
    "python.linting.pylintEnabled": true,
    "python.terminal.activateEnvironment": false,
    "python.linting.pycodestyleEnabled": true,
    "python.formatting.provider": "black",
    "python.linting.lintOnSave": true

## 04

Fazer esse tutorial: https://realpython.com/advanced-visual-studio-code-python/#setting-format-and-lint-on-save

## 05

Dar F1 e depois: Settings Sync: Show Synced Data

## 06

APRENDER A CONFIGURAR O pytest.ini, VER NA NET

## 07

APRENDR SOBRE: https://realpython.com/pypi-publish-python-package/#building-your-package

setup.py

## 08

Adicionar ao ./vscode

tasks.json que se encontra no gist

## 09

Aprender sobre tox: https://tox.wiki/en/latest/

NO POETRY SEMPRE ADICIONAR E CRIAR O tox.ini

## 10

https://marketplace.visualstudio.com/items?itemName=spmeesseman.vscode-taskexplorer

# 11
https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker
https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
https://marketplace.visualstudio.com/items?itemName=tonybaloney.vscode-pets