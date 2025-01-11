product_name: str = "Pizza"
product_price: float = 5.6
stock: int = 5
ingredients: list = ["domate, djath, proshute"]
table_number: int = 8
stock: int = 3
is_vegetarian: bool = "False"
client_rate: float = 4.5
staff_list: list = "Ani, Beni, Ana"
staff_salary: list [float]= [123.4, 124.4, 134.5]
has_online_payment: bool = "True"
if (stock > 0):
    print(f" {product_name} është në stok dhe mund të shitet për {product_price} $")
else:
    print(f"Pizza {product_name} nuk është në stok ")
emri_pizza: str = input("Cfare pizza deshironi? ")
print(f"Produkti qe ju zgjodhet eshte {emri_pizza}!")
if (is_vegetarian == False):
    print(f"{product_name} nuk është vegjetariane ")
else:
    print(f"{product_name} është vegjetariane ")















