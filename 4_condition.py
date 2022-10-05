input = input('Enter Fahrenheit Temperature: ')
try:
    fahrenheit = float(input)
    celcius = (fahrenheit - 32.0) * 5.0 / 9.0
    print(celcius)
except:
    print('Please enter a number')
