def Loe_failist(fail:str)->list:
    jarjend=[]
    f=open(fail,'r',encoding="utf-8-sig")
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend



paevad=Loe_failist("Paevad.txt")
print(paevad)



