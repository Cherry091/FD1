# Mariuss Blumbergs 18.10.24
Vecums = int(input("Ievadi savu vecumu: ")) #Lietotājs ievada savu vecumu lai to varētu pārbaudīt
if (Vecums<13): # Pārbauda ja vecums ir mazāks par 13
    print("Tu esi bērns") #Izvada ka lietotājs ir bērns ja if statements piepildās
elif (Vecums>=13) and (Vecums<=19): #Pārbauda vai vecums ir lielāks vai vienāds ar 13 UN vienāds vai mazāks par 19
    print("Tu esi tīnis") #Izvada ka lietotājs ir tīnis ja elif statements piepildās
elif (Vecums>=20): #Pārbauda vai vecums ir lielāks vai vienāds ar 20
    print("Tu esi pieaugušais") #Izvada ka lietotājs ir pieaugušais ja elif statements piepildās