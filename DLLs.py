import os
import sys

def main():
    
    lista =  (os.listdir())

    #procurando o nuget.exe para setar seu nome na variavel
    getnuget = ''
    for arquivo in os.listdir():
        if arquivo.upper() == "NUGET.EXE":
            getnuget = arquivo

    # Upando Dlls
    command = " push -Source " + sys.argv[1] +" -ApiKey AzureDevOps " 
    for item in lista:
        os.system(getnuget + command + item)

main()