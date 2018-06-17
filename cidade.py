from easysnmp import Session
import BlynkLib
import time
import os
import sys

ip = "192.168.100.24"

community = "public"

#oid4 = ".1.3.6.1.4.1.37504.3.4.8.3.3.0" #PRESSAO
oid4 = ".1.3.6.1.2.1.1.1.0"

session = Session(hostname = ip, community = community, version = 2)

BLYNK_AUTH = 'aef1a8506a9a44708fa7dedd78d13e3c'

#response = os.system("ping -c 1 " + ip)

blynk = BlynkLib.Blynk(BLYNK_AUTH)
 
def my_user_task():
#  session = Session(hostname = ip, community = community, version = 2)

  snmp_get = session.get(oid4)
  pressao = snmp_get.value.encode('ascii')
  blynk.virtual_write(29, pressao)
  print pressao

def my_user_task2():
  blynk.virtual_write(29, "Teste")
  print ("Teste")

def reboot():
 blynk.virtual_write(29, "OFFLINE")
 python = sys.executable
 os.execl(python, python, * sys.argv)

try:
 blynk.set_user_task(my_user_task, 3000) 
 blynk.run()

except Exception:
  blynk.set_user_task(reboot, 3000)
  blynk.run()
  pass
