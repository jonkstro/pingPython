import os
import requests

token = "5193651735:AAFPChZ2ZqNm4tUzvF81ZKhQoFbcqSnfCQw"
chatId = "-1001793924653"

#URL = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chatId+"&text=<MENSAGEM>"
URL = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chatId+"&text="

ipList = [['10.254.0.1', 'Serv. THE'],
          ['10.75.17.100','SE TBD'],
          ['10.75.17.101', 'DJ-13C1'],
          ['10.75.17.102', 'DJ-13C2'],
          ['10.75.17.103', 'DJ-12S1'],
          ['10.75.17.104', 'DJ-12S2'],
          ['10.75.17.105', 'DJ-12S3'],
          ['10.75.17.106', 'DJ-12S4'],
          ['10.75.17.107', 'DJ-12S8'],
          ['10.75.17.108', 'TF-03T1'],
          ['10.75.17.109', 'DJ-12T1'],
          ['10.75.17.110', 'TF-03T2'],
          ['10.75.17.111', 'DJ-12T2']            
        ]
for ip in ipList:
    response = os.popen("ping "+ ip[0] +" -n 4").read()
    if "Recebidos = 4" in response and "Aproximar " in response:
        print("ok pingou ip "+ip[1])
        mensagem = ("OK consegui pingar o IP: "+ip[1])
        #requests.get(URL+mensagem)
    else:
        while True:
            statusEquipamento = False
            for i in range(3):
                response = os.popen("ping "+ ip[0] +" -n 4").read()
                if "Recebidos = 4" in response and "Aproximar " in response:
                    print("ok pingou ip "+ip[1])
                    mensagem = ("OK consegui pingar o IP: "+ip[1])
                    statusEquipamento = True

            if statusEquipamento == False:
                print("nao pingou ip "+ip[1]+" apos 3 testes")
                mensagem = ("Nao foi possivel pingar o IP: "+ip[1]+" apos 3 tentativas")
                #requests.get(URL+mensagem)
                break
            
