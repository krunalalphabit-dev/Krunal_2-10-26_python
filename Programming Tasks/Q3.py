'''03. Temperature converter
Read a temperature in Celsius and display Fahrenheit and Kelvin. Use F = C * 9 / 5 + 32 and K = C +
273.15. Format results to one or two decimal places.
Extension: Reject a temperature below absolute zero (-273.15 C).'''

celsius = float(input("Enter temperature in Celsius: "))

if celsius < -273.15:
    print("Invalid temperature!")
else:
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15

    print(f"Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Kelvin: {kelvin:.2f} K")