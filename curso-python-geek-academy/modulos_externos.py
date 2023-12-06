"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip, - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo:

pip install nome-do-modulo

# Instalando o pacote colorama

pip install colorama

# Utilizando o pacote instalando

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
"""
import pydf
from colorama import init, Fore

pdf = pydf.generate_pdf('<h1>Geek University<h1><br><strong>Programação em Python: Essencial</strong>')

with open('teste_doc.pdf', 'wb', encoding='utf-8') as f:
    f.write(pdf)