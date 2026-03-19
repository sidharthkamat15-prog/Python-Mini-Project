                                       # Number_Analyzer  
num = int(input("Enter a number to analyze: "))

def analyze_number(n):
    if n > 0:
        PNz = "Positive"
    elif n < 0:
        PNz = "Negative"
    else:
        PNz = "Zero"

    if n != 0:
        OnE = "Even" if n % 2 == 0 else "Odd"
        Dv3 = "Divisible by 3" if n % 3 == 0 else "Not divisible by 3"
    else:
        OnE = "Neither odd nor even"
        Dv3 = "Zero is divisible by all numbers"

    return PNz, OnE, Dv3


PNz, OnE, Dv3 = analyze_number(num)
print(f"The number is {PNz}, {OnE}, and {Dv3}.")