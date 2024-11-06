
#Número invertido
#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241 
#142

numero = (input("Enter a three digit number: "))

if len(numero) == 3 and numero.isdigit():

    InvertedNumber = numero[::-1]
    print(InvertedNumber)
else:
    print("Please enter a valid three digit number.")
    