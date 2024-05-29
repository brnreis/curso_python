# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/


# OBS.: sempre lembre-se de criar um .env-example
# usar gitignore no arquivo .env que contem as informações sensíveis


import os

from dotenv import load_dotenv  # type: ignore
load_dotenv()

# print(os.environ)
print(os.getenv('BD_PASSWORD'))
