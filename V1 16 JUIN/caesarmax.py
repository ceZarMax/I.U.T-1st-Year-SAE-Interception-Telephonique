#!/usr/bin/python3
#pip3 install python-nmap

import nmap
sc = nmap.PortScanner()

print("""  _____                           __  __                      _   _           
  / ____|                         |  \/  |                    | | (_)           
 | |     __ _  ___  ___  __ _ _ __| \  / | __ ___  _____ _ __ | |_ _ _   _ ___  
 | |    / _` |/ _ \/ __|/ _` | '__| |\/| |/ _` \ \/ / _ \ '_ \| __| | | | / __| 
 | |___| (_| |  __/\__ \ (_| | |  | |  | | (_| |>  <  __/ | | | |_| | |_| \__ \ 
  \_____\__,_|\___||___/\__,_|_|  |_|  |_|\__,_/_/\_\___|_| |_|\__|_|\__,_|___/ 
                                                                                \n
                                                                                \n """)

def main():

	n = input("1- Network Scanner\n2- Vulnerabilities Detection\n3- Exploit\n\nEntrez un nombre : ")
	if n == '1':
		nmap()


def nmap():
	print("**********Bienvenue sur le Network Scanner de CaesarMaxentius**********")
	print("***********************************************************************")
	ip = input("\nPlease, enter the IP adress : ")
	if ip != sc.ip():
		print("L'adresse IP n'est pas valide, veuillez recommencer")
		return ip	
	else :
		pass
	sc.scan(ip , '1-1024')
	print(sc.scaninfo())
	print(sc[ip]['tcp'].keys()) 

if __name__ == "__main__":
	main()