
#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5 
import math
radius = float(input("Enter the radius of a circle "))
perimeter = 2 * math.pi * radius
area = math.pi * radius**2
print(f""" The perimeter of the circle is: {perimeter} and the area is {area}""")
