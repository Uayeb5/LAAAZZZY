#coding:utf-8

import os
import time
import sys
import pyfiglet
import colorama
from colorama import Fore, Style

ascii_banner = pyfiglet.figlet_format("LAAAZZZY")
print(ascii_banner)
print("LAAAZZZY V1.0 - A TOOL BY UAYEB5")
print("WARNING ! THIS TOOL IS FOR EDUCATIONAL PURPOSE ONLY !\n")

time.sleep(2)

ip_target = input(Fore.GREEN + "[+] Who is your target (IP address) ?: \n> ")
print(Style.RESET_ALL)

try:
	ip_target = str(ip_target)
except:
	print(Fore.RED + "Incorrect value, please enter an IP address")
	print(Style.RESET_ALL)

allCommands = ("sudo mkdir LAAAZZZY_DUMP && cd LAAAZZZY_DUMP && sudo mkdir NMAP_DUMP && cd NMAP_DUMP && sudo nmap -sC -sV -O -Pn {} -oA nmapscan && cd .. &&  sudo mkdir NIKTO_DUMP && cd NIKTO_DUMP && sudo nikto -host {} -output nikto.txt && cd .. && sudo mkdir GOBUSTER && cd GOBUSTER && sudo gobuster dir -u {}/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster_output.txt")
nmap_scan = ("sudo mkdir NMAP_DUMP && cd NMAP_DUMP && sudo nmap -sC -sV -O {} -oA nmapscan1")
nmap_scan2 = ("sudo mkdir NMAP_DUMP2 && cd NMAP_DUMP2 && sudo nmap -A -Pn {} -oA nmapscan2")
nikto2 = ("sudo mkdir NIKTO_DUMP && cd NIKTO_DUMP && sudo nikto -host {} -output nikto.txt")
nikto3 = ("sudo mkdir NIKTO_DUMP && cd NIKTO_DUMP && sudo nikto -host {} -output nikto.txt")
gobuster = ("sudo mkdir GOBUSTER_DUMP && cd GOBUSTER_DUMP && sudo gobuster dir -u {}/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o GOBUSTER")

print(Fore.GREEN + "[+] What would you like to do ?")
print(Fore.GREEN + "[+] Available choices : complete_scan, nmap, nikto, gobuster, help, exit")
print(Style.RESET_ALL)

program_on = True

while program_on:		
	choixProgramme = input("> ")
	if choixProgramme == "complete_scan":
		os.system(allCommands.format(ip_target, ip_target, ip_target))
		time.sleep(2)
		print(Fore.GREEN + "[+] Your results were saved")
		print(Style.RESET_ALL)

	elif choixProgramme == "nmap":
		os.system(nmap_scan.format(ip_target))
		time.sleep(2)
		print(Fore.GREEN + "[+] Your results were saved")
		print(Style.RESET_ALL)

		choixMenu = input("Would you re-try nmap ? \n> ")
		choixMenu = str(choixMenu)
		if choixMenu == "Yes":
			os.system(nmap_scan2.format(ip_target))
			time.sleep(2)
			print(Fore.GREEN + "[+] Your results were saved")
			print(Style.RESET_ALL)
		elif choixMenu == "Non":
			nikto = input("Would you use nikto ? \n> ")
			if nikto == "Yes":
				os.system(nikto3.format(ip_target))
			elif nikto == "No":
				sys.exit("Bye")
		elif choixMenu == "exit":
				sys.exit("Bye")
		

	elif choixProgramme == "nikto":
		os.system(nikto2.format(ip_target))
		time.sleep(2)
		print(Fore.GREEN + "[+] You results were saved")
		print(Style.RESET_ALL)
		choixMenu = input("What would you do now ? \n ")
		choixMenu = str(choixMenu)
		if choixMenu == "nmap":
			os.system(nmap_scan.format(ip_target))
	elif choixProgramme == "gobuster":		
		os.system(gobuster.format(ip_target))
	elif choixProgramme == "help":
		print(Fore.RED + "[+] You must choose one of theses options : complete_scan, nmap, nikto, gobuster, help, exit")
		print(Style.RESET_ALL)
	elif choixProgramme == "exit":
		sys.exit("Bye...")
	else:
		print("I didn't understand your query, here are your choices : complete_scan, nmap, nikto, help, exit")

	
	


