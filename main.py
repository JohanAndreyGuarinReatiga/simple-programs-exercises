#Qué nota necesito
#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)/3
#NF=NC⋅0.7+NL⋅0.3

#Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3

C1 = int(input("Enter the first exam score: "))
C2 = int(input("Enter the second exam score: "))
NL = int(input("Enter the laboratory score: "))

NC = (59.5 - 0.3 * NL) / 0.7 # Promedio de certámenes 

C3 = 3 * NC - (C1 + C2) + 1 
RC3 = round(C3)
print(f"You need a score of {RC3} to achieve a final score of 60.")

