while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        print("Distance in Miles =", round(km * 0.621371, 2))
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit =", round((celsius * 9 / 5) + 32, 2))
    elif choice == "3":
        kg = float(input("Enter weight in kilograms: "))
        print("Weight in Pounds =", round(kg * 2.20462, 2))
    elif choice == "4":
        print("Exiting Unit Converter.")
        break
    else: print("Invalid Choice!")
