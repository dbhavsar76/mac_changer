import subprocess
import optparse 
import re
import sys
import time 
import os

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(7. /100)
slowprint("\033[1;31m \033[91m [!] Starting MAC Changer...")
time.sleep(3)
os.system('clear')
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0. /100)
slowprint(''' \033[1;31m \033[91m
                             _                                 
 _ __ ___   __ _  ___    ___| |__   __ _ _ __   __ _  ___ _ __ 
| '_ ` _ \ / _` |/ __|  / __| '_ \ / _` | '_ \ / _` |/ _ \ '__|
| | | | | | (_| | (__  | (__| | | | (_| | | | | (_| |  __/ |   
|_| |_| |_|\__,_|\___|  \___|_| |_|\__,_|_| |_|\__, |\___|_|   
                                               |___/           
\033[97m ''')

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(3. /100)
slowprint("\t\t \033[93m Coded By : Parshwa Bhavsar \033[97m")


def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface to change it's MAC Address")
	parser.add_option("-m","--mac",dest="new_mac",help="New MAC Address")
	(options,arguments) = parser.parse_args()
	if not options.interface:
		 parser.error("[-] Please specify an interface, use --help for more info.")#code to handle error
	elif not options.new_mac:
		  parser.error("[-] Please specify a new mac, use --help for more info.")#code to handle error
	return options


def change_mac(interface,new_mac):
	print("\033[96m [+] Capturing Old MAC Address...")
	print("\033[96m [+] Changing MAC Addres for " + interface +"...")
	print("\033[96m [+] Holaaaa !!!!!")
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	mac_addr_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	if mac_addr_search_result:
		return mac_addr_search_result.group(0)
	else:
		print("[-] Could not find MAC Address")


options = get_arguments()
change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)
print("\033[92m [+] MAC Address is successfully changed to : \033[97m" + current_mac)
