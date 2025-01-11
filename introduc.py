print ("Hello world")

#Vote
age = input("Sa vjec je?")
print ("Ti je" + age + "vjec!")

if (int(age) >= 18):
    print ("Ti mund te votosh")
else:
    print("Ti nuk mund te votosh")

# Gjejme mesataren e numrave

mes: float = 0
total: float=0
count: int = 0

for i in range (1,4):
    nr = float(input ("Give your number:"))
    count = i + 1
    total = total + nr
mes = total/count
print(f"Mesatarja e nr te dhene eshte: {mes}" )

#Gjatesia e nje fjale

fjala = str (input ("Shkruj fjalen:"))
gjatesia = len(fjala)
print(f"Gjatesia e fjales {fjala} eshte {gjatesia} karaktere.")

