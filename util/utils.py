
import colorama
from colorama import *
import os
import subprocess
import socket
import time
import requests
import time
from datetime import datetime
import util
from util import utils
from util.program import *
import random


red = Fore.RED
reset = Fore.RESET
pink = Fore.MAGENTA
green = Fore.GREEN
blue = Fore.CYAN
cyan = Fore.BLUE

rdm = ['Call 911 please', "911 what's your emergency", 'FINISH HIM', "1337 H4X0R", "saori solo", "FICTION", "MINDSET"]
rrr = random.choice(rdm)

author = "saori.wx"
github = "https://github.com/akalpb"
discord = "https://discord.com/users/571974950823395328"
repo_name = 'a0ri-multitool'
latest_release = f'{github}/{repo_name}/releases/latest'


hostname = socket.gethostname()




banner = f"""


{green} $$$$$$\  $$\                                 $$$$$$$$\                  $$\           {reset}
{green} $$  __$$\ $$ |                                \__$$  __|                 $$ |          {reset}
{green} $$ /  $$ |$$ |  $$\ $$\   $$\  $$$$$$\           $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ {reset}
{green} $$$$$$$$ |$$ | $$  |\$$\ $$  |$$  __$$\          $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|{reset}
{green} $$  __$$ |$$$$$$  /  \$$$$  / $$ /  $$ |         $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  {reset}
{green} $$ |  $$ |$$  _$$<   $$  $$<  $$ |  $$ |         $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ {reset}
{green} $$ |  $$ |$$ | \$$\ $$  /\$$\ \$$$$$$  |         $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |{reset}
{green} \__|  \__|\__|  \__|\__/  \__| \______/          \__| \______/  \______/ \__|\_______/ {reset}  
                                                                    {green}  Aka : {green}{discord} {reset}
                                                                    {green}  Github : {green} {github}{reset}
{green}                                                                                              
_________________________________________________________________________________________
  
{green}[1] IPLOOKUP{reset}      {green}[4] PHONE LOOKUP{reset}      {green}[7] HYPESQUAD CHANGER{reset}  {green}[10] SERVER NUKER{reset}

{green}[2] STEALER{reset}       {green}[5] OSINT TOOL{reset}        {green}[8] DOX TOOL{reset}

{green}[3] SEARCHER{reset}      {green}[6] DOMAIN LOOKUP{reset}     {green}[9] TOKEN RAIDER{reset}       {green}{rrr}

{green} _________________________________________________________________________________________
"""





iplookup_banner = f"""
{green}


  _       _             _                
 (_)     | |           | |               
  _ _ __ | | ___   ___ | | ___   _ _ __  
 | | '_ \| |/ _ \ / _ \| |/ / | | | '_ \ 
 | | |_) | | (_) | (_) |   <| |_| | |_) |
 |_| .__/|_|\___/ \___/|_|\_\\__,_| .__/ 
   | |                            | |    
   |_|                            |_|    


                                                {reset}


"""

stealer_banner = r"""


     _______.___________. _______     ___       __       _______ .______      
    /       |           ||   ____|   /   \     |  |     |   ____||   _  \     
   |   (----`---|  |----`|  |__     /  ^  \    |  |     |  |__   |  |_)  |    
    \   \       |  |     |   __|   /  /_\  \   |  |     |   __|  |      /     
.----)   |      |  |     |  |____ /  _____  \  |  `----.|  |____ |  |\  \----.
|_______/       |__|     |_______/__/     \__\ |_______||_______|| _| `._____|
                                                                              

"""


searcher_banner = """

                     _               
  ___  ___  __ _ _ __ ___| |__   ___ _ __ 
 / __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__|
 \__ \  __/ (_| | | | (__| | | |  __/ |   
 |___/\___|\__,_|_|  \___|_| |_|\___|_|   
                                          

"""

phone_banner = """



 _______   __                                            __                            __                           
/       \ /  |                                          /  |                          /  |                          
$$$$$$$  |$$ |____    ______   _______    ______        $$ |        ______    ______  $$ |   __  __    __   ______  
$$ |__$$ |$$      \  /      \ /       \  /      \       $$ |       /      \  /      \ $$ |  /  |/  |  /  | /      \ 
$$    $$/ $$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |      $$ |      /$$$$$$  |/$$$$$$  |$$ |_/$$/ $$ |  $$ |/$$$$$$  |
$$$$$$$/  $$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$   $$<  $$ |  $$ |$$ |  $$ |
$$ |      $$ |  $$ |$$ \__$$ |$$ |  $$ |$$$$$$$$/       $$ |_____ $$ \__$$ |$$ \__$$ |$$$$$$  \ $$ \__$$ |$$ |__$$ |
$$ |      $$ |  $$ |$$    $$/ $$ |  $$ |$$       |      $$       |$$    $$/ $$    $$/ $$ | $$  |$$    $$/ $$    $$/ 
$$/       $$/   $$/  $$$$$$/  $$/   $$/  $$$$$$$/       $$$$$$$$/  $$$$$$/   $$$$$$/  $$/   $$/  $$$$$$/  $$$$$$$/  
                                                                                                          $$ |      
                                                                                                          $$ |      
                                                                                                          $$/       



"""


osint_banner = r"""


                                                                                  
                                                                                  
                                    iiii                            tttt          
                                   i::::i                        ttt:::t          
                                    iiii                         t:::::t          
                                                                 t:::::t          
   ooooooooooo       ssssssssss   iiiiiiinnnn  nnnnnnnn    ttttttt:::::ttttttt    
 oo:::::::::::oo   ss::::::::::s  i:::::in:::nn::::::::nn  t:::::::::::::::::t    
o:::::::::::::::oss:::::::::::::s  i::::in::::::::::::::nn t:::::::::::::::::t    
o:::::ooooo:::::os::::::ssss:::::s i::::inn:::::::::::::::ntttttt:::::::tttttt    
o::::o     o::::o s:::::s  ssssss  i::::i  n:::::nnnn:::::n      t:::::t          
o::::o     o::::o   s::::::s       i::::i  n::::n    n::::n      t:::::t          
o::::o     o::::o      s::::::s    i::::i  n::::n    n::::n      t:::::t          
o::::o     o::::ossssss   s:::::s  i::::i  n::::n    n::::n      t:::::t    tttttt
o:::::ooooo:::::os:::::ssss::::::si::::::i n::::n    n::::n      t::::::tttt:::::t
o:::::::::::::::os::::::::::::::s i::::::i n::::n    n::::n      tt::::::::::::::t
 oo:::::::::::oo  s:::::::::::ss  i::::::i n::::n    n::::n        tt:::::::::::tt
   ooooooooooo     sssssssssss    iiiiiiii nnnnnn    nnnnnn          ttttttttttt  

"""


domain_banner = r"""


    .___                    .__         .__                 __                 
  __| _/____   _____ _____  |__| ____   |  |   ____   ____ |  | ____ ________  
 / __ |/  _ \ /     \\__  \ |  |/    \  |  |  /  _ \ /  _ \|  |/ /  |  \____ \ 
/ /_/ (  <_> )  Y Y  \/ __ \|  |   |  \ |  |_(  <_> |  <_> )    <|  |  /  |_> >
\____ |\____/|__|_|  (____  /__|___|  / |____/\____/ \____/|__|_ \____/|   __/ 
     \/            \/     \/        \/                          \/     |__|    

"""

hschanger_banner = r"""

       __                                    __                  __                      __                           
      |  \                                  |  \                |  \                    |  \                          
  ____| $$  ______   ______ ____    ______   \$$ _______        | $$  ______    ______  | $$   __  __    __   ______  
 /      $$ /      \ |      \    \  |      \ |  \|       \       | $$ /      \  /      \ | $$  /  \|  \  |  \ /      \ 
|  $$$$$$$|  $$$$$$\| $$$$$$\$$$$\  \$$$$$$\| $$| $$$$$$$\      | $$|  $$$$$$\|  $$$$$$\| $$_/  $$| $$  | $$|  $$$$$$\
| $$  | $$| $$  | $$| $$ | $$ | $$ /      $$| $$| $$  | $$      | $$| $$  | $$| $$  | $$| $$   $$ | $$  | $$| $$  | $$
| $$__| $$| $$__/ $$| $$ | $$ | $$|  $$$$$$$| $$| $$  | $$      | $$| $$__/ $$| $$__/ $$| $$$$$$\ | $$__/ $$| $$__/ $$
 \$$    $$ \$$    $$| $$ | $$ | $$ \$$    $$| $$| $$  | $$      | $$ \$$    $$ \$$    $$| $$  \$$\ \$$    $$| $$    $$
  \$$$$$$$  \$$$$$$  \$$  \$$  \$$  \$$$$$$$ \$$ \$$   \$$       \$$  \$$$$$$   \$$$$$$  \$$   \$$  \$$$$$$ | $$$$$$$ 
                                                                                                            | $$      
                                                                                                            | $$      
                                                                                                             \$$      
                                                         

                    
"""

dox_banner = r"""

 ______   _______            _________ _______  _______  _        _______ 
(  __  \ (  ___  )|\     /|  \__   __/(  ___  )(  ___  )( \      (  ____ \
| (  \  )| (   ) |( \   / )     ) (   | (   ) || (   ) || (      | (    \/
| |   ) || |   | | \ (_) /      | |   | |   | || |   | || |      | (_____ 
| |   | || |   | |  ) _ (       | |   | |   | || |   | || |      (_____  )
| |   ) || |   | | / ( ) \      | |   | |   | || |   | || |            ) |
| (__/  )| (___) |( /   \ )     | |   | (___) || (___) || (____/\/\____) |
(______/ (_______)|/     \|     )_(   (_______)(_______)(_______/\_______)
                                                                          

"""


w_banner = r"""
                                                            
,-.----.                                                       
\    /  \                ,--,         ,---,                    
;   :    \             ,--.'|       ,---.'|            __  ,-. 
|   | .\ :             |  |,        |   | :          ,' ,'/ /| 
.   : |: |   ,--.--.   `--'_        |   | |   ,---.  '  | |' | 
|   |  \ :  /       \  ,' ,'|     ,--.__| |  /     \ |  |   ,' 
|   : .  / .--.  .-. | '  | |    /   ,'   | /    /  |'  :  /   
;   | |  \  \__\/: . . |  | :   .   '  /  |.    ' / ||  | '    
|   | ;\  \ ," .--.; | '  : |__ '   ; |:  |'   ;   /|;  : |    
:   ' | \.'/  /  ,.  | |  | '.'||   | '/  ''   |  / ||  , ;    
:   : :-' ;  :   .'   \;  :    ;|   :    :||   :    | ---'     
|   |.'   |  ,     .-./|  ,   /  \   \  /   \   \  /           
`---'      `--`---'     ---`-'    `----'     `----'            
                                                               
                                           
 
"""


nuker_banner = r"""

    _   __      __            
   / | / /_  __/ /_____  _____
  /  |/ / / / / //_/ _ \/ ___/
 / /|  / /_/ / ,< /  __/ /    
/_/ |_/\__,_/_/|_|\___/_/     
                              

"""