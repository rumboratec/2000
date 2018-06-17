from easysnmp import Session
import BlynkLib
import time
import datetime
import os
import sys

ip = "10.10.17.3"

community = "public"

oid = ".1.3.6.1.4.1.37504.3.4.1.3.4.0" #POTENCIA TOTAL
oid2 = ".1.3.6.1.4.1.37504.3.4.1.3.6.0" # POTENCIA REFLETIDA
oid3 = ".1.3.6.1.4.1.37504.3.4.8.3.5.0" #STATUS BOMBA 1
oid4 = ".1.3.6.1.4.1.37504.3.4.8.3.6.0" #STATUS BOMBA 2
oid5 = ".1.3.6.1.4.1.37504.3.4.8.3.3.0" #PRESSAO
oid6 = ".1.3.6.1.4.1.37504.3.4.8.3.2.0" #TEMPERATURA
oid7 = ".1.3.6.1.4.1.37504.3.4.5.3.1.1.3.1" #POWER PA1
oid8 = ".1.3.6.1.4.1.37504.3.4.5.3.1.1.3.2" #POWER PA2
oid9 = ".1.3.6.1.4.1.37504.3.4.5.3.1.1.3.3" #POWER PA3
oid10 = ".1.3.6.1.4.1.37504.3.4.5.3.1.1.3.4" #POWER PA4
oid11 = ".1.3.6.1.4.1.37504.3.4.5.3.1.1.3.5" #POWER PA5
oid12 = ".1.3.6.1.4.1.37504.3.4.5.3.1.1.3.6" #POWER PA6
oid13 = ".1.3.6.1.4.1.37504.3.4.5.3.1.1.3.7" #POWER PA7
oid14 = ".1.3.6.1.4.1.37504.3.4.5.3.1.1.3.8" #POWER PA8
oid15 = ".1.3.6.1.4.1.37504.3.4.8.3.4.0" #NIVEL DO TANQUE
oid16 = ".1.3.6.1.4.1.37504.3.4.1.3.3.0" #STATUS TX
oid17 = ".1.3.6.1.4.1.37504.3.4.1.3.2.0" #EXCITADOR EM USO

session = Session(hostname = ip, community = community, version = 2)

BLYNK_AUTH = 'aef1a8506a9a44708fa7dedd78d13e3c'

# inicializa Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def my_user_task():
#    print('teste')

#    snmp_get = session.get(oid)
#    ptotal = snmp_get.value.encode('ascii')
#    ptotal = ptotal[0] + "." + ptotal[1:2]
#    blynk.virtual_write(3, ptotal)
#    print ("POTENCIA TOTAL -> ", ptotal)

    print ("<------------------------------------>")

    today = datetime.datetime.now()
    log = today.strftime("%d, %b %Y - %H:%M")  
    blynk.virtual_write(17,log)
    #blynk.virtual_write(29, "ONLINE")
    snmp_get = session.get(oid)
    ptotal = snmp_get.value
    ctotal = len(ptotal)
    if ctotal == 7:
     ctotal = ptotal[0:4]
     blynk.virtual_write(3, ctotal)
     print ("POTENCIA TOTAL -> ", ctotal)

    elif ctotal > 7:
     ctotal = ptotal[0:5]
     blynk.virtual_write(3, ctotal)
     print ("POTENCIA TOTAL -> ", ctotal)

    elif ctotal < 7:
     ctotal = ptotal[0:3]
     blynk.virtual_write(3, ctotal)
     print ("POTENCIA TOTAL -> ", ctotal)

    snmp_get = session.get(oid2)
    pref = snmp_get.value
    cref = len(pref)
    if cref == 7:
     cref = pref[0:4]
     blynk.virtual_write(4, cref)
     print ("POTENCIA REFLETIDA -> ", cref)

    elif cref > 7:
     cref = pref[0:5]
     blynk.virtual_write(4, cref)
     print ("POTENCIA REFLETIDA -> ", cref)

    elif cref < 7:
     cref = pref[0:3]
     blynk.virtual_write(4, cref)
     print ("POTENCIA REFLETIDA -> ", cref)

#    snmp_get = session.get(oid2)
#    result = snmp_get.value.encode('ascii')
#    result2 = result[0:3]
#    blynk.virtual_write(4, result2)
#    print ("POTENCIA REFLETIDA -> ", result2)

    snmp_get = session.get(oid3)
    bomba1 = snmp_get.value.encode('ascii')

    if bomba1 == "2":
     bomba1 = "Rodando"
     blynk.virtual_write(12, bomba1)
     print ("BOMBA 1 -> ", bomba1)

    if bomba1 == "1":
     bomba1 = "Standby"
     blynk.virtual_write(12, bomba1)
     print bomba1

    if bomba1 == "3":
      bomba1 = "Aviso"
      blynk.virtual_write(12, bomba1)
      print bomba1

    if bomba1 == "4":
      bomba1 = "Alarme"
      blynk.virtual_write(12, bomba1)
      print bomba1

    if bomba1 == "5":
      bomba1 = "Alarme"
      blynk.virtual_write(12, bomba1)
      print bomba1

    if bomba1 == "6":
      bomba1 = "Off"
      blynk.virtual_write(12, bomba1)
      print bomba1

    snmp_get = session.get(oid4)
    bomba2 = snmp_get.value.encode('ascii')
    if bomba2 == "2":
     bomba2 = "Rodando"
     blynk.virtual_write(14, bomba2)
     print ("BOMBA 2 -> ", bomba2)

    if bomba2 == "1":
     bomba2 = "Standby"
     blynk.virtual_write(14, bomba2)
     print bomba2

    if bomba2 == "3":
      bomba2 = "Aviso"
      blynk.virtual_write(14, bomba2)
      print bomba2

    if bomba2 == "4":
      bomba2 = "Alarme"
      blynk.virtual_write(14, bomba2)
      print bomba2

    if bomba2 == "5":
      bomba2 = "Alarme"
      blynk.virtual_write(14, bomba2)
      print bomba2

    if bomba2 == "6":
      bomba2 = "Off"
      blynk.virtual_write(14, bomba2)
      print bomba2

    snmp_get = session.get(oid5)
    pressao = snmp_get.value.encode('ascii')
    pressao = pressao[0] + "." + pressao[1:2]
    blynk.virtual_write(1, pressao)
    print ("PRESSAO -> ", pressao)

    snmp_get = session.get(oid15)
    nivelt = snmp_get.value
    nivelt = nivelt[0] + "." + nivelt[1:2]
    blynk.virtual_write(6, nivelt)
    print ("NIVEL DO TANQUE -> ", nivelt)

    snmp_get = session.get(oid16)
    stx = snmp_get.value
#    print ("STATUS TX -> ", stx)
    if stx == "1":
     blynk.virtual_write(0, "ON")
     print ("STATUS TX -> ", stx)
    elif stx == "0":
     blynk.virtual_write(0, "OFF")
     print ("STATUS TX -> ", stx)

    snmp_get = session.get(oid6)
    temp = snmp_get.value.encode('ascii')
    blynk.virtual_write(5, temp)
    print ("TEMPERATURA -> ", temp)

    snmp_get = session.get(oid17)
    exc = snmp_get.value
    if exc == "1":
     blynk.virtual_write(15, "DRIVE 1")
     print ("EXCITADOR EM USO -> ", exc)
    elif exc == "2":
     blynk.virtual_write(15, "DRIVE 2")
     print ("EXCITADOR EM USO -> ", exc)

    snmp_get = session.get(oid6)
    temp = snmp_get.value.encode('ascii')
    blynk.virtual_write(5, temp)
    print ("TEMPERATURA -> ", temp)


#    snmp_get = session.get(oid7)
#    pa1 = snmp_get.value.encode('ascii')
#    cpa1 = len(pa1)
#    icpa1 = int(cpa1)
#    if icpa1 <= 6:
#     rpa1 = pa1[0:3]
#     blynk.virtual_write(7, rpa1)
#     print ("PA1 -> ", rpa1)
#     print ("LEN CPA1 -> ", icpa1)

#    elif icpa1 > 6:
#     rpa1 = pa1[0:4]
#     blynk.virtual_write(7, rpa1)
#     print ("PA1 -> ", rpa1)
#     print ("LEN CPA1 -> ", icpa1)

    snmp_get = session.get(oid7)
    pa1 = snmp_get.value
    cpa1 = len(pa1)

    if cpa1 <= 6:
     rpa1 = pa1[0:3]
     blynk.virtual_write(7, rpa1)
     print ("PA1 ->", rpa1)

    elif cpa1 > 6:
     rpa1 = pa1[0:4]
     blynk.virtual_write(7, rpa1)
     print ("PA1- ->", rpa1)

    snmp_get = session.get(oid8)
    pa2 = snmp_get.value
    cpa2 = len(pa2)

    if cpa2 <= 6:
     rpa2 = pa2[0:3]
     blynk.virtual_write(16, rpa2)
     print ("PA2 ->", rpa2)

    elif cpa2 > 6:
     rpa2 = pa2[0:4]
     blynk.virtual_write(16, rpa2)
     print ("PA2- ->", rpa2)

    snmp_get = session.get(oid9)
    pa3 = snmp_get.value
    cpa3 = len(pa3)

    if cpa3 <= 6:
     rpa3 = pa3[0:3]
     blynk.virtual_write(13, rpa3)
     print ("PA3 ->", rpa3)

    elif cpa3 > 6:
     rpa3 = pa3[0:4]
     blynk.virtual_write(13, rpa3)
     print ("PA3- ->", rpa3)

    snmp_get = session.get(oid10)
    pa4 = snmp_get.value
    cpa4 = len(pa4)

    if cpa4 <= 6:
     rpa4 = pa4[0:3]
     blynk.virtual_write(8, rpa4)
     print ("PA4 ->", rpa4)

    elif cpa4 > 6:
     rpa4 = pa4[0:4]
     blynk.virtual_write(8, rpa4)
     print ("PA4- ->", rpa4)

    snmp_get = session.get(oid11)
    pa5 = snmp_get.value
    cpa5 = len(pa5)

    if cpa5 <= 6:
     rpa5 = pa5[0:3]
     blynk.virtual_write(9, rpa5)
     print ("PA5 ->", rpa5)

    elif cpa5 > 6:
     rpa5 = pa5[0:4]
     blynk.virtual_write(9, rpa5)
     print ("PA5- ->", rpa5)

    snmp_get = session.get(oid12)
    pa6 = snmp_get.value
    cpa6 = len(pa6)

    if cpa6 <= 6:
     rpa6 = pa6[0:3]
     blynk.virtual_write(10, rpa6)
     print ("PA6 ->", rpa6)

    elif cpa6 > 6:
     rpa6 = pa6[0:4]
     blynk.virtual_write(10, rpa6)
     print ("PA6 ->", rpa6)

    snmp_get = session.get(oid13)
    pa7 = snmp_get.value
    cpa7 = len(pa7)

    if cpa7 <= 6:
     rpa7 = pa7[0:3]
     blynk.virtual_write(11, rpa7)
     print ("PA7 ->", rpa7)

    elif cpa7 > 6:
     rpa7 = pa7[0:4]
     blynk.virtual_write(11, rpa7)
     print ("PA7 ->", rpa7)

    snmp_get = session.get(oid14)
    pa8 = snmp_get.value
    cpa8 = len(pa8)

    if cpa8 <= 6:
     rpa8 = pa8[0:3]
     blynk.virtual_write(2, rpa8)
     print ("PA8 ->", rpa8)

    elif cpa8 > 6:
     rpa8 = pa8[0:4]
     blynk.virtual_write(2, rpa8)
     print ("PA8 ->", rpa8)

    print ("<------------------------------------>")
    blynk.virtual_write(29, "ONLINE")
def reboot():
 blynk.virtual_write(29, "OFFLINE")
 blynk.virtual_write(0, "OFFLINE")
 blynk.virtual_write(15, "OFFLINE")
 blynk.virtual_write(5, "OFFLINE")
 blynk.virtual_write(3, "---")
 blynk.virtual_write(4, "---")
 blynk.virtual_write(12, "OFFLINE")
 blynk.virtual_write(14, "OFFLINE")
 blynk.virtual_write(1, "OFFLINE")
 blynk.virtual_write(6, "OFFLINE")
 blynk.virtual_write(7, "OFFLINE")
 blynk.virtual_write(16, "OFFLINE")
 blynk.virtual_write(13, "OFFLINE")
 blynk.virtual_write(8, "OFFLINE")
 blynk.virtual_write(9, "OFFLINE")
 blynk.virtual_write(10, "OFFLINE")
 blynk.virtual_write(11, "OFFLINE")
 blynk.virtual_write(2, "OFFLINE")

 python = sys.executable
 os.execl(python, python, * sys.argv)

try:
 blynk.set_user_task(my_user_task, 300000)
 blynk.run()
except Exception:
 blynk.set_user_task(reboot, 300000)
 blynk.run()
 pass
