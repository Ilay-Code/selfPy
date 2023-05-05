def distance(num1, num2, num3):
    if abs(num2 - num1) == 1 or abs(num3 - num1) == 1:
        return True
    elif (abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2) or (abs(num3 - num1) >= 2 and abs(num3 - num2) >= 2):
        return True
