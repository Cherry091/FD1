vecums = int(input("Ievadi savu vecumu: "))
pase = (input("Vai tev ir derīga pase?: "))
if (vecums>=18) and pase == "jā":
    print("Tu varu balsot")
elif (vecums<18) or pase == "nē":
    print("Viens no kritērijiem neizpildās")
elif (vecums<18) and pase == "nē":
    print("Abi no kritērijiem neizpildās")
if not pase == "jā" or pase == "nē":
    print ("Kļūdaini dati")