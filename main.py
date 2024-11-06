
import math 
TO = float(input("Temperatura original del huevo\n")) #temperatura original del huevo
TW = 100 #temperatura del agua para alcanzar la ebullicion
TY = 70 #temperatura de la yema para coagularse 
M = 67 #masa del huevo 47 = peque;o y 67 grande
P = 1.038 #constate de la formula
C = 3.7 #constante de la formula
K = 5.4 * math.pow(10, -3) #formula de conductividad termica

dividendo = math.pow(M, (2/3)) * (C * (math.pow(P, (1/3))))
divisor = (K * math.pow(math.pi, 2)) * math.pow((4*math.pi)/3, (2/3))
resultado = dividendo / divisor

resulta2 = math.log(0.76 * (TO - TW) / (TY - TW))

segundos = resultado * resulta2
minutos = round(segundos/60)

print(f"El tiempo maximo para prepararlo a la copa {round(segundos)} segundos")
#print(f"El tiempo maximo para prepararlo a la copa {minutos} minutos") 