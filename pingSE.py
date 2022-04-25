import os
import requests

token = "qNm4tUzvF81ZKhQoFbcqSnfCQw"
chatId = "-10653"

URL = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chatId+"&text="

ipList = [['10.0.0.1', 'SE'],
          ['10.0.0.2', 'TF-02T1'],
          ['10.0.0.3', 'TF-02T2']            
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
            
