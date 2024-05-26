import util
from util import utils
from util.program import *
import asyncio
import util.program
import util.program.stealer
import os
utils.os.system('cls')

while True:

    async def menu():
        utils.os.system('cls')
        print(utils.banner)
     
        choice = input(f"""{utils.green}┌───({utils.reset}{utils.hostname}Aka{utils.green})─[{utils.reset}~{utils.green}]
└──{utils.reset}$ {utils.reset}""")
         

        if choice == '1':
            utils.os.system('cls')
            from util.program.iplookup import iplookup
            await iplookup()

            input(f'\n{utils.green}press enter to exit{utils.reset}')

        elif choice == '2':
            from util.program.stealer import stealer
            await stealer()
            input(f'\n{utils.green}press enter to exit{utils.reset}')

        elif choice == '3':
            from util.program.searcher import searcher
            await searcher()
            input(f'\n{utils.green}press enter to exit{utils.reset}')
         
        elif choice == '4':
            from util.program.phonelookup import phonelookup
            await phonelookup()
            input(f'\n{utils.green}press enter to exit{utils.reset}')
             
        elif choice == '5':
            from util.program.osint import osint
            await osint()
            input(f'\n{utils.green}press enter to exit{utils.reset}')

        elif choice == '6':
            from util.program.domainlookup import domainlookup
            await domainlookup()
            input(f'\n{utils.green}press enter to exit{utils.reset}')

        elif choice == '7':
            from util.program.hypesquadchanger import hypesquadchanger
            await hypesquadchanger()
            input(f'\n{utils.green}press enter to exit{utils.reset}')

        elif choice == '8':
            from util.program.dox import dox
            await dox()
            input(f'\n{utils.green}press enter to exit{utils.reset}')
            
        elif choice == '9':
            from util.program.raid import token_raid
            await token_raid().raider()
            input(f'\n{utils.green}press enter to exit{utils.reset}')
            
        elif choice == '10':
            utils.os.system('cls')
            from util.program.nuker import nuke
            await nuke()
            input(f'\n{utils.green}press enter to exit{utils.reset}')

        elif choice == '0':
            from util.program.latest import latest
            await latest()
            input(f'\n{utils.green}press enter to exit{utils.reset}')
              
        else:
            print(f'{utils.green}[+] INVALID CHOICE{utils.reset}')
            utils.time.sleep(2)

    asyncio.run(menu())
