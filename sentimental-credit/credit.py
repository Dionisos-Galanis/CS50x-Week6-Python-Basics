from cs50 import get_int

# Getting a CC number
number = get_int("Number: ")
sNumber = str(number)

digitsNo = len(sNumber)

# Choosing a potential card type, based on the number pf digits and first digits
digits = [x for x in range(digitsNo)]
for i in range(digitsNo):
    digits[i] = int(sNumber[digitsNo - i - 1])

result = "INVALID"
if digitsNo == 15:
    if digits[14] == 3 and (digits[13] == 4 or digits[13] == 7):
        result = "AMEX"
elif digitsNo == 13:
    if digits[12] == 4:
        result = "VISA"
elif digitsNo == 16:
    if digits[15] == 5 and digits[14] >= 1 and digits[14] <= 5:
        result = "MASTERCARD"
    elif digits[15] == 4:
        result = "VISA"

# Checking for validity
if not result == "INVALID":
    sum = 0
    dbld = 0

    for k in range(1, digitsNo, 2):
        dbld = 2 * digits[k]
        if dbld < 10:
            sum = sum + dbld
        else:
            sum = sum + int(dbld / 10) + dbld % 10

    for k in range(0, digitsNo, 2):
        sum = sum + digits[k]

    if not sum % 10 == 0:
        result = "INVALID"

# Printing the result
print(result)