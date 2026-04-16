from urllib import request
import urllib

try:
    site = request.urlopen("https://www.roblox.com/pt/home")
except urllib.error.URLError:
    print("O site não está acessível no momento.")
else:
    print("Consegui acessar o site do Roblox com sucesso!")
    print(site.read())