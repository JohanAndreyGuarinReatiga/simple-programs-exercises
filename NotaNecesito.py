#Qué nota necesito
#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)3
#NF=NC⋅0.7+NL⋅0.3
#Donde NC
# es el promedio de certámenes, NL
 #el promedio de laboratorio y NF
 #la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3

C1 = float(input("Enter the first exam score: "))
C2 = float(input("Enter the second exam score: "))
NL = float(input("Enter the laboratory score: "))

NC = (C1 + C2 + 65) / 3 # Promedio de certámenes
NF = (NC * 0.7) + (NL * 0.3) # Nota final

print(f"You need a score of {NF:.1f} in the third exam to achieve a final score of 60.")
print(f"Your current score in the third exam is {65:.1f}.") # Not

#REVISAR TODO EL CODIGO
