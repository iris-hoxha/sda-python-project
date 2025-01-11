name: str = "Il gusto Italiano"
type:  str = "Restaurant"
table_number = [1,2,3,4,5,6,7,8,9,10]
table_capacity: list[int] = [4,6,8,4,4,6,6,6,8,8]
table_status: list[str] = ["Free"] * 10
staff_nr: int = 13
staff_schedule: int = 0
daily_sales: float= 0
is_reserved: bool = False
main_menu: list[str]= ["Meat","Fish","Finger food"]

meat: list[str] = ["Steak", "Chicken", "Beef", "test",]
meat_prices: list[float] = [12.5, 9.0, 8.5]
fish: list[str] = ["Salmon", "Shrimp", "Fish"]
fish_prices: list[float] = [15.0, 12.0, 14.0]
finger_food: list[str] = ["Chicken Nuggets", "Mozzarella Sticks", "Onion Rolls"]
fingerFood_prices: list[float] = [4.5, 5.0, 3.5]

stock_drinks = {"Beer": 20,"Water": 30,"Wine": 15,"Orange Juice": 25, "Coffee": 50,"Tea": 40}
has_card_payment = True
restaurant_balance = 800
client_cash_balance = 20.5
client_card_balance = 10
client_bag = []

print(f"Welcome to {name} {type}!")


service = 0
while service != 1 and service != 2:
    print("Choose the service (1 or 2):  ")
    service = int(input())
    if service != 1 and service != 2:
        print("Please choose 1 or 2")
if service == 1:
    guests = int(input("Enter the Guests number:"))

    table_is_found = False
    for i in range(len(table_capacity)):
        if table_capacity[i] >= guests and table_status[i] == "Free":
            table_status[i] = "Reserved"
            table_is_found = True
            print(f"Table {i + 1} is successfully reserved")
            print(f"Please choose your meal from the following menu: {main_menu}")
        chosen_meal = input("Enter your choice: ").capitalize()
        if chosen_meal in main_menu:
            print(f"You've chosen {chosen_meal} menu.")
            print("Done")
        else:
            print("Invalid menu choice.")
        break
    else:
        print("No available tables for this number of guests. ")
elif service == 2:
    print("Please choose your meal from the following menu:")
    print("1. Meat")
    print("2. Fish")
    print("3. Finger food")
    meal = int(input("Enter the number corresponding to your choice: "))

    if meal == 1:
        print("You've chosen the Meat menu.")
        print("Available options: ", meat)
        chosen_meat = input("Enter your choice: ").capitalize()
        if chosen_meat in meat:
            meat_index = meat.index(chosen_meat)
            client_bag.append((chosen_meat, meat_prices[meat_index]))
            print(f"{chosen_meat} added to your order.")
        else:
            print("Invalid meat choice.")
    elif meal == 2:
        print("You've chosen the Fish menu.")
        print("Available options: ", fish)
        chosen_fish = input("Enter your choice: ").capitalize()
        if chosen_fish in fish:
            fish_index = fish.index(chosen_fish)
            client_bag.append((chosen_fish, fish_prices[fish_index]))
            print(f"{chosen_fish} added to your order.")
        else:
            print("Invalid fish choice.")
    elif meal == 3:
        print("You've chosen the Finger food menu.")
        print("Available options: ", finger_food)
        chosen_finger_food = input("Enter your choice: ").capitalize()
        if chosen_finger_food in finger_food:
            finger_food_index = finger_food.index(chosen_finger_food)
            client_bag.append((chosen_finger_food, fingerFood_prices[finger_food_index]))
            print(f"{chosen_finger_food} added to your order.")
        else:
            print("Invalid finger food choice.")
    else:
        print("Invalid choice.")


payment_method = input("How would you like to pay? (cash/card): ").lower()

if payment_method == "cash":
    if client_cash_balance >= total_price:
        client_cash_balance = client_cash_balance - product_price
        restaurant_balance = restaurant_balance + product_price
        stock[product] -= 1
        client_bag.append(product)
        print("Payment was successfully made with cash!")
        # print(f"Stoku i ri per {product} eshte: {stock[product]}")
    else:
        print("You do not have enough money!")
        exit()

elif payment_method == "card":
    if client_card_balance >= product_price:
        client_card_balance = client_card_balance - product_price
        restaurant_balance = restaurant_balance + product_price
        stock[product] -= 1
        client_bag.append(product)
        print("Payment was successfully made with the card!")
    else:
        print("You do not have enough limit on your card!")
        exit()

else:
    print("The chosen method is not valid!")
    exit()

print(f"The product was added to the bag: {client_bag}")
print(f"The new balance of the restaurant: {restaurant_balance}")
print(f"Your balance: cash: {client_cash_balance}, card: {client_card_balance} ")

rating = int(input("Give your rating for our restaurant (1-5 stars): "))
if 1 <= rating <= 5:
    print("Your rating", rating)
else:
    print("The number must be between 1 and 5.")
