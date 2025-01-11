welcome: str = "Hello world"

name1: str = ("Beni")
surname1: str=("Aristotel")
name2: str = ("Ana")
surname2: str= ("Bali")
print (welcome)
print(welcome[0])


print ("Kush student pyetet i pari?")
print(ord(name1[0]))
print(ord(name2[0]))

name1_char_code = ord(name1[0])
name2_char_code = ord(name2[0])

print(name1_char_code)
print(name2_char_code)

if(name1_char_code < name2_char_code):
    print(f"Studenti {name1} do te pyetet i pari")
    print(f"Studenti {name2} do te pyetet i dyti")
else:
    print(f"Studenti {name2} do te oyetet i pari")
    print(f"Studenti {name1} do te oyetet i dyti")

##########################################################################################

print("Rasti1: Kontrollo EMRAT e tyre")
name1: str = "Ana"