# Resposta atividade

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site "http://www.pudim.com.br" não está disponivel no momento :(\033[m')
else:
    print('\033[0;32mO site "http://www.pudim.com.br" está funcionando corretamente :)\033[m')

# Minha resposta pesquisando

'''

import requests

try:
    site = requests.get('http://www.pudim.com.br')
except:
    print('\033[0;31mO site "http://www.pudim.com.br" não está disponivel no momento :(\033[m')
else:
    print('\033[0;32mO site "http://www.pudim.com.br" está funcionando corretamente :)\033[m')
    
'''

