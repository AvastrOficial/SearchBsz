# Importar colorama y sus estilos de color
from colorama import init, Fore, Style

# Inicializar colorama
init()

banner = f"""{Fore.GREEN}
  ____                      _     ____          
 / ___|  ___  __ _ _ __ ___| |__ | __ ) ___ ____  
 \___ \ / _ \/ _` | '__/ __| '_ \|  _ \/ __|_  /
  ___) |  __/ (_| | | | (__| | | | |_) \__ \/ / 
 |____/ \___|\__,_|_|  \___|_| |_|____/|___/___|
 
  {Fore.RED} By {Fore.WHITE} @AvaStrOficial
 {Fore.RED}Version : {Fore.WHITE} 0.0.0
{Fore.GREEN}
"""

from bs4 import BeautifulSoup as htmlparser
import requests


def lookup(phone_number):
    http = requests.get(f"https://free-lookup.net/{phone_number}")
    html = htmlparser(http.text, "html.parser")
    infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")

    return {k.text.strip(): infos[i+1].text.strip() if infos[i+1].text.strip() else "No information" for i, k in enumerate(infos) if not i % 2}


def main():
    print(banner) 
    while True:
        try:
            phone_number = input("Escribe el Numero para buscarlo : ").strip().replace("-", "").replace(" ", "").replace("+", "")
        except KeyboardInterrupt:
            return

        try:
            infos = lookup(phone_number)
        except AttributeError:
            print("Error: Invalid phone number\n")
            continue

        [print(f"{info}: {infos[info]}") for info in infos]
        print("\n")

if __name__ == "__main__":
    main()
