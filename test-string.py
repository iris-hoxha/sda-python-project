
#input
name: str ="Ana"
grades:list[int] = [7, 8, 8, 7]
school_price = 2500
student_payment:float
#logic
total = sum(grades)
print(total)
average = sum(grades)/len(grades)
print(average)

if (average < 7):
    student_payment = school_price
elif (7 < average and 9 > average):
    student_payment = school_price/2
else:
     student_payment = 0

print(f"{name} payment: {student_payment}")


