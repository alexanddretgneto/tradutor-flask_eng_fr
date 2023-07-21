# import subprocess
# import sys

# def verificar_codigo_arquivo(caminho_arquivo):
#     try:
#         resultado = subprocess.run(['pylint', caminho_arquivo], capture_output=True, text=True)
#         saida = resultado.stdout.strip()
#         print(saida)
#         if resultado.returncode != 0:
#             sys.exit(1)
#     except FileNotFoundError:
#         print("Erro: O comando 'pylint' não foi encontrado. Certifique-se de que o Pylint esteja instalado.")
#         sys.exit(1)

# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print("Erro: Forneça o caminho para o arquivo a ser verificado.")
#         sys.exit(1)
    
#     caminho_arquivo = sys.argv[1]
#     verificar_codigo_arquivo(caminho_arquivo)

#!/usr/bin/env python

import subprocess
import sys

def verificar_codigo_arquivo(caminho_arquivo):
    try:
        resultado = subprocess.run(['pylint', caminho_arquivo], capture_output=True, text=True)
        saida = resultado.stdout.strip()
        print(saida)
        if resultado.returncode != 0:
            sys.exit(1)
    except FileNotFoundError:
        print("Erro: O comando 'pylint' não foi encontrado. Certifique-se de que o Pylint esteja instalado.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Erro: Forneça o caminho para o arquivo a ser verificado.")
        sys.exit(1)
    
    caminho_arquivo = sys.argv[1]
    verificar_codigo_arquivo(caminho_arquivo)

if __name__ == '__main__':
    main()