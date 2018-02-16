# Ryan Mottahed – Chapter 3 – Exercise 1 – 021618

# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    pay = (hours - (hours - 40)) * rate + ((hours - 40) * rate * 1.5)
else:
    pay = hours * rate

print("Pay: " + str(pay))
