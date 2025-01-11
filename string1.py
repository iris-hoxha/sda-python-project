# name = "Ana Tot"
# x = name.split()
# print(x)

# name = "Ana Tot"[::-1]
# print(name)
#
# name = "Ana Tot"
# x = name.replace("Ana","Frasheri")
# print(x)

# name = "Ana Tot"
# count = name.lower().count("a")
# print(f"Shkronja 'A' është përmendur {count} herë.")

# name = "Ana Tot"
# surname = "Frasheri"
# new_name = name + " " + surname
# print(new_name)

# # "Ana" vendosi te mbaje nje emer te mesit, emer pagezimi... => "Ana (Anastasia) Toti"
#
# original_string = "Ana Tot"
# string_to_insert = ("Anastasia")
# middle_index = len(original_string) // 2  # Gjej pozitën e mesme
# new_string = original_string[:middle_index]+ " " + string_to_insert + original_string[middle_index:]
# print(new_string)

# Jepet nje menu boshe: menu: list[str] = []
# Mbushe me 3 elemente Pizza, Spaghetti, Fish
# Fshij elementin e 2-te "Spaghetti"
# kerko nese gjenet "pizza" ne menu
#
menu_list  = []
menu_list.extend (["pizza", "spaghetti", "fish"])
print(menu_list)
menu_list.remove ("spaghetti")
menu_list = (["pizza", "spaghetti", "fish"])
if ("spaghetti" in menu_list):
    print("Element exists in the list")
else:
    print("Element does not exist")

# krijo nje liste me cmimet 4.0, 6.5 per produktet e listes
# Gjej produktin me cmimin me te larte

price_list = [4.0, 6.5]
max = 0
max_index = -1
for i in range(len(price_list)):
    if i > max:
        max = price_list[i]
        max_index = i

menu_list.remove(menu_list[max_index])
price_list.remove(price_list[max_index])

print(max)
print(max_index)

print(f"{menu_list}: {price_list}")

price_list = [4.0]
max = 0
max_index = -1
for i in range(len(price_list)):
    if i > max:
        max = price_list[i]
        max_index = i

menu_list.remove(menu_list[max_index])
price_list.remove(price_list[max_index])

print(max)
print(max_index)

price_list = [4.0, 6.5]

def find_most_Expensive_product(menu_list, price_list):
    max = 0
    max_index = -1
    for i in range(len(price_list)):
        if i > max:
            max = price_list[i]
            max_index = i

    menu_list.remove(menu_list[max_index])
    price_list.remove(price_list[max_index])
    return max_index
















