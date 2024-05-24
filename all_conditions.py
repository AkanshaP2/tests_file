temperature = float(input("Enter the temperature in degrees Celsius: "))

# Conditional statements to classify the temperature
if temperature > 30:
    status = 'Hot'
    message = 'Stay cool!'
elif 20 <= temperature <= 30:
    status = 'Moderate'
    message = 'Enjoy the day.'
elif 10 <= temperature < 20:
    status = 'Cool'
    message = 'Wear a light jacket.'
else:
    status = 'Cold'
    message = 'Bundle up!'

# Display the result
print(f"\nFor a temperature of {temperature} degrees Celsius:")
print(f"Status: {status}")
print(f"Message: {message}")
