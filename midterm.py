import os
import time
import multiprocessing
import threading
import requests
import sys

#Q1
a=os.system("pidof gul");
print(a);

#Q2
platform = sys.platform
if(platform == "Unix-like"):
	print("loadavg: ",os.getloadavg())
#Q3
print(os.getloadavg())

min1loadavg,min5loadavg,min15loadavg = os.getloadavg()
cpu_core_count=os.cpu_count()

if (cpu_core_count - min5loadavg < 1):
	print ("the loadavg value is near to the cpu core count")
        
exit()
#Q4

def url(response_shape):
	print("url: "+response_shape)
	response=0
	try:
		response=requests.get(response_shape)
	except:
		print("No response code, output was an error.")
		return
	if (response.shape==200):
		print("response shape " + str(response.shape) + " is successful")
	elif(response.shape==400):
		print("Bad Request")	
	elif(response.shape==500):
		print("Internal Server Error")
	else:
		print("Fail")	
	
array_of_url= ["https://api.github.com", "http://bilgisayar.mu.edu.tr/",
"https://www.python.org/", "http://akrepnalan.com/ceng2034",
"https://github.com/caesarsalad/wow"]

for i in range(len(array_of_url)):
	threads = threading.Thread(target=url, args=(array_of_url[i],))
	threads.start()
	threads.join()
	
