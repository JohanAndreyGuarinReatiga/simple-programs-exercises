
#Hora futura
#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43 
#En 43 horas, el reloj marcara las 6

t= int(input("Enter the actual time: "))
h = int(input("Enter the hours: "))

FutureTime = (t + h) % 24

print(f"""
      "In {h} hours, the clock will mark {FutureTime}"
""")
