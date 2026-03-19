                                 # Temperature Convertor

print("Welcom to the Temperature Convertor!")

print("-----MENU-----")
print("\n1_Celsius → Fahrenheit")
print("2_Fahrenheit → Celsius")
print("3_Celsius → Kelvin")
print("4_Kelvin → Celsius")
print("5_Fahrenheit → Kelvin")
print("6_Kelvin → Fahrenheit")

choice = input("\nChoose the conversion (1-6): ")
temp = float(input("\nEnter the temperature to convert: "))

if choice == "1":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C is {converted}°F")
elif choice == "2":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F is {converted}°C") 
elif choice == "3":
    converted = temp + 273.15
    print(f"{temp}°C is {converted}K")
elif choice == "4":
    converted = temp - 273.15
    print(f"{temp}K is {converted}°C")
elif choice == "5":
    converted = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F is {converted}K")
elif choice == "6":
    converted = (temp - 273.15) * 9/5 + 32
    print(f"{temp}K is {converted}°F")
else:
    print("Invalid choice. Please select a number between 1 and 6.")