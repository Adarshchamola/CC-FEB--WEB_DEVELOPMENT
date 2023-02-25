import math
import time

"""Unit Converter"""
# variable setting
cat = input("Which category would you like to convert? we support length(l), Weight(w) and temperature(t):  ")
if cat == ("l"):
    print("Press the following keys:")
    print('km: kilometer\nm: meter\ncm: centimeter\nmm:  millimeter')
    unit1 = input("Which unit would you like to convert from: ")
    unit2 = input("Which unit would you like to convert to: ")
    num1 = input("Enter your value: ")

##Calculations

    if unit1 == "cm" and unit2 == "m":
        ans = float(num1) / 100
    elif unit1 == "mm" and unit2 == "cm":
        ans = float(num1) / 10
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1) * 100
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1) * 10
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1) / 1000
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1) * 1000
    elif unit1 == "km" and unit2 == "m":
        ans = float(num1) * 1000
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1) / 1000
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1) / 1000000
    elif unit1  == 'km' and unit2 == 'cm':
        ans = float(num1) * 100000
    elif unit1 == 'cm' and unit2 == 'km':
        ans = float(num1) / 100000
    elif unit1 == 'km' and unit2 == 'mm':
        ans = float(num1) * 1000000
    else:
        ans = 'Unit not found'

elif cat == ("w"):
    print("Press the following keys")
    print("kg: kilogram\ng: gram\nmg: milligram\nlb: pounds")
    unit1 = input("Which unit would you like to convert from: ")
    unit2 = input("Which unit would you like to convert to: ")
    num1 = input("Enter your value: ")

    if unit1 == 'kg' and unit2 == 'g':
        ans = float(num1)*1000
    elif unit1 == 'g' and unit2 == 'kg':
        ans = float(num1) / 1000
    elif unit1 == 'kg' and unit2 == 'mg':
        ans = float(num1) * 1000000
    elif unit1 == 'mg' and unit2 == 'kg':
        ans = float(num1) / 1000000
    elif unit1 == 'kg' and unit2 == 'lb':
        ans = float(num1) * 2.205
    elif unit1 == 'lb' and unit2 == 'kg':
        ans = float(num1) / 2.205
    elif unit1 == 'g' and unit2 == 'mg':
        ans = float(num1) * 1000
    elif unit1 == 'mg' and unit2 == 'g':
        ans = float(num1) / 1000
    elif unit1 == 'g' and unit2 == 'lb':
        ans = float(num1) * 0.0022
    elif unit1 == 'lb' and unit2 == 'g':
        ans = float(num1) * 453.59
    elif unit1 == 'mg' and unit2 == 'lb':
        ans = float(num1) / 453592.37
    elif unit1 == 'lb' and unit2 == 'mg':
        ans = float(num1) * 453592.37
    else:
        ans = 'Unit not found'

elif cat == ('t'):
    print("Press the following keys")
    print("C: Celsius\nF: Fahrenheit\nK: Kelvin")
    unit1 = input("Which unit would you like to convert from: ")
    unit2 = input("Which unit would you like to convert to: ")
    num1 = input("Enter your value: ")

    if unit1 == 'C' and unit2 == 'F':
        ans = (float(num1) * 1.8) + 32
    elif unit1 == 'F' and unit2 == 'C':
        ans = (float(num1) - 32) * 0.555555556
    elif unit1 == 'C' and unit2 == 'K':
        ans = float(num1) + 273.15
    elif unit1 == 'K' and unit2 == 'C':
        ans = float(num1) - 273.15
    elif unit1 == 'F' and unit2 == 'K':
        ans = (float(float(num1)-32)*0.555555556) + 273.15
    elif unit1 == 'K' and unit2 == 'F':
        ans = (float(float(num1)-273.15)*1.8) + 32
    else:
        ans = 'Unit not found'

print(ans)
print(':)')