str = ("HelloWorld")
x = str.isalpha()
print(x)


str= "12322"
x = str.isnumeric()
print (x)

str= "Hello"
x = str.isupper()
print (x)

str = "welcome back"
x = str.split()
print(x)

str = "welcome back"
x = str.title()
print(x)

str = "welcome back"
x = str.strip()
print(x)

str = "welcome back"
x = str.replace("back", "home")
print(x)

str = "WElDFDDD bjdd"
x = str.casefold()
print(x)

str = "WElDFDDD laptop"
x = str.center(100)
print(x)

#
#
#
# name: str = "Ana"
# grades: list[int] = [4,10,10,7]
#
# school_price: int = 2500
# payment: float
#
# if len(grades) == 0:
#     print("List is empty")
#     exit()
#
# for grade in grades:
#     if not isinstance(grade, (int, float)):
#         print("Lista përmban vlera që nuk janë numra")
#         exit()
#     if grade < 4 or grade > 10:
#         print("Lejohen vetëm numra nga 4 deri te 10")
#         exit()
#
# total = sum(grades)
# average = total / len(grades)
#
# if average < 7:
#     payment = school_price
# elif 7 <= average < 9:
#     payment = school_price / 2
# else:
#     payment = 0
#
# print(f"{name} will pay {payment}")


