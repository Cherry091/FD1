# Mariuss Blumbergs 18.10.24
correct_password = "python123" #Mainīgo correct_password uzliek kā python123
while True: #Bezgalīgs cikls
    parole = (input("Ievadi paroli:")) #Lietotājs ievada savu paroles minējumu
    if parole == correct_password: #Ja parole ir vienāda ar pareizo paroli
        break #beigt ciklu
    print ("Piekļuve liegta") #Savādāk, printēt ka piekļuve liegta un turpināt ciklu
print ("Piekļuve atļauta!") #Ja cilks tiek lauzts, tiek printēts Piekļuve atļauta! 