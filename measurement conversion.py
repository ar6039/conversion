# Measurement Conversion App

print("Welcome to the Measurement Conversion App!\n")

# Length Conversion
def length_conversion():
    print("Length Conversion:\n")
    length = float(input("Enter length to convert: "))
    from_unit = input("Enter the unit you want to convert from (in, ft, cm, m, mi, km): ")
    to_unit = input("Enter the unit you want to convert to (in, ft, cm, m, mi, km): ")
    
    # Conversion factor
    factors = {'in': 1, 'ft': 12, 'cm': 0.393701, 'm': 39.3701, 'mi': 63360, 'km': 39370.1}
    converted_length = length * factors[from_unit] / factors[to_unit]
    
    print(f"{length} {from_unit} is equal to {converted_length:.2f} {to_unit}.\n")

# Weight Conversion
def weight_conversion():
    print("Weight Conversion:\n")
    weight = float(input("Enter weight to convert: "))
    from_unit = input("Enter the unit you want to convert from (oz, lb, g, kg): ")
    to_unit = input("Enter the unit you want to convert to (oz, lb, g, kg): ")
    
    # Conversion factor
    factors = {'oz': 1, 'lb': 16, 'g': 0.035274, 'kg': 35.274}
    converted_weight = weight * factors[from_unit] / factors[to_unit]
    
    print(f"{weight} {from_unit} is equal to {converted_weight:.2f} {to_unit}.\n")

# Temperature Conversion
def temperature_conversion():
    print("Temperature Conversion:\n")
    temperature = float(input("Enter temperature to convert: "))
    from_unit = input("Enter the unit you want to convert from (F, C): ")
    to_unit = input("Enter the unit you want to convert to (F, C): ")
    
    # Conversion formula
    if from_unit == 'F' and to_unit == 'C':
        converted_temp = (temperature - 32) * 5/9
    elif from_unit == 'C' and to_unit == 'F':
        converted_temp = (temperature * 9/5) + 32
    else:
        print("Invalid unit selection.\n")
        return
    
    print(f"{temperature} {from_unit} is equal to {converted_temp:.2f} {to_unit}.\n")

# Main program
while True:
    print("Please select a conversion option:")
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Quit")
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        length_conversion()
    elif choice == 2:
        weight_conversion()
    elif choice == 3:
        temperature_conversion()
    elif choice == 4:
        print("Thank you for using the Measurement Conversion App!")
        break
    else:
        print("Invalid choice. Please try again.\n")
