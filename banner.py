from colorama import Fore as color
from time import sleep 

bold = '\033[1m'
endbold = '\033[0m'

def banner():
    print(bold+color.RED+'''
        
  __  __ _____    _____ ____  ______ _  _  __ ______ 
 |  \/  |  __ \  |  __ \___ \|  ____| || |/_ |____  |
 | \  / | |__) | | |  | |__) | |__  | || |_| |   / / 
 | |\/| |  _  /  | |  | |__ <|  __| |__   _| |  / /  
 | |  | | | \ \ _| |__| |__) | |       | | | | / /   
 |_|  |_|_|  \_(_)_____/____/|_|       |_| |_|/_/    
                                                     
                                                
     '''+endbold)

    print(bold+color.WHITE+'''
    ------------------------------------
    ⚒  Programmer: MR.D3F417           ⚒
    ⚒  Lable : BlackGUARD              ⚒
    ⚒  Discord : discord.gg/KsskgvE48z ⚒
    ------------------------------------
     '''+endbold)  
    sleep(1)
def menu():

    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[2]"+color.LIGHTYELLOW_EX+" Hex")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[3]"+color.LIGHTYELLOW_EX+" Rot13")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[4]"+color.LIGHTYELLOW_EX+" Decoder")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[0]"+color.LIGHTYELLOW_EX+" exit"+endbold)



def decoder_menu():
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[2]"+color.LIGHTYELLOW_EX+" Hex")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[3]"+color.LIGHTYELLOW_EX+" Rot13")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[0]"+color.LIGHTYELLOW_EX+" back"+endbold)