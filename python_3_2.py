# Ryan Mottahed – Chapter 3 – Exercise 2 – 020618

# Rewrite your pay program using "try" and "except" so that your program handles non-numeric input gracefully by printing a message and exiting the program.

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hours > 40:
        pay = (hours - (hours - 40)) * rate + ((hours - 40) * rate * 1.5)
    else:
        pay = hours * rate
    print("Pay: " + str(pay))
except:
    print("Error, please enter numeric input")
