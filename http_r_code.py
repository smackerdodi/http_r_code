import sys
import colorama
import requests
from colorama import Fore, Style
from requests.exceptions import ConnectionError
sublist=sys.argv[1]
outlist=sys.argv[2]
redlist=sys.argv[3]
deniedlist=sys.argv[4]
subfile=open(sublist, "r")
outfile=open(outlist, "a")
redfile=open(redlist, "a")
deniedfile=open(deniedlist, "a")
for sub in subfile:
	try:
		subd=sub.strip()
		subd2="http://" + subd		
		res = requests.head(subd2, timeout=1)
		if str(res.status_code)[0] == "3":
			res3=subd2 + " : " + str(res.status_code) + " >> " + res.headers['location']
			redfile.write(res3 +"\n")
			print(Style.BRIGHT + Fore.WHITE + (subd2) + " : " + Fore.BLUE + str(res.status_code) + Fore.GREEN + " >> " + Fore.YELLOW + (res.headers['location']))
		elif str(res.status_code)[0] == "2":
			print(Style.BRIGHT + Fore.WHITE + (subd2) + " : " + Fore.GREEN + str(res.status_code))
			res2=subd2 + " : " + str(res.status_code)
			outfile.write(res2 +"\n") 
		elif str(res.status_code)[0] == "4":
			print(Style.BRIGHT + Fore.WHITE + (subd2) + " : " + Fore.RED + str(res.status_code))
			res4=subd2 + " : " + str(res.status_code)
			deniedfile.write(res4 +"\n") 
		else :
			print(Style.BRIGHT + Fore.WHITE + (subd2) + " : " + Fore.BLUE + str(res.status_code))
	except :    
   		print(Style.BRIGHT + Fore.WHITE + (subd2) + " : " + Fore.RED + (' Unreachable'))
subfile.close()
