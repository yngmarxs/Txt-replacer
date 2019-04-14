import sys           # File manipulation for saving and reading files
import numpy as np   # Array stuff
import os            # File manipulation
textObsahArrayVysledek1=[] #Definition of arrays
textObsahArrayVysledek=[]  #        ^

print("Write the name of the input file")
nazevSouboruOrig = input()
nazevSouboru = nazevSouboruOrig + (".txt")
cestaPython = os.path.dirname(os.path.realpath(__file__))
cestaSouboru = cestaPython + ("/input/") + nazevSouboru
textObsah = open(cestaSouboru, "r")
textObsahArray = textObsah.read().split("\n")
print("Write the config")
nazevProfilu = input()
nazevProfiluA = nazevProfilu + (".txt")
cestaProfiluA = cestaPython + ("/config/") + nazevProfiluA
ProfilAObsah = open(cestaProfiluA, "r")
ProfilAObsahArray = ProfilAObsah.read().split("\n")
exec(ProfilAObsahArray[0])
exec(ProfilAObsahArray[1])
exec(ProfilAObsahArray[2])
exec(ProfilAObsahArray[3])
exec(ProfilAObsahArray[4])
exec(ProfilAObsahArray[5])
exec(ProfilAObsahArray[6])
exec(ProfilAObsahArray[7])
exec(ProfilAObsahArray[8])
exec(ProfilAObsahArray[9])

exec(ProfilAObsahArray[11])
exec(ProfilAObsahArray[12])
#13
exec(ProfilAObsahArray[14])
exec(ProfilAObsahArray[15])
#16
exec(ProfilAObsahArray[17])
exec(ProfilAObsahArray[18])
#19
exec(ProfilAObsahArray[20])
exec(ProfilAObsahArray[21])
#22
exec(ProfilAObsahArray[23])
exec(ProfilAObsahArray[24])
#25
exec(ProfilAObsahArray[26])
exec(ProfilAObsahArray[27])
#28
exec(ProfilAObsahArray[29])
exec(ProfilAObsahArray[30])
#31
exec(ProfilAObsahArray[32])
exec(ProfilAObsahArray[33])
#34
exec(ProfilAObsahArray[35])
exec(ProfilAObsahArray[36])
#37
exec(ProfilAObsahArray[38])
exec(ProfilAObsahArray[39])

for x in textObsahArray:
    if x==chyba1:
        x=spravne1
    elif x==chyba2:
        x=spravne2
    elif x==chyba3:
        x=spravne3
    elif x==chyba4:
        x=spravne4
    elif x==chyba5:
        x=spravne5
    elif x==chyba6:
        x=spravne6
    elif x==chyba7:
        x=spravne7
    elif x==chyba8:
        x=spravne8
    elif x==chyba9:
        x=spravne9
    elif x==chyba0:
        x=spravne0
    textObsahArrayVysledek.append(x)
    textObsahArrayVysledek = list(filter(None, textObsahArrayVysledek))
print("Word exchange done")

cestaSouboruVys = cestaPython + ("/output/") + nazevSouboruOrig + (".txt")
textObsahArrayVysledek= str('\n'.join(textObsahArrayVysledek))
f=open(cestaSouboruVys, "w+")
f.write(textObsahArrayVysledek)
f.close()
print("Saved into" + (" ") + cestaSouboruVys + ".")
