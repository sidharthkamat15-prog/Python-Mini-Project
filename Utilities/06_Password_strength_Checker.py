                                            #  Password Strength Checker

password = input("ENTER YOUR PASSWORD: ")

length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True

if length < 8:
    strength = "WEAK"
elif has_upper and has_lower and has_digit and has_special:
    strength = "STRONG"
elif has_digit and (has_upper or has_lower):
    strength = "MEDIUM"
else:
    strength = "WEAK"

print("\n--- Password Analysis ---")
print("Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digit:", has_digit)
print("Special Character:", has_special)
print("Password Strength:", strength)
