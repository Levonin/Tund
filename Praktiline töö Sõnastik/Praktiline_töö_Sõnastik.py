# main.py
from salary_module import add_people_and_salaries

def Loe_failist(fail:str)->list:

def Kirjuta_failisse(fail:str,jarjend:list):


from gtts import gTTS
def Heli(text:str,keel:str):
    obj=gTTS(text=text, lang=keel, slow=False).save("heli.mp3")
    system("heli.mp3")

test_to_speech=""#-----------------------------------
paevad, test_to_speech=Loe_failist("Paevad.txt")#-----------------
print(paevad)
list_=[]
for i in range(5):
    nimi=input(str(i+1))+".Nimi ")
    list.append(nimi)
Kirjuta_failisse("Nimed.txt", list_)

with open ("Nimed.txt", 'r') as f:
    print(f.read())

from os import *
if path.isfile ("Nimi.txt"): #path.isdir(kaust)
   remove("Nimed.txt") #faili kustutamine, kui ta olemas
   from ggts import gTTS

Heli(test_to_speech,"et")