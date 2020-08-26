import concurrent.futures
import requests
import threading
import sys
import time
from colorama import Fore, Style
inputfile=sys.argv[1]
outputfile=sys.argv[2]
output=open(outputfile, "a")
with open(inputfile, "r") as f:
	inputurl = [line.rstrip() for line in f]
threadLocal = threading.local()
count = len(inputurl)
print("number of urls = " + str(count))
def get_session():
    if not hasattr(threadLocal, "session"):
        threadLocal.session = requests.Session()
    return threadLocal.session
def check_sub(url):
	try :
		session=get_session()
		res=session.get(url, timeout=1, allow_redirects=False)
		if str(res.status_code)[0] == "3":
			res3=url + " : " + str(res.status_code) + " >> " + res.headers['location']
			print(Style.BRIGHT + Fore.WHITE + (url)+ " : " + Fore.BLUE + str(res.status_code) + Fore.GREEN + " >> " + Fore.YELLOW + (res.headers['location']))
			output.write(res3 +"\n")
		elif str(res.status_code)[0] == "2":
			res2=url + " : " + str(res.status_code) 
			print(Style.BRIGHT + Fore.WHITE + (url)+ " : " + Fore.GREEN + str(res.status_code))
			output.write(res2 +"\n")
		else :
			res4=url + " : " + str(res.status_code)
			print(Style.BRIGHT + Fore.WHITE + (url)+ " : " + Fore.RED + str(res.status_code))
			output.write(res4 +"\n")
	except:
		print(Style.BRIGHT + Fore.WHITE + (url)+ " : " + Fore.RED+ " : is unreachable")
def itterate_url(inputurl):
	url="https://"+inputurl
	check_sub(url)
	
if __name__ == "__main__":
	start_time = time.time()
	with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
       		executor.map(itterate_url, inputurl)
	duration = time.time() - start_time
	print("finished in : " + str(duration) + "  sec")
