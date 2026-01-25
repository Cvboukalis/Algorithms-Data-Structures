#INPUT:
# amount, a float for the total purchase amount
# is_member, True if the customer is a member, False otherwise as a boolean.
# OUTPUT:
# Final price after discount, rounded to two decimal places as a float.

def calculate_discount(amount, is_member):
    if is_member == True:
        if amount > 100:
            return round((amount*.8),2)
        else:
            if (amount >= 50) & (amount <= 100):
                return round((amount * .9),2)
            else:
                if (amount >= 0) & (amount <=49.99):
                    return round((amount * .95),2)
    else:
        if amount > 100:
            return round((amount * .9),2)
        else:
            if (amount >= 50) & (amount <= 100):
                return round((amount * .95),2)
            else:
                if (amount >= 0) & (amount <=49.99):
                    return round((amount),2)
    pass

print(calculate_discount(120, True)) # Expected output: 96.00

print(calculate_discount(75, False)) # Expected output: 71.25

print(calculate_discount(40, True)) # Expected output: 38.00

print(calculate_discount(30, False)) # Expected output: 30.00